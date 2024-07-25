import streamlit as st
from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
import io
import os

# Function to translate text
def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text, translated.src

# Function to convert text to speech
def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    filename = "translated_audio.mp3"
    tts.save(filename)
    return filename

# Function to recognize speech from audio file
def recognize_speech_from_audio(file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = recognizer.record(source)
    try:
        speech_text = recognizer.recognize_google(audio)
    except sr.RequestError:
        speech_text = "API unavailable"
    except sr.UnknownValueError:
        speech_text = "Unable to recognize speech"
    return speech_text

# Function to detect language
def detect_language(text):
    translator = Translator()
    return translator.detect(text).lang

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        color: #2e86c1;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 24px;
        color: #3498db;
    }
    .highlight {
        background-color: #ecf0f1;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .sidebar {
        background-color: #3498db;
        color: white;
    }
    .sidebar .sidebar-content {
        color: white;
    }
    .btn-primary {
        background-color: #3498db;
        color: white;
    }
    .btn-primary:hover {
        background-color: #2980b9;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app layout
st.title("🌍 Multilingua App 📚")
st.markdown("> \"Language is the road map of a culture. It tells you where its people come from and where they are going.\" - Rita Mae Brown")

# Input field for text
input_text = st.text_area("Enter text to translate", height=150, placeholder="Type your text here...")

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

# Add language-specific emojis
language_emojis = {
    'af': '🇿🇦', 'sq': '🇦🇱', 'am': '🇪🇹', 'ar': '🇸🇦', 'hy': '🇦🇲', 'az': '🇦🇿',
    'eu': '🇪🇸', 'be': '🇧🇾', 'bn': '🇧🇩', 'bs': '🇧🇦', 'bg': '🇧🇬', 'ca': '🇪🇸',
    'ceb': '🇵🇭', 'ny': '🇲🇼', 'zh-tw': '🇹🇼', 'co': '🇫🇷', 'hr': '🇭🇷', 'cs': '🇨🇿',
    'da': '🇩🇰', 'nl': '🇳🇱', 'en': '🇬🇧', 'eo': '🇪🇪', 'et': '🇪🇪', 'tl': '🇵🇭',
    'fi': '🇫🇮', 'fr': '🇫🇷', 'fy': '🇳🇱', 'gl': '🇪🇸', 'ka': '🇬🇪', 'de': '🇩🇪',
    'el': '🇬🇷', 'gu': '🇮🇳', 'ht': '🇭🇹', 'ha': '🇳🇬', 'haw': '🇺🇸', 'iw': '🇮🇱',
    'hi': '🇮🇳', 'hmn': '🇲🇲', 'hu': '🇭🇺', 'is': '🇮🇸', 'ig': '🇳🇬', 'id': '🇮🇩',
    'ga': '🇮🇪', 'it': '🇮🇹', 'ja': '🇯🇵', 'jw': '🇮🇩', 'kn': '🇮🇳', 'kk': '🇰🇿',
    'km': '🇰🇭', 'ko': '🇰🇷', 'ku': '🇹🇷', 'ky': '🇰🇬', 'lo': '🇱🇦', 'la': '🇲🇭',
    'lv': '🇱🇻', 'lt': '🇱🇹', 'lb': '🇱🇺', 'mk': '🇲🇰', 'mg': '🇲🇬', 'ms': '🇲🇾',
    'ml': '🇮🇳', 'mt': '🇲🇹', 'mi': '🇳🇿', 'mr': '🇮🇳', 'mn': '🇲🇳', 'my': '🇲🇲',
    'ne': '🇳🇵', 'no': '🇳🇴', 'or': '🇮🇳', 'ps': '🇦🇫', 'fa': '🇮🇷', 'pl': '🇵🇱',
    'pt': '🇵🇹', 'pa': '🇮🇳', 'ro': '🇷🇴', 'ru': '🇷🇺', 'sm': '🇼🇸', 'gd': '🇬🇧',
    'sr': '🇷🇸', 'st': '🇱🇸', 'sn': '🇿🇼', 'sd': '🇵🇰', 'si': '🇱🇰', 'sk': '🇸🇰',
    'sl': '🇸🇮', 'so': '🇸🇴', 'es': '🇪🇸', 'su': '🇲🇨', 'sw': '🇰🇪', 'sv': '🇸🇪',
    'tg': '🇹🇯', 'ta': '🇮🇳', 'te': '🇮🇳', 'th': '🇹🇭', 'tr': '🇹🇷', 'uk': '🇺🇦',
    'ur': '🇵🇰', 'ug': '🇺🇳', 'uz': '🇺🇿', 'vi': '🇻🇳', 'cy': '🇬🇧', 'xh': '🇿🇦',
    'yi': '🇩🇪', 'yo': '🇳🇬', 'zu': '🇿🇦'
}

# Display the selected language's emoji
target_language_emoji = language_emojis.get(languages[target_language], '🌍')

if st.button("Translate Text"):
    if input_text:
        translated_text, detected_lang = translate_text(input_text, languages[target_language])
        st.subheader("Detected Language:")
        st.write(f"{detected_lang} {language_emojis.get(detected_lang, '')}")
        st.subheader("Translated Text:")
        st.markdown(f"<div class='highlight'>{translated_text}</div>", unsafe_allow_html=True)
        audio_file = text_to_speech(translated_text, languages[target_language])
        st.audio(audio_file, format='audio/mp3')
        
    else:
        st.warning("Please enter text to translate.")

# Section for speech-to-text and translation
st.subheader("Speech-to-Text Translation")
st.write("Upload an audio file to transcribe and translate.")

uploaded_audio = st.file_uploader("Upload an audio file", type=["wav", "flac", "aiff"])

if st.button("Translate Audio"):
    if uploaded_audio is not None:
        try:
            speech_text = recognize_speech_from_audio(uploaded_audio)
            translated_text, detected_lang = translate_text(speech_text, languages[target_language])

            # Display the recognized and translated text
            st.subheader("Recognized Text:")
            st.markdown(f"<div class='highlight'>{speech_text}</div>", unsafe_allow_html=True)
            st.subheader("Translated Text:")
            st.markdown(f"<div class='highlight'>{translated_text}</div>", unsafe_allow_html=True)

            # Convert the translated text to speech and display the audio player
            audio_file = text_to_speech(translated_text, languages[target_language])
            st.audio(audio_file, format='audio/mp3')
          
        except Exception as e:
            st.error(f"An error occurred during audio translation: {e}")
    else:
        st.warning("Please upload an audio file to translate.")

# Upload text file for translation
st.subheader("Text File Translation")
st.write("Upload a text file (.txt) to translate its content.")

uploaded_file = st.file_uploader("Upload a text file (.txt)", type=["txt"])

if st.button("Translate File"):
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")

        try:
            # Translate the text to the selected language
            translated_text, detected_lang = translate_text(content, languages[target_language])

            # Display the original and translated text
            st.subheader("Original Text:")
            st.markdown(f"<div class='highlight'>{content}</div>", unsafe_allow_html=True)
            st.subheader("Translated Text:")
            st.markdown(f"<div class='highlight'>{translated_text}</div>", unsafe_allow_html=True)

            # Convert the translated text to speech and display the audio player
            audio_file = text_to_speech(translated_text, languages[target_language])
            st.audio(audio_file, format='audio/mp3')
          
        except Exception as e:
            st.error(f"An error occurred during text file translation: {e}")
    else:
        st.warning("Please upload a text file to translate.")

# Recent translations history
if 'history' not in st.session_state:
    st.session_state.history = []

st.subheader("Recent Translations")
if st.session_state.history:
    for item in st.session_state.history:
        st.markdown(f"<div class='highlight'>Text: {item['text']}<br>Translated: {item['translated']}</div>", unsafe_allow_html=True)
else:
    st.write("No recent translations.")

if input_text and st.button("Save Translation"):
    st.session_state.history.append({
        'text': input_text,
        'translated': translate_text(input_text, languages[target_language])[0]
    })
    
# User feedback
st.sidebar.markdown("---")
st.sidebar.markdown("### Multilingua Highlights")
st.sidebar.markdown("🌐 Supports over 100 languages.")
st.sidebar.markdown("🎤 Converts text to speech.")
st.sidebar.markdown("🗣️ Converts speech to text.")
st.sidebar.markdown("🧠 Built with advanced translation technology.")
st.sidebar.markdown("📝 We value your feedback!")
feedback = st.sidebar.text_area("Leave your feedback here:", height=150)
if st.sidebar.button("Submit Feedback"):
    if feedback:
        st.sidebar.success("Thank you for your feedback!")
    else:
        st.sidebar.warning("Please enter some feedback.")
