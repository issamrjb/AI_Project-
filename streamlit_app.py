import streamlit as st

# Fonction simulée de prédiction
def prediction():
    return 1.25  # valeur simulée de PUE

# Interface utilisateur
st.set_page_config(page_title="PUE Predictor", page_icon="💡", layout="centered")

st.title("💡 Prédiction du PUE d'un Data Center")
st.write("Ce prototype utilise une fonction fixe pour simuler une prédiction IA. "
         "Le modèle réel sera intégré prochainement.")

# Affichage de la prédiction
pue = prediction()
st.metric(label="PUE (Power Usage Effectiveness)", value=round(pue, 2))

st.markdown("---")
st.info("Ce projet sera enrichi avec un modèle d'IA complet et des données réelles.")
