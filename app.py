"""
Adding cartwheeling (🤸‍♀️) emojis between spaces
"""
# Importing local display module
import display as dp

# Importing pyperclip clipboard module
import pyperclip as clip

# Importing streamlit third-party App Framework
import streamlit as st


# Setting page Title and Icon
st.set_page_config(page_title="Beshy App", page_icon="🤸‍♀️")


def add_emoji(txt: str) -> str:
    """
    Adds a cartwheel emoji between spaces
    """
    # Adding text output
    txt =  txt.replace(" ", " 🤸‍♀️ ")

    # Returning modified text
    return txt


def main():
    """
    Contains the main app
    """
    # Adding title
    st.title("🤸‍♀️🤸‍♀️🤸‍♀️")

    # Adding text input
    text_input = st.text_area(label=" ",placeholder="Bakit tinatamad mag-type ang beshy ko?")

    # Replaces spaces with emojis
    txt = add_emoji(text_input)

    # If input is not empty and spaces are present
    if " " in text_input:
        # Display text modified block
        dp.display_text(txt)

        # Copy to clipboard button
        if st.button("Copy"):
            clip.copy(txt)


# Running the main function
if __name__ == "__main__":
    main()
