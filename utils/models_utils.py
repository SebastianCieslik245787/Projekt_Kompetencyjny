import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
from sklearn.svm import SVC


def train_RF(data: pd.DataFrame, labels: pd.DataFrame, label_encoder: LabelEncoder):
    labels_encoded = label_encoder.fit_transform(labels)

    model : RandomForestClassifier = RandomForestClassifier(n_estimators=100, random_state=42)

    model.fit(data, labels_encoded)

    return model

def train_KNN(data: pd.DataFrame, labels: pd.DataFrame, label_encoder: LabelEncoder, scaler: StandardScaler):
    labels_encoded = label_encoder.fit_transform(labels)

    data_scaled = scaler.fit_transform(data)
    model : KNeighborsClassifier = KNeighborsClassifier(
        n_neighbors=7,
        weights='distance',
        metric='minkowski',
        p=2
    )
    model.fit(data_scaled, labels_encoded)

    return model

def train_SVC(data: pd.DataFrame, labels: pd.DataFrame, label_encoder: LabelEncoder):
    labels_encoded = label_encoder.fit_transform(labels)

    model : SVC = SVC(kernel='rbf', C=10, gamma=0.1, probability=True)
    model.fit(data, labels_encoded)

    return model

def train_NN(data: pd.DataFrame, labels: pd.DataFrame, label_encoder: LabelEncoder, scaler: StandardScaler):
    labels_encoded = label_encoder.fit_transform(labels)

    data_scaled = scaler.fit_transform(data)
    model : MLPClassifier = MLPClassifier(
        hidden_layer_sizes=(100, 50),
        activation='relu',
        solver='adam',
        alpha=1e-4,
        batch_size=64,
        learning_rate='adaptive',
        learning_rate_init=0.001,
        max_iter=300,
        early_stopping=True,
        validation_fraction=0.1,
        random_state=42,
        verbose=True
    )
    model.fit(data_scaled, labels_encoded)

    return model

def save_model(model, model_name: str = "model"):
    joblib.dump(model, f"../model/{model_name}.joblib")

def save_scaler(scaler: StandardScaler):
    joblib.dump(scaler, f"../model/scaler.joblib")

def save_label_encoder(label_encoder : LabelEncoder):
    joblib.dump(label_encoder, f"../model/label_encoder.joblib")

def load_model(model_name: str):
    return joblib.load(f'../model/{model_name}.joblib')

def load_scaler():
    return joblib.load(f'../model/scaler.joblib')

def load_label_encoder():
    return joblib.load(f'../model/label_encoder.joblib')

def show_accuracy(true_labels, predicted_labels, label_encoder, model_name: str):
    accuracy = accuracy_score(true_labels, predicted_labels)
    print(f"\nDokładność modelu {model_name}: {accuracy:.4f}\n")

    print(">>> Raport klasyfikacji:\n")
    print(classification_report(
        true_labels,
        predicted_labels,
        target_names=label_encoder.classes_
    ))

    labels_present = np.unique(np.concatenate([true_labels, predicted_labels]))

    fig, ax = plt.subplots(figsize=(5, 5))
    ConfusionMatrixDisplay.from_predictions(
        true_labels,
        predicted_labels,
        labels=labels_present,
        display_labels=[label_encoder.classes_[i] for i in labels_present],
        ax=ax,
        xticks_rotation='vertical'
    )

    plt.title(f'Macierz Pomyłek Modelu {model_name}')
    plt.tight_layout()
    plt.show()