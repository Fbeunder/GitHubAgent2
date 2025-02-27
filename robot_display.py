"""
Robot Display Module voor Stan de GitHub Agent.

Deze module verzorgt de weergave van de robot in de Streamlit applicatie
en bevat functies voor het tonen en stylen van de robot afbeelding.
"""

import os
import base64
import streamlit as st
from constants import ROBOT_IMAGE_PATH, PRIMARY_COLOR


def get_base64_encoded_image(image_path):
    """
    Leest een afbeeldingsbestand en retourneert de base64-encoded versie.
    
    Args:
        image_path (str): Pad naar de afbeelding
        
    Returns:
        str: Base64-encoded afbeelding string
    """
    try:
        with open(image_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return encoded
    except Exception as e:
        st.error(f"Fout bij het lezen van afbeelding: {str(e)}")
        return None


def display_robot():
    """
    Toont de robot afbeelding in de Streamlit app.
    
    Laadt de robot afbeelding uit het gespecificeerde pad in constants.py
    en geeft deze weer in het midden van de app met een hover-effect en klikfunctionaliteit.
    
    Returns:
        bool: True als de robot succesvol is weergegeven, anders False
    """
    try:
        # Controleer of het bestand bestaat
        if not os.path.exists(ROBOT_IMAGE_PATH):
            st.error(f"Robot afbeelding niet gevonden op pad: {ROBOT_IMAGE_PATH}")
            return False
        
        # Haal de base64-encoded SVG op
        encoded_image = get_base64_encoded_image(ROBOT_IMAGE_PATH)
        if not encoded_image:
            st.error("Kon de robotafbeelding niet inlezen")
            return False
        
        # Genereer een unieke key voor de sessie
        if 'robot_click_key' not in st.session_state:
            st.session_state.robot_click_key = 0
        
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
            /* Verberg de submit knop */
            .robot-click-form .stButton {{
                display: none;
            }}
        </style>
        """
        st.markdown(hover_css, unsafe_allow_html=True)
        
        # Container voor centreren en opmaak
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            # JavaScript om de form te submitten wanneer op de robot wordt geklikt
            javascript = f"""
            <script>
                document.addEventListener('DOMContentLoaded', function() {{
                    const robotContainer = document.querySelector('.robot-container');
                    const robotForm = document.querySelector('.robot-click-form form');
                    
                    if (robotContainer && robotForm) {{
                        robotContainer.addEventListener('click', function() {{
                            const submitButton = robotForm.querySelector('button[type="submit"]');
                            if (submitButton) {{
                                submitButton.click();
                            }}
                        }});
                    }}
                }});
            </script>
            """
            st.markdown(javascript, unsafe_allow_html=True)
            
            # Toon de robot afbeelding in HTML om hover-effect mogelijk te maken
            # Gebruik data URI voor de afbeelding
            st.markdown(
                f"""
                <div class="robot-container">
                    <img src="data:image/svg+xml;base64,{encoded_image}" alt="GitHub Agent Robot">
                </div>
                """, 
                unsafe_allow_html=True
            )

            # Onzichtbare form die wordt gesubmit wanneer op de robot wordt geklikt
            with st.form(key=f"robot_click_form_{st.session_state.robot_click_key}", clear_on_submit=False):
                st.form_submit_button("Robot Klik", type="primary", use_container_width=True, 
                                     on_click=lambda: st.session_state.update({"robot_was_clicked": True}))
        
        # Check of er geklikt is op de robot sinds laatste render
        if st.session_state.get("robot_was_clicked", False):
            # Reset de robot_was_clicked flag
            st.session_state.robot_was_clicked = False
            
            # Verhoog de robot_click_key voor de volgende keer
            st.session_state.robot_click_key += 1
            
            # Voer de klikactie uit zoals gedefinieerd in app.py
            import quote_generator
            st.session_state.click_count += 1
            st.session_state.current_quote = quote_generator.get_next_quote_with_state()
            st.rerun()
        
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
    # Controleer of het bestand bestaat
    if not os.path.exists(ROBOT_IMAGE_PATH):
        return f"<div>Robot afbeelding niet gevonden op pad: {ROBOT_IMAGE_PATH}</div>"
    
    # Haal de base64-encoded SVG op
    encoded_image = get_base64_encoded_image(ROBOT_IMAGE_PATH)
    if not encoded_image:
        return "<div>Kon de robotafbeelding niet inlezen</div>"
    
    return f"""
    <div class="robot-container" style="width: {width}px;">
        <img src="data:image/svg+xml;base64,{encoded_image}" alt="GitHub Agent Robot">
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
