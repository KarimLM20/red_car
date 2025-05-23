import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate


    # Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {
    'usernames': {
        'voiture': {
            'name': 'Inspecteur_Nahnah',
            'password': 'rouge',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()


def accueil():
    st.markdown(f"<h1 style='color:#D2042D;'>{nom_affiche}, bienvenue sur le site de la <em>Voiture Rouge</em> 🚗</h1>", unsafe_allow_html=True)
def photos():
    st.markdown(f"<h1 style='color:#D2042D;'>{nom_affiche}, voici la fameuse voiture rouge <em>Voiture Rouge</em> 🚗</h1>", unsafe_allow_html=True)

if st.session_state["authentication_status"]:
    
    with st.sidebar:
        nom_affiche = lesDonneesDesComptes["usernames"][st.session_state["username"]]["name"]
        st.write(f"Bienvenue {nom_affiche}")
        # Création du menu qui va afficher les choix qui se trouvent dans la variable options
        selection = option_menu(
            menu_title=None,
            options = ["🥸 Accueil", "🚗 Photos de la voiture rouge", "🎶 En chanson", "🤣 Multichouf"]
        )
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")


    # On indique au programme quoi faire en fonction du choix
    if selection == "🥸 Accueil":
        accueil()
        st.image("https://photos.tf1.fr/1920/1080/cover-showpage-hallalpolic-365400-ae8c69-0@3x.jpg")
    elif selection == "🚗 Photos de la voiture rouge":
        photos()
            # Création de 3 colonnes 
        col1, col2, col3 = st.columns(3)

        # Contenu de la première colonne : 
        with col1:
            st.header("Avec les collègues")
            st.image("https://www.imcdb.org/i409822.jpg")

        # Contenu de la deuxième colonne :
        with col2:
            st.header("Sur la scène de crime")
            st.image("https://pics.imcdb.org/0is834/hpde012014c14.6161.jpg")

        # Contenu de la troisième colonne : 
        with col3:
            st.header("À l'aéroport")
            st.image("https://focus.telerama.fr/2022/07/18/235/158/1725/1150/1200/0/60/0/29e24fd_1658132929444-11-halalpolicedetat201111j.jpg")
        # ... et ainsi de suite pour les autres pages
    elif selection == "🎶 En chanson":
        st.markdown(f"<h1 style='color:#D2042D;'>{nom_affiche}, chantons !", unsafe_allow_html=True)
        st.video('https://www.youtube.com/watch?v=e2OIv14ov68')
    elif selection == "🤣 Multichouf":
        st.video('https://www.youtube.com/watch?v=I6KK1GYVE9U')

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')