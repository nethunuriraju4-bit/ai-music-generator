import streamlit as st
from music_generator import generate_music

st.set_page_config(page_title="AI Music Generator", page_icon="🎵")

st.title("🎵 AI Music Generator")
st.write("Generate music using AI")

mood = st.selectbox(
    "Select Mood",
    ["Happy", "Sad", "Energetic", "Relax"]
)

genre = st.selectbox(
    "Select Genre",
    ["Classical", "Rock", "Lo-fi"]
)

instrument = st.selectbox(
    "Select Instrument",
    ["Piano", "Guitar", "Flute", "Drum"]
)

if st.button("Generate Music"):

    st.write("Generating music...")

    music_file = generate_music(mood, genre, instrument)

    st.audio(music_file)

    with open(music_file, "rb") as f:
        st.download_button(
            "Download Music",
            f,
            file_name="ai_music.wav"
        )
