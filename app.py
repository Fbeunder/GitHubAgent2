"""
Stan de GitHub Agent - Hoofdapplicatie

Deze module vormt de hoofdapplicatie die alle andere modules samenvoegt tot een
werkende Streamlit applicatie die gebruikers in staat stelt om de robot te bekijken,
erop te klikken en grappige uitspraken te zien.
"""

import streamlit as st
import robot_display
import quote_generator
import styles
from constants import APP_TITLE, APP_DESCRIPTION


def setup_page_config():
    """
    Configureert de Streamlit pagina-instellingen.
    
    Stelt de pagina titel, favicon en layout in.
    """
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="collapsed"
    )


def initialize_session():
    """
    Initialiseert de sessie-state variabelen voor de applicatie.
    
    Zorgt ervoor dat alle benodigde sessie-variabelen bestaan en juist zijn ingesteld.
    """
    # Initialiseer quote generator sessie-state
    quote_generator.initialize_session_state()
    
    # Initialiseer click counter als die nog niet bestaat
    if 'click_count' not in st.session_state:
        st.session_state.click_count = 0
    
    # Initialiseer huidige quote als die nog niet bestaat
    if 'current_quote' not in st.session_state:
        st.session_state.current_quote = "Klik op de robot om een grappige uitspraak te zien!"


def handle_robot_click():
    """
    Afhandeling van een klik op de robot.
    
    Genereert een nieuwe uitspraak en verhoogt de click counter.
    """
    st.session_state.click_count += 1
    st.session_state.current_quote = quote_generator.get_next_quote_with_state()
    
    # Forceer een refresh van de pagina om de nieuwe uitspraak te tonen
    st.rerun()


def display_header():
    """
    Toont de header sectie van de applicatie.
    
    Bevat de titel, beschrijving en eventuele introductietekst.
    """
    st.title(APP_TITLE)
    st.markdown(APP_DESCRIPTION)
    
    # Voeg extra instructies toe
    st.write("👇 **Klik op de robot hieronder om grappige uitspraken te zien!** 👇")


def display_quote_section():
    """
    Toont de sectie met de huidige uitspraak.
    
    Als er nog geen uitspraak is, toont een instructie-bericht.
    """
    # Gebruik de HTML generator uit styles.py voor mooiere quotes
    quote_html = styles.create_quote_html(
        st.session_state.current_quote,
        is_new=(st.session_state.click_count > 0)
    )
    st.markdown(quote_html, unsafe_allow_html=True)
    
    # Toon een subtiele indicator voor het aantal clicks
    if st.session_state.click_count > 0:
        st.caption(f"Je hebt de robot {st.session_state.click_count} keer geklikt")


def display_robot_section():
    """
    Toont de robot sectie inclusief klikbare robot afbeelding.
    
    De klikbaarheid van de robot is nu geïmplementeerd in de robot_display module.
    Voor toegankelijkheid is er ook nog een extra knop beschikbaar.
    """
    # Container voor robot weergave
    robot_container = st.container()
    
    with robot_container:
        # Gebruik de robot_display module om de robot weer te geven
        # De robot is nu direct klikbaar en verwerkt kliks intern
        success = robot_display.display_robot()
        
        if not success:
            st.info("Zorg ervoor dat de assets directory bestaat met een robot.svg bestand.")
            return
        
        # Een zichtbare button onder de robot voor alternatieve klikinteractie
        # (Voor toegankelijkheidsdoeleinden)
        if st.button("Klik op de Robot", key="robot_button", help="Alternatieve knop voor een nieuwe uitspraak"):
            handle_robot_click()


def add_extra_features():
    """
    Voegt extra features toe aan de applicatie.
    
    Inclusief een reset knop en information footer.
    """
    # Voeg een horizontale lijn toe voor visuele scheiding
    st.markdown("---")
    
    # Maak twee kolommen voor reset knop en credits
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Reset knop om alle uitspraken opnieuw te beginnen
        if st.button("Reset", help="Begin opnieuw met de uitspraken"):
            st.session_state.click_count = 0
            st.session_state.quote_index = None
            st.session_state.current_quote = "Klik op de robot om een grappige uitspraak te zien!"
            st.rerun()
    
    with col2:
        # Voeg een footer met credits toe
        st.caption("Stan de GitHub Agent | Ontwikkeld met ❤️ en Python")
        st.caption("© 2025 | Alle grappen met een korreltje zout nemen 🧂")


def main():
    """
    Hoofdfunctie die de Streamlit applicatie initialiseert en draait.
    
    Deze functie coördineert alle componenten van de applicatie.
    """
    try:
        # Setup pagina configuratie
        setup_page_config()
        
        # Initialiseer de sessie-state
        initialize_session()
        
        # Pas de stijlen toe
        styles.apply_styles()
        
        # Toon de header
        display_header()
        
        # Toon de huidige uitspraak sectie
        display_quote_section()
        
        # Toon de robot sectie
        display_robot_section()
        
        # Voeg extra features toe
        add_extra_features()
        
    except Exception as e:
        st.error(f"Er is een fout opgetreden: {str(e)}")
        st.info("Probeer de pagina te vernieuwen of neem contact op met de ontwikkelaar.")


# Entry point voor de applicatie
if __name__ == "__main__":
    main()
