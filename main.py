import streamlit as st
from utils import workflow

def main():
    yt_url = st.text_input("Insert your Youtube URL here")
    generate_ideas = st.button("Generate Short Form Content Ideas")

    if generate_ideas:
        ideas = workflow.generate_short_form_ideas(yt_url)
        st.write('Here are some ideas for you:')
        st.write(ideas)


if __name__ == '__main__':
    main()