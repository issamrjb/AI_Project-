import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Charger les données
df = pd.read_csv("data/hosts_dataset.csv")

# Features et cible
features = ["n_vms", "cpu_used", "ram_used", "cpu_capacity", "ram_capacity"]
target = "power_consumed"

X = df[features]
y = df[target]

# Split en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modèle de régression
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Évaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"✅ Modèle entraîné avec succès !")
print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.3f}")

# Sauvegarde du modèle
joblib.dump(model, "ml/model.pkl")
