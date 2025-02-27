"""
Robot Display Module voor Stan de GitHub Agent.

Deze module verzorgt de weergave van de robot in de Streamlit applicatie
en bevat functies voor het tonen en stylen van de robot afbeelding.
"""

import os
import streamlit as st
from constants import ROBOT_IMAGE_PATH, PRIMARY_COLOR


def display_robot():
    """
    Toont de robot afbeelding in de Streamlit app.
    
    Laadt de robot afbeelding uit het gespecificeerde pad in constants.py
    en geeft deze weer in het midden van de app met een hover-effect.
    
    Returns:
        bool: True als de robot succesvol is weergegeven, anders False
    """
    try:
        # Controleer of het bestand bestaat
        if not os.path.exists(ROBOT_IMAGE_PATH):
            st.error(f"Robot afbeelding niet gevonden op pad: {ROBOT_IMAGE_PATH}")
            return False
        
        # CSS voor hover-effect
        hover_css = f"""
        <style>
            .robot-container {{
                display: flex;
                justify-content: center;
                margin: 20px auto;
                width: 300px;
                transition: transform 0.3s ease;
            }}
            .robot-container:hover {{
                transform: scale(1.05);
                cursor: pointer;
            }}
            .robot-container img {{
                max-width: 100%;
                border-radius: 10px;
            }}
        </style>
        """
        st.markdown(hover_css, unsafe_allow_html=True)
        
        # Container voor centreren en opmaak
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            # Toon de robot afbeelding in HTML om hover-effect mogelijk te maken
            st.markdown(
                f"""
                <div class="robot-container">
                    <img src="{ROBOT_IMAGE_PATH}" alt="GitHub Agent Robot">
                </div>
                """, 
                unsafe_allow_html=True
            )
        
        return True
        
    except Exception as e:
        st.error(f"Fout bij het weergeven van de robot: {str(e)}")
        return False


def get_robot_html(width=300):
    """
    Genereert HTML voor de robot afbeelding met aangepaste breedte.
    
    Args:
        width (int): Breedte van de robot afbeelding in pixels
        
    Returns:
        str: HTML code voor het weergeven van de robot
    """
    return f"""
    <div class="robot-container" style="width: {width}px;">
        <img src="{ROBOT_IMAGE_PATH}" alt="GitHub Agent Robot">
    </div>
    """


# Voor standalone test
if __name__ == "__main__":
    st.title("Robot Display Test")
    st.write("Dit is een test voor de robot_display module.")
    
    if display_robot():
        st.success("Robot succesvol weergegeven!")
    else:
        st.error("Er was een probleem bij het weergeven van de robot.")
