"""
Styles Module voor Stan de GitHub Agent.

Deze module is verantwoordelijk voor het definiëren en laden van CSS-stijlen
die de visuele presentatie van de Streamlit applicatie verbeteren.
"""

import streamlit as st
from constants import (
    PRIMARY_COLOR, 
    SECONDARY_COLOR, 
    BACKGROUND_COLOR, 
    TEXT_COLOR
)


def load_styles():
    """
    Laadt CSS-stijlen voor de Streamlit applicatie.
    
    Genereert en retourneert een CSS-string met stijlen die de visuele presentatie
    van de applicatie verbeteren, inclusief headers, containers en quote weergave.
    
    Returns:
        str: CSS-code die in Streamlit kan worden geladen via st.markdown()
    """
    # Basis CSS-stijlen voor de hele applicatie
    css = f"""
    <style>
        /* Algemene pagina styling */
        .reportview-container .main .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 800px;
        }}
        
        /* Achtergrond en tekst kleuren */
        .reportview-container {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }}
        
        /* Header stijlen */
        h1, h2, h3, h4, h5, h6 {{
            color: {PRIMARY_COLOR};
            font-weight: bold;
        }}
        h1 {{
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            text-align: center;
        }}
        h2 {{
            font-size: 1.8rem;
            margin-bottom: 1rem;
        }}
        
        /* Quote container stijlen */
        .quote-container {{
            background-color: white;
            border-left: 5px solid {PRIMARY_COLOR};
            border-radius: 5px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }}
        .quote-container:hover {{
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
            transform: translateY(-2px);
        }}
        
        /* Quote tekst stijlen */
        .quote-text {{
            font-size: 1.2rem;
            line-height: 1.5;
            font-style: italic;
            color: {TEXT_COLOR};
        }}
        
        /* Robot container stijlen (aanvullend op robot_display.py) */
        .robot-container {{
            transition: all 0.3s ease !important;
            cursor: pointer !important;
        }}
        .robot-container:hover {{
            transform: scale(1.05) !important;
        }}
        
        /* Button stijlen */
        .stButton>button {{
            background-color: {PRIMARY_COLOR};
            color: white;
            border: none;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        .stButton>button:hover {{
            background-color: {SECONDARY_COLOR};
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        /* Animatie voor quotes */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .quote-container.new {{
            animation: fadeIn 0.5s ease-out;
        }}
        
        /* Responsieve aanpassingen */
        @media screen and (max-width: 640px) {{
            h1 {{
                font-size: 2rem;
            }}
            .quote-text {{
                font-size: 1rem;
            }}
        }}
    </style>
    """
    return css


def apply_styles():
    """
    Past de CSS-stijlen toe op de huidige Streamlit app.
    
    Deze functie genereert de CSS-stijlen en past ze toe op de app
    via st.markdown() met unsafe_allow_html=True.
    """
    css = load_styles()
    st.markdown(css, unsafe_allow_html=True)


def create_quote_html(quote_text, is_new=True):
    """
    Genereert HTML voor een quote met styling.
    
    Args:
        quote_text (str): De tekst van de quote
        is_new (bool, optional): Of de quote nieuw is (voor animatie). Default is True.
        
    Returns:
        str: HTML-code voor de gestileerde quote
    """
    new_class = "new" if is_new else ""
    return f"""
    <div class="quote-container {new_class}">
        <p class="quote-text">{quote_text}</p>
    </div>
    """


# Voor standalone test
if __name__ == "__main__":
    st.title("Styles Test")
    st.write("Dit is een test voor de styles module.")
    
    # Pas stijlen toe
    apply_styles()
    
    # Toon een voorbeeld quote
    quote = "Als GitHub Agent kan ik commits maken zonder koffie te drinken... Maar het is wel fijner mét."
    st.markdown(create_quote_html(quote), unsafe_allow_html=True)
    
    # Toon een button voor demo
    if st.button("Klik voor een gestijlde button"):
        st.write("De button werkt!")
    
    # Toon informatie over de gebruikte kleuren
    st.write("## Kleurenpalet:")
    st.write(f"Primary Color: {PRIMARY_COLOR}")
    st.write(f"Secondary Color: {SECONDARY_COLOR}")
    st.write(f"Background Color: {BACKGROUND_COLOR}")
    st.write(f"Text Color: {TEXT_COLOR}")
