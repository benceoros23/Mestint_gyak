import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# 1. CSV beolvasása
df = pd.read_csv('Iris.csv')

# Ha van Id oszlop, töröljük
if 'Id' in df.columns:
    df = df.drop('Id', axis=1)

# 2. Adatok szétválasztása
X = df.iloc[:, :-1]   # jellemzők (minden oszlop kivéve az utolsó)
y = df.iloc[:, -1]    # célváltozó (utolsó oszlop)

# 3. Tanító és teszt adatok
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Modell létrehozása
model = GaussianNB()

# 5. Modell tanítása
model.fit(X_train, y_train)

# 6. Predikció
y_pred = model.predict(X_test)

# 7. Kiértékelés
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 8. Vizualizáció (2 dimenzióban)
plt.figure(figsize=(8,6))

for i, label in enumerate(y.unique()):
    plt.scatter(
        X_test[y_test == label].iloc[:, 0],
        X_test[y_test == label].iloc[:, 1],
        label=label
    )

plt.xlabel(X.columns[0])
plt.ylabel(X.columns[1])
plt.title('Teszt adatok - Valós osztályok')
plt.legend()
plt.grid(True)

plt.show()