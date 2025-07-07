import os
import pandas as pd
import json

columns_to_predict = ['rightCheekRiseValue', 'leftCheekRiseValue', 'rightSmileValue',
                      'leftSmileValue', 'rightDimplerValue', 'leftDimplerValue',
                      'leftBrowLowerValue', 'rightBrowLowerValue', 'leftInnerBrowRiseValue',
                      'rightInnerBrowRiseValue', 'leftLidTightnerValue', 'rightLidTightnerValue',
                      'jawDropValue', 'leftLidRiserValue', 'rightLidRiserValue', 'leftLipCornerDepressor',
                      'rightLipCornerDepressor' , 'label']

# Function which replacing comma to dot in data
#
# data : pd.DataFrame - data
def replace_comma_with_dot(data: pd.DataFrame):
    if data.empty:
        raise Exception("Dane są puste")

    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].str.replace(',', '.', regex=False)


def merge_data():
    folder_path = 'data'
    all_dataframes = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)

            try:
                df = pd.read_csv(file_path, usecols=columns_to_predict, sep=';')
                all_dataframes.append(df)
                print(f"Wczytano plik: {filename}")

            except ValueError as e:
                print(f"Błąd w pliku {filename}: {e}. Plik został pominięty.")

    if all_dataframes:
        final_df: pd.DataFrame = pd.concat(all_dataframes, ignore_index=True)
        print(f"Wczytano dane z {len(all_dataframes)}")
        replace_comma_with_dot(final_df)
        return final_df

    else:
        print("Nie znaleziono żadnych pasujących plików CSV lub wystąpiły błędy.")


def display_count_of_labels(data: pd.DataFrame):
    print("Emocje:")
    print(data['label'].value_counts())


def drop_label_column(data: pd.DataFrame):
    new_data: pd.DataFrame = data.drop(columns=['label'])
    return new_data


def detect_eye_rotation(data: pd.DataFrame):
    num_rows = data.shape[0]

    is_up = (data['rightEyeUpValue'] > 0.5) & (data['leftEyeUpValue'] > 0.5)
    is_down = (data['rightEyeDownValue'] > 0.5) & (data['leftEyeDownValue'] > 0.5)
    is_right = (data['rightEyeRightValue'] > 0.5) & (data['leftEyeRightValue'] > 0.5)
    is_left = (data['rightEyeLeftValue'] > 0.5) & (data['leftEyeLeftValue'] > 0.5)

    is_v_center = ~is_up & ~is_down
    is_h_center = ~is_right & ~is_left

    counts = {
        'upper_right': (is_up & is_right).sum(),
        'upper_left': (is_up & is_left).sum(),
        'upper_center': (is_up & is_h_center).sum(),

        'right': (is_v_center & is_right).sum(),
        'left': (is_v_center & is_left).sum(),
        'center': (is_v_center & is_h_center).sum(),

        'bottom_right': (is_down & is_right).sum(),
        'bottom_left': (is_down & is_left).sum(),
        'bottom_center': (is_down & is_h_center).sum(),
    }

    if num_rows > 0:
        final_proportions = {key: round(value / num_rows * 100, 2) for key, value in counts.items()}
    else:
        final_proportions = {key: 0 for key in counts.keys()}

    return final_proportions

def count_blinking(data: pd.DataFrame):
    blinks_count = 0

    blink_state = 'OPEN'

    is_half_closed = (data['rightEyeClosedValue'] > 0.5) | (data['leftEyeClosedValue'] > 0.5)
    is_fully_closed = (data['rightEyeClosedValue'] > 0.7) | (data['leftEyeClosedValue'] > 0.7)

    for i in range(len(data)):
        half = is_half_closed.iloc[i]
        full = is_fully_closed.iloc[i]


        if blink_state == 'OPEN':
            if half:
                blink_state = 'ENTERING_BLINK'

        elif blink_state == 'ENTERING_BLINK':
            if full:
                blink_state = 'FULLY_CLOSED'
            elif not half:
                blink_state = 'OPEN'

        elif blink_state == 'FULLY_CLOSED':
            if not half:
                blinks_count += 1
                blink_state = 'OPEN'

    return blinks_count

import pandas as pd

def count_emotions(data: pd.DataFrame):
    flag_map = {
        0: 'normal',
        1: 'starting',
        2: 'turbulence',
        3: 'landing'
    }

    counts = data.groupby(['flag', 'label']).size()

    emotions = {
        'starting': {'natural': 0, 'happy': 0, 'sad': 0, 'surprised': 0, 'disturbed': 0},
        'turbulence': {'natural': 0, 'happy': 0, 'sad': 0, 'surprised': 0, 'disturbed': 0},
        'landing': {'natural': 0, 'happy': 0, 'sad': 0, 'surprised': 0, 'disturbed': 0},
        'normal': {'natural': 0, 'happy': 0, 'sad': 0, 'surprised': 0, 'disturbed': 0}
    }

    for (flag, label), count in counts.items():
        phase_name = flag_map.get(flag)
        if phase_name and label in emotions[phase_name]:
            emotions[phase_name][label] = count

    return emotions

def export_to_json(data, filename : str):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Dane zostały pomyślnie zapisane do pliku: {filename}")
