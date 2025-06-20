import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Projet IA - Data Center",
    page_icon="assets/green_computing_icon.png",  # ✅ Ajoute ici le chemin
    layout="wide"
)





# Fonction pour charger une page HTML externe
def load_html_page(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    st.markdown(html, unsafe_allow_html=True)

# Menu de navigation
menu = st.sidebar.radio("📚 Menu", [
    "🏠 Page d'accueil",
    "🔍 Introduction & Problématique",
    "🎯 Objectifs",
    "🧪 Méthodologie",
    "📊 Résultats",
    "🤖 Prédiction IA",
    "🧩 Conclusion"
])

# Routage vers les fichiers HTML ou blocs dynamiques
if menu == "🏠 Page d'accueil":
    load_html_page("html/accueil.html")

elif menu == "🔍 Introduction & Problématique":
    load_html_page("html/introduction.html")

elif menu == "🎯 Objectifs":
    load_html_page("html/objectifs.html")

elif menu == "🧪 Méthodologie":
    load_html_page("html/methode.html")

elif menu == "📊 Résultats":
    load_html_page("html/resultats.html")

elif menu == "🧩 Conclusion":
    load_html_page("html/conclusion.html")

elif menu == "🤖 Prédiction IA":
    st.header("🤖 Prédiction de la Consommation Énergétique")

    n_vms = st.slider("Nombre de VMs actives", 0, 150, 30)
    cpu_used = st.slider("CPU utilisée (GHz)", 0.0, 64.0, 20.0)
    ram_used = st.slider("RAM utilisée (Go)", 0.0, 256.0, 80.0)
    cpu_capacity = st.selectbox("Capacité totale CPU", [32, 64])
    ram_capacity = st.selectbox("Capacité totale RAM", [128, 256])

    # Charger modèle ML
    model = joblib.load("ml/model.pkl")
    input_data = np.array([[n_vms, cpu_used, ram_used, cpu_capacity, ram_capacity]])
    predicted_power = model.predict(input_data)[0]

    st.metric(label="Consommation énergétique estimée (Watts)", value=f"{predicted_power:.2f}")
