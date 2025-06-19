import streamlit as st

# Configuration générale de la page
st.set_page_config(
    page_title="Projet IA - Data Center",
    page_icon="💡",
    layout="wide"
)

# Menu de navigation dans la barre latérale
menu = st.sidebar.radio("📚 Menu", [
    "🏠 Page d'accueil",
    "🔍 Introduction & Problématique",
    "🎯 Objectifs",
    "🧪 Méthodologie",
    "📊 Résultats",
    "🧩 Conclusion"
])

# Fonctions de contenu
def accueil():
    st.title("💡 Projet IA : Optimisation Énergétique des Data Centers")
    st.write("""
        Bienvenue sur ce site de présentation du projet d'intelligence artificielle appliqué à la prédiction
        du facteur d'efficacité énergétique (PUE) dans les centres de données.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Server_room.jpg/640px-Server_room.jpg", use_column_width=True)

def introduction():
    st.header("🔍 Introduction & Problématique")
    st.write("""
        Les centres de données consomment une quantité massive d’énergie. Cette surconsommation engendre
        des coûts financiers et un impact environnemental préoccupant. Le PUE (Power Usage Effectiveness) est
        l’un des indicateurs clés de performance énergétique.
        
        Ce projet vise à intégrer des techniques d’intelligence artificielle pour prédire ce facteur et
        contribuer à une gestion énergétique plus intelligente.
    """)

def objectifs():
    st.header("🎯 Objectifs du projet")
    st.markdown("""
    - Simuler des données réalistes pour un data center.
    - Créer une interface simple de démonstration.
    - Intégrer un modèle IA de prédiction du PUE.
    - Fournir une visualisation claire des résultats.
    - Préparer un site de présentation scientifique hébergé gratuitement.
    """)

def methode():
    st.header("🧪 Méthodologie prévue")
    st.markdown("""
    **Étapes prévues :**
    1. Génération de données simulées
    2. Nettoyage et préparation des données
    3. Entraînement d’un modèle de régression (ML/DL)
    4. Évaluation et optimisation
    5. Intégration dans l’app Streamlit
    """)

def resultats():
    st.header("📊 Résultats (Simulation)")
    st.write("Voici une prédiction simulée du PUE :")
    pue = 1.25
    st.metric("PUE prédictif (simulé)", f"{pue}")

def conclusion():
    st.header("🧩 Conclusion")
    st.write("""
        Ce prototype démontre les bases de la prédiction du PUE à l’aide de l’IA.
        La prochaine étape consistera à intégrer des données réelles, entraîner un modèle
        et mesurer les performances.

        Le projet montre comment IA et green computing peuvent se compléter pour créer
        des infrastructures numériques plus durables.
    """)
    st.download_button("📄 Télécharger le rapport (PDF)", data="Rapport à venir...", file_name="rapport_PUE.pdf")

# Affichage basé sur le menu sélectionné
if menu == "🏠 Page d'accueil":
    accueil()
elif menu == "🔍 Introduction & Problématique":
    introduction()
elif menu == "🎯 Objectifs":
    objectifs()
elif menu == "🧪 Méthodologie":
    methode()
elif menu == "📊 Résultats":
    resultats()
elif menu == "🧩 Conclusion":
    conclusion()
