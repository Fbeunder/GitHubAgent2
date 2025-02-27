"""
Quote Generator Module voor Stan de GitHub Agent.

Deze module is verantwoordelijk voor het genereren en beheren van grappige uitspraken
die worden weergegeven wanneer de gebruiker op de robot klikt.
"""

import random
import streamlit as st
from constants import QUOTES


def get_next_quote(current_index=None):
    """
    Haalt de volgende willekeurige uitspraak op uit de lijst met uitspraken.
    
    Zorgt ervoor dat dezelfde uitspraak niet direct wordt herhaald door de huidige
    index uit te sluiten van de willekeurige selectie.
    
    Args:
        current_index (int, optional): De index van de huidige uitspraak.
            Indien None, wordt er geen index uitgesloten.
            
    Returns:
        tuple: (str, int) Een tuple met de volgende uitspraak en de nieuwe index.
    """
    # Aantal beschikbare uitspraken
    num_quotes = len(QUOTES)
    
    # Als er maar 1 uitspraak is, of helemaal geen uitspraken
    if num_quotes <= 1:
        return QUOTES[0] if num_quotes == 1 else "Geen uitspraken beschikbaar", 0
    
    # Genereer een lijst met alle mogelijke indices, behalve de huidige
    possible_indices = list(range(num_quotes))
    if current_index is not None and 0 <= current_index < num_quotes:
        possible_indices.remove(current_index)
    
    # Kies een willekeurige index uit de mogelijke indices
    new_index = random.choice(possible_indices)
    
    # Return de uitspraak en de nieuwe index
    return QUOTES[new_index], new_index


def get_random_quote():
    """
    Haalt een volledig willekeurige uitspraak op uit de lijst met uitspraken.
    
    Deze functie houdt geen rekening met eerder gekozen uitspraken en kan dezelfde
    uitspraak meerdere keren achter elkaar kiezen.
    
    Returns:
        str: Een willekeurige uitspraak.
    """
    num_quotes = len(QUOTES)
    if num_quotes == 0:
        return "Geen uitspraken beschikbaar"
    
    random_index = random.randint(0, num_quotes - 1)
    return QUOTES[random_index]


def initialize_session_state():
    """
    Initialiseert de Streamlit sessie-state voor het bijhouden van de huidige quote index.
    
    Deze functie moet worden aangeroepen aan het begin van de Streamlit app.
    """
    if 'quote_index' not in st.session_state:
        st.session_state.quote_index = None


def get_next_quote_with_state():
    """
    Haalt de volgende uitspraak op en update de sessie-state.
    
    Deze functie is specifiek voor gebruik in een Streamlit-applicatie en maakt gebruik
    van Streamlit's sessie-state mechanisme om de huidige index bij te houden.
    
    Returns:
        str: De volgende uitspraak.
    """
    # Initialiseer sessie-state indien nodig
    initialize_session_state()
    
    # Haal de volgende uitspraak op
    quote, new_index = get_next_quote(st.session_state.quote_index)
    
    # Update de sessie-state
    st.session_state.quote_index = new_index
    
    return quote


# Voor standalone tests
if __name__ == "__main__":
    print("Quote Generator Test\n")
    print("Test 1: Verschillende uitspraken testen (zou geen directe herhalingen moeten bevatten)")
    
    current = None
    history = []
    
    for i in range(10):
        quote, current = get_next_quote(current)
        print(f"Quote {i+1}: {quote}")
        print(f"Index: {current}")
        history.append(current)
    
    print("\nTest 2: Controleren of alle uitspraken worden gebruikt")
    all_indices = set(range(len(QUOTES)))
    used_indices = set(history)
    missing_indices = all_indices - used_indices
    
    if missing_indices and len(history) >= len(QUOTES):
        print(f"Waarschuwing: Niet alle uitspraken werden gebruikt. Ontbrekende indices: {missing_indices}")
    else:
        print("Alle uitspraken werden gebruikt of er waren niet genoeg iteraties om alle uitspraken te gebruiken.")
    
    print("\nTest 3: Volledig willekeurige uitspraken")
    for i in range(5):
        quote = get_random_quote()
        print(f"Random quote {i+1}: {quote}")
