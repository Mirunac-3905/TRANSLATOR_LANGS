import streamlit as st
from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr

# Function to translate text
def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

# Function to convert text to speech
def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    filename = "translated_audio.mp3"
    tts.save(filename)
    return filename

# Function to recognize speech
def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        speech_text = recognizer.recognize_google(audio)
    except sr.RequestError:
        speech_text = "API unavailable"
    except sr.UnknownValueError:
        speech_text = "Unable to recognize speech"
    return speech_text

# Streamlit app layout
st.title("🌍 Multilingua App 📚")
st.markdown("> \"Language is the road map of a culture. It tells you where its people come from and where they are going.\" - Rita Mae Brown")

# Input field for text
input_text = st.text_area("Enter text to translate", height=150)

# Language selection
languages = {
    'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Azerbaijani': 'az',
    'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca',
    'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese (Traditional)': 'zh-tw', 'Corsican': 'co', 'Croatian': 'hr',
    'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl',
    'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el',
    'Gujarati': 'gu', 'Haitian Creole': 'ht', 'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'iw', 'Hindi': 'hi',
    'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it',
    'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Korean': 'ko', 'Kurdish': 'ku',
    'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb',
    'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi',
    'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Odia': 'or', 'Pashto': 'ps',
    'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm',
    'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk',
    'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg',
    'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug',
    'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'
}

target_language = st.selectbox("Select Target Language", list(languages.keys()))

if st.button("Translate Text"):
    if input_text:
        translated_text = translate_text(input_text, languages[target_language])
        st.subheader("Translated Text:")
        st.write(translated_text)
        audio_file = text_to_speech(translated_text, languages[target_language])
        st.audio(audio_file, format='audio/mp3')
    else:
        st.warning("Please enter text to translate.")

# Section for speech-to-text and translation
st.subheader("Speech-to-Text Translation")
st.write("Use this section to translate spoken words to the target language.")

if st.button("Speak"):
    st.write("Listening...")
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        speech_text = recognizer.recognize_google(audio)

        # Translate the recognized text to the selected language
        translated_text = translate_text(speech_text, languages[target_language])

        # Display the original and translated text
        st.subheader("Recognized Text:")
        st.write(speech_text)
        st.subheader("Translated Text:")
        st.write(translated_text)

        # Convert the translated text to speech and display the audio player
        audio_file = text_to_speech(translated_text, languages[target_language])
        st.audio(audio_file, format='audio/mp3')

    except sr.RequestError:
        st.error("API unavailable")
    except sr.UnknownValueError:
        st.error("Unable to recognize speech. Please check your microphone and try again.")

if st.button("Translate Speech"):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        speech_text = recognizer.recognize_google(audio)
        translated_text = translate_text(speech_text, languages[target_language])
        st.subheader("Translated Text:")
        st.write(translated_text)
        audio_file = text_to_speech(translated_text, languages[target_language])
        st.audio(audio_file, format='audio/mp3')
    except sr.RequestError:
        st.error("API unavailable")
    except sr.UnknownValueError:
        st.error("Unable to recognize speech. Please try again.")

# Upload text file for translation
st.subheader("Text File Translation")
st.write("Upload a text file (.txt) to translate its content.")

uploaded_file = st.file_uploader("Upload a text file (.txt)", type=["txt"])

if st.button("Translate File"):
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")

        try:
            # Translate the text to the selected language
            translated_text = translate_text(content, languages[target_language])

            # Display the original and translated text
            st.subheader("Original Text:")
            st.write(content)
            st.subheader("Translated Text:")
            st.write(translated_text)

            # Convert the translated text to speech and display the audio player
            audio_file = text_to_speech(translated_text, languages[target_language])
            st.audio(audio_file, format='audio/mp3')

        except Exception as e:
            st.error(f"An error occurred during text file translation: {e}")
    else:
        st.warning("Please upload a text file to translate.")

# Creative section in the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### Multilingua Highlights")
st.sidebar.markdown("🌐 Supports over 100 languages.")
st.sidebar.markdown("🎤 Converts text to speech.")
st.sidebar.markdown("🗣️ Converts speech to text.")
st.sidebar.markdown("🧠 Built with advanced translation technology.")
