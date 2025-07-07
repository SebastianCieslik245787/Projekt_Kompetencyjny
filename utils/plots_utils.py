import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Function which shows plot from data
#
#time_col - column with time value (x axis)
#value_col - column with data (y axis)
#title - title for plot, default None
#xaxis_label - name for x axis, default None
#yaxis_label - name for y axis, default None
def show_plot(time_col, value_col, title=None, xaxis_label=None, yaxis_label=None):
    plt.figure(figsize=(10, 5))
    plt.plot(time_col, value_col, linestyle='-', color='b')

    plt.xticks(np.linspace(time_col.min(), time_col.max(), 10))
    plt.yticks(np.linspace(value_col.min(), value_col.max(), 10))

    plt.xlabel(xaxis_label)
    plt.ylabel(yaxis_label)
    plt.title(title if title else f'{yaxis_label} over {xaxis_label}')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#Function which shows plots for closed eyes
#
#data : pd.DataFrame - data, must contain unityGameTime, leftEyeClosedValue and rightEyeClosedValue
def show_closed_eyes_plot(data : pd.DataFrame):
    show_plot(data['unityGameTime'], data['leftEyeClosedValue'], "Zamknięcie lewego oka", "Czas [s]",
              "Zamknięcie lewego oka [%]")
    show_plot(data['unityGameTime'], data['rightEyeClosedValue'], 'Zamknięcie prawego oka', "Czas [s]",
              "Zamknięcie prawego oka [%]")

#Function which shows plots for chicks rise
#
#data : pd.DataFrame - data, must contain unityGameTime, leftCheekRiseValue and rightCheekRiseValue
def show_chick_risen_plot(data : pd.DataFrame):
    show_plot(data['unityGameTime'], data['leftCheekRiseValue'], "Uniesienie lewego polika", "Czas [s]",
              "Uniesienie lewego polika [%]")
    show_plot(data['unityGameTime'], data['rightCheekRiseValue'], 'Uniesienie prawego polika', "Czas [s]",
              "Uniesienie prawego polika [%]")

#Function which shows plots for smile
#
#data : pd.DataFrame - data, must contain unityGameTime, leftSmileValue and rightSmileValue
def show_smile_plot(data : pd.DataFrame):
    show_plot(data['unityGameTime'], data['leftSmileValue'], "Uniesienie lewego koncika ust", "Czas [s]",
              "Uniesienie lewego koncika ust [%]")
    show_plot(data['unityGameTime'], data['rightSmileValue'], 'Uniesienie prawego koncika ust', "Czas [s]",
              "Uniesienie prawego koncika ust [%]")

#Function which shows plots for dimpler (retraction of the corner of the mouth)
#
#data : pd.DataFrame - data, must contain unityGameTime, leftDimplerValue and rightDimplerValue
def show_dimpler_plot(data : pd.DataFrame):
    show_plot(data['unityGameTime'], data['leftDimplerValue'], "Cofnięcie lewego koncika ust", "Czas [s]",
              "Cofnięcie lewego koncika ust [%]")
    show_plot(data['unityGameTime'], data['rightDimplerValue'], 'Cofnięcie prawego koncika ust', "Czas [s]",
              "Cofnięcie prawego koncika ust [%]")

#Function which shows plots for inner brow rise
#
#data : pd.DataFrame - data, must contain unityGameTime, leftInnerBrowRiseValue and rightInnerBrowRiseValue
def show_inner_brow_rise_plot(data : pd.DataFrame):
    show_plot(data['unityGameTime'], data['leftInnerBrowRiseValue'], "Uniesienie środkowej częsci lewej brwi", "Czas [s]",
              "Uniesienie środkowej częsci lewej brwi [%]")
    show_plot(data['unityGameTime'], data['rightInnerBrowRiseValue'], 'Uniesienie środkowej częsci prawej brwi', "Czas [s]",
              "Uniesienie środkowej częsci prawej brwi [%]")

#Function which shows plots for lower brow
#
#data : pd.DataFrame - data, must contain unityGameTime, leftBrowLowerValue and rightBrowLowerValue
def show_lower_brow_plot(data : pd.DataFrame):
    show_plot(data['unityGameTime'], data['leftBrowLowerValue'], "Zniżenie wewnętrznej częsci lewej brwi", "Czas [s]",
              "Zniżenie wewnętrznej częsci lewej brwi [%]")
    show_plot(data['unityGameTime'], data['rightBrowLowerValue'], 'Zniżenie wewnętrznej częsci prawej brwi', "Czas [s]",
              "Zniżenie wewnętrznej częsci prawej brwi [%]")

#Function which shows plots for squint eyes
#
#data : pd.DataFrame - data, must contain unityGameTime, leftLidTightnerValue and rightLidTightnerValue
def show_lid_tightener_plot(data : pd.DataFrame):
    show_plot(data['unityGameTime'], data['leftLidTightnerValue'], "Zmrużenie lewego oka", "Czas [s]",
              "Zmrużenie lewego oka [%]")
    show_plot(data['unityGameTime'], data['rightLidTightnerValue'], 'Zmrużenie prawego oka', "Czas [s]",
              "Zmrużenie prawego oka [%]")

#Function which shows plots for open one's eyes wide
#
#data : pd.DataFrame - data, must contain unityGameTime, leftLidRiserValue and rightLidRiserValue
def show_lid_rise_plot(data : pd.DataFrame):
    show_plot(data['unityGameTime'], data['leftLidRiserValue'], "RozszeRzenie lewego oka", "Czas [s]",
              "Rozszerzenie lewego oka [%]")
    show_plot(data['unityGameTime'], data['rightLidRiserValue'], 'Rozszerzenie prawego oka', "Czas [s]",
              "Rozszerzenie prawego oka [%]")

#Function which shows plots for jaw drop
#
#data : pd.DataFrame - data, must contain unityGameTime and jawDropValue
def show_jaw_drop_plot(data : pd.DataFrame):
    show_plot(data['unityGameTime'], data['jawDropValue'], "Opuszczenie szczęki", "Czas [s]",
              "Opuszczenie szczęki [%]")

#Function which shows plots for eyes rotation
#
#data : pd.DataFrame - data, must contain unityGameTime, leftEyeUpValue, rightEyeUpValue, leftEyeDownValue, rightEyeDownValue,
#leftEyeRightValue, rightEyeRightValue, leftEyeLeftValue and rightEyeLeftValue
def show_eyes_rotation_plot(data : pd.DataFrame):
    show_plot(data['unityGameTime'], data['leftEyeUpValue'], "Lewe oko patrzące w góre", "Czas [s]",
              "Lewe oko patrzące w góre [%]")
    show_plot(data['unityGameTime'], data['rightEyeUpValue'], 'Prawe oko patrzące w góre', "Czas [s]",
              "Prawe oko patrzące w góre [%]")
    show_plot(data['unityGameTime'], data['leftEyeDownValue'], "Lewe oko patrzące w dół", "Czas [s]",
              "Lewe oko patrzące w dół [%]")
    show_plot(data['unityGameTime'], data['rightEyeDownValue'], 'Prawe oko patrzące w dół', "Czas [s]",
              "Prawe oko patrzące w dół [%]")
    show_plot(data['unityGameTime'], data['leftEyeRightValue'], "Lewe oko patrzące w prawo", "Czas [s]",
              "Lewe oko patrzące w prawo [%]")
    show_plot(data['unityGameTime'], data['rightEyeRightValue'], 'Prawe oko patrzące w prawo', "Czas [s]",
              "Prawe oko patrzące w prawo [%]")
    show_plot(data['unityGameTime'], data['leftEyeLeftValue'], "Lewe oko patrzące w lewo", "Czas [s]",
              "Lewe oko patrzące w lewo [%]")
    show_plot(data['unityGameTime'], data['rightEyeLeftValue'], 'Prawe oko patrzące w lewo', "Czas [s]",
              "Prawe oko patrzące w lewo [%]")

#Function which shows correlation matrix
#
#data : pd.DataFrame - data
def show_correlation_matrix(data : pd.DataFrame):
    plt.figure(figsize=(24, 20))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Macierz korelacji")
    plt.show()

#Function which create directory in current directory, if directory not already exist
#
#directory_name : str - name of directory
def create_directory(directory_name : str):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

#Function which saves plot from data
#
#time_col - column with time value (x-axis)
#value_col - column with data (y-axis)
#title - title for plot, default None
#xaxis_label - name for x-axis, default None
#yaxis_label - name for y-axis, default None
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_plot_as_image(time_col, value_col, title=None, xaxis_label=None, yaxis_label=None, filename : str = None, directory_name : str = ""):
    if filename is None:
        raise TypeError("filename cannot be empty!")

    plt.figure(figsize=(10, 5))
    plt.plot(time_col, value_col, linestyle='-', color='b')

    plt.xticks(np.linspace(time_col.min(), time_col.max(), 10))
    plt.yticks(np.linspace(value_col.min(), value_col.max(), 10))

    plt.xlabel(xaxis_label)
    plt.ylabel(yaxis_label)
    plt.title(title if title else f'{yaxis_label} over {xaxis_label}')
    plt.grid(True)
    plt.tight_layout()
    full_path = os.path.join(directory_name, f"{filename}.png")
    plt.savefig(full_path)
    plt.close()

#Function which saves plots for chicks rise
#
#data : pd.DataFrame - data, must contain unityGameTime, leftEyeClosedValue and rightEyeClosedValue
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_eye_closed_plots(data : pd.DataFrame, directory_name : str = ""):
    save_plot_as_image(data['unityGameTime'], data['leftEyeClosedValue'], "Zamknięcie lewego oka", "Czas [s]",
              "Zamknięcie lewego oka [%]", "left_eye_closed", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightEyeClosedValue'], 'Zamknięcie prawego oka', "Czas [s]",
              "Zamknięcie prawego oka [%]", "right_eye_closed", directory_name)

#Function which saves plots for chicks rise
#
#data : pd.DataFrame - data, must contain unityGameTime, leftCheekRiseValue and rightCheekRiseValue
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_chicks_risen_plot(data : pd.DataFrame, directory_name : str = ""):
    save_plot_as_image(data['unityGameTime'], data['leftCheekRiseValue'], "Uniesienie lewego polika", "Czas [s]",
              "Uniesienie lewego polika [%]","left_cheek_rise", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightCheekRiseValue'], 'Uniesienie prawego polika', "Czas [s]",
              "Uniesienie prawego polika [%]", "right_cheek_rise", directory_name)

#Function which saves plots for smile
#
#data : pd.DataFrame - data, must contain unityGameTime, leftSmileValue and rightSmileValue
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_smile_plot(data : pd.DataFrame, directory_name : str = ""):
    save_plot_as_image(data['unityGameTime'], data['leftSmileValue'], "Uniesienie lewego koncika ust", "Czas [s]",
              "Uniesienie lewego koncika ust [%]", "left_smile", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightSmileValue'], 'Uniesienie prawego koncika ust', "Czas [s]",
              "Uniesienie prawego koncika ust [%]", "right_smile", directory_name)

#Function which saves plots for dimpler (retraction of the corner of the mouth)
#
#data : pd.DataFrame - data, must contain unityGameTime, leftDimplerValue and rightDimplerValue
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_dimpler_plot(data : pd.DataFrame, directory_name : str = ""):
    save_plot_as_image(data['unityGameTime'], data['leftDimplerValue'], "Cofnięcie lewego koncika ust", "Czas [s]",
              "Cofnięcie lewego koncika ust [%]","left_dimpler", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightDimplerValue'], 'Cofnięcie prawego koncika ust', "Czas [s]",
              "Cofnięcie prawego koncika ust [%]", "right_dimpler", directory_name)

#Function which saves plots for inner brow rise
#
#data : pd.DataFrame - data, must contain unityGameTime, leftInnerBrowRiseValue and rightInnerBrowRiseValue
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_inner_brow_rise_plot(data : pd.DataFrame, directory_name : str = ""):
    save_plot_as_image(data['unityGameTime'], data['leftInnerBrowRiseValue'], "Uniesienie środkowej częsci lewej brwi", "Czas [s]",
              "Uniesienie środkowej częsci lewej brwi [%]", "right_inner_brow_rise", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightInnerBrowRiseValue'], 'Uniesienie środkowej częsci prawej brwi', "Czas [s]",
              "Uniesienie środkowej częsci prawej brwi [%]", "left_inner_brow_rise", directory_name)

#Function which saves plots for lower brow
#
#data : pd.DataFrame - data, must contain unityGameTime, leftBrowLowerValue and rightBrowLowerValue
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_lower_brow_plot(data : pd.DataFrame, directory_name : str = ""):
    save_plot_as_image(data['unityGameTime'], data['leftBrowLowerValue'], "Zniżenie wewnętrznej częsci lewej brwi", "Czas [s]",
              "Zniżenie wewnętrznej częsci lewej brwi [%]", "left_brow_lower_rise", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightBrowLowerValue'], 'Zniżenie wewnętrznej częsci prawej brwi', "Czas [s]",
              "Zniżenie wewnętrznej częsci prawej brwi [%]", "right_brow_lower_rise", directory_name)

#Function which saves plots for squint eyes
#
#data : pd.DataFrame - data, must contain unityGameTime, leftLidTightnerValue and rightLidTightnerValue
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_lid_tightener_plot(data : pd.DataFrame, directory_name : str = ""):
    save_plot_as_image(data['unityGameTime'], data['leftLidTightnerValue'], "Zmrużenie lewego oka", "Czas [s]",
              "Zmrużenie lewego oka [%]", "left_lid_tightner", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightLidTightnerValue'], 'Zmrużenie prawego oka', "Czas [s]",
              "Zmrużenie prawego oka [%]", "right_lid_tightner", directory_name)

#Function which saves plots for open one's eyes wide
#
#data : pd.DataFrame - data, must contain unityGameTime, leftLidRiserValue and rightLidRiserValue
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_lid_rise_plot(data : pd.DataFrame, directory_name : str = ""):
    save_plot_as_image(data['unityGameTime'], data['leftLidRiserValue'], "Rozszerzenie lewego oka", "Czas [s]",
              "Rozszerzenie lewego oka [%]", "left_lid_riser", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightLidRiserValue'], 'Rozszerzenie prawego oka', "Czas [s]",
              "Rozszerzenie prawego oka [%]", "right_lid_riser", directory_name)

#Function which saves plots for jaw drop
#
#data : pd.DataFrame - data, must contain unityGameTime and jawDropValue
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_jaw_drop_plot(data : pd.DataFrame, directory_name : str = ""):
    save_plot_as_image(data['unityGameTime'], data['jawDropValue'], "Opuszczenie szczęki", "Czas [s]",
              "Opuszczenie szczęki [%]", "jaw_drop", directory_name)

#Function which saves plots for eyes rotation
#
#data : pd.DataFrame - data, must contain unityGameTime, leftEyeUpValue, rightEyeUpValue, leftEyeDownValue, rightEyeDownValue,
#leftEyeRightValue, rightEyeRightValue, leftEyeLeftValue and rightEyeLeftValue
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_eyes_rotation_plot(data : pd.DataFrame, directory_name : str = ""):
    save_plot_as_image(data['unityGameTime'], data['leftEyeUpValue'], "Lewe oko patrzące w góre", "Czas [s]",
              "Lewe oko patrzące w góre [%]", "left_eye_up", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightEyeUpValue'], 'Prawe oko patrzące w góre', "Czas [s]",
              "Prawe oko patrzące w góre [%]", "right_eye_up", directory_name)
    save_plot_as_image(data['unityGameTime'], data['leftEyeDownValue'], "Lewe oko patrzące w dół", "Czas [s]",
              "Lewe oko patrzące w dół [%]", "left_eye_down", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightEyeDownValue'], 'Prawe oko patrzące w dół', "Czas [s]",
              "Prawe oko patrzące w dół [%]", "right_eye_down", directory_name)
    save_plot_as_image(data['unityGameTime'], data['leftEyeRightValue'], "Lewe oko patrzące w prawo", "Czas [s]",
              "Lewe oko patrzące w prawo [%]", "left_eye_right", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightEyeRightValue'], 'Prawe oko patrzące w prawo', "Czas [s]",
              "Prawe oko patrzące w prawo [%]", "right_eye_right", directory_name)
    save_plot_as_image(data['unityGameTime'], data['leftEyeLeftValue'], "Lewe oko patrzące w lewo", "Czas [s]",
              "Lewe oko patrzące w lewo [%]", "left_eye_left", directory_name)
    save_plot_as_image(data['unityGameTime'], data['rightEyeLeftValue'], 'Prawe oko patrzące w lewo', "Czas [s]",
              "Prawe oko patrzące w lewo [%]", "right_eye_left", directory_name)

#Function which saves all plots
#
#data : pd.DataFrame - data
#directory_name : str - name of directory where plots will be saved, default is empty (active directory)
def save_all_plots(data : pd.DataFrame, directory_name : str = ""):
    create_directory(directory_name)
    save_eye_closed_plots(data, directory_name)
    save_chicks_risen_plot(data, directory_name)
    save_smile_plot(data, directory_name)
    save_dimpler_plot(data, directory_name)
    save_inner_brow_rise_plot(data, directory_name)
    save_lower_brow_plot(data, directory_name)
    save_lid_tightener_plot(data, directory_name)
    save_lid_rise_plot(data, directory_name)
    save_jaw_drop_plot(data, directory_name)
    save_eyes_rotation_plot(data, directory_name)