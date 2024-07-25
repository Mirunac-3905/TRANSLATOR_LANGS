
# import streamlit as st
# from googletrans import Translator
# from gtts import gTTS
# import pytesseract
# from PIL import Image
# from pymongo import MongoClient
# import bcrypt

# # MongoDB setup
# client = MongoClient("mongodb://localhost:27017/")
# db = client["language_translator"]
# users_collection = db["users"]

# # Function to hash passwords
# def hash_password(password):
#     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# # Function to check passwords
# def check_password(hashed_password, password):
#     return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# # Function to translate text
# def translate_text(text, target_language):
#     translator = Translator()
#     translated = translator.translate(text, dest=target_language)
#     return translated.text

# # Function to convert text to speech
# def text_to_speech(text, lang):
#     tts = gTTS(text=text, lang=lang, slow=False)
#     filename = "translated_audio.mp3"
#     tts.save(filename)
#     return filename

# # Streamlit app layout
# st.title("Language Translator")
# st.markdown("> \"Language is the road map of a culture. It tells you where its people come from and where they are going.\" - Rita Mae Brown")

# # Check if the user is already registered
# registered_usernames = [user['username'] for user in users_collection.find()]

# # Display register section
# st.header("Register")
# new_username = st.text_input("Username", key="register_username")
# new_password = st.text_input("Password", type="password", key="register_password")
# email = st.text_input("Email", key="register_email")

# if st.button("Create Account"):
#     if new_username in registered_usernames:
#         st.error("This username is already taken. Please choose another one.")
#     else:
#         hashed_password = hash_password(new_password)
#         users_collection.insert_one({"username": new_username, "password": hashed_password, "email": email})
#         st.success("Account created successfully! Now you can login.")

# # Display login section
# st.header("Login")
# username = st.text_input("Username", key="login_username")
# password = st.text_input("Password", type="password", key="login_password")

# if st.button("Login"):
#     user = users_collection.find_one({"username": username})

#     if user:
#         if check_password(user["password"], password):
#             st.success(f"Logged in as {username}")
#             st.session_state.logged_in = True
#             st.session_state.username = username
#         else:
#             st.error("Incorrect password")
#     else:
#         st.error("User not found")

# # Redirect to main page after successful login
# if "logged_in" in st.session_state and st.session_state.logged_in:
#     st.header(f"Welcome {st.session_state['username']}!")

#     # Input field for text
#     input_text = st.text_area("Enter text to translate", height=150)

#     # Language selection
#     languages = {
#         'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Azerbaijani': 'az',
#         'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca',
#         'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese (Traditional)': 'zh-tw', 'Corsican': 'co', 'Croatian': 'hr',
#         'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl',
#         'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el',
#         'Gujarati': 'gu', 'Haitian Creole': 'ht', 'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'iw', 'Hindi': 'hi',
#         'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it',
#         'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Korean': 'ko', 'Kurdish': 'ku',
#         'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb',
#         'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi',
#         'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Odia': 'or', 'Pashto': 'ps',
#         'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm',
#         'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk',
#         'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg',
#         'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug',
#         'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'
#     }

#     target_language = st.selectbox("Select Target Language", list(languages.keys()))

#     # Upload image or text file
#     uploaded_file = st.file_uploader("Upload an image with text or a text file to translate", type=["jpg", "jpeg", "png", "txt"])

#     # Translate button
#     if st.button("Translate"):
#         if uploaded_file is not None:
#             # Check file type and process accordingly
#             if uploaded_file.type.startswith('image'):
#                 try:
#                     image = Image.open(uploaded_file)
#                     st.image(image, caption="Uploaded Image", use_column_width=True)

#                     # Extract text from the image using Tesseract OCR
#                     extracted_text = pytesseract.image_to_string(image)

#                     # Translate the extracted text to the selected language
#                     translated_text = translate_text(extracted_text, languages[target_language])

#                     # Display the extracted and translated text
#                     st.subheader("Extracted Text:")
#                     st.write(extracted_text)
#                     st.subheader("Translated Text:")
#                     st.write(translated_text)

#                     # Convert the translated text to speech and display the audio player
#                     audio_file = text_to_speech(translated_text, languages[target_language])
#                     st.audio(audio_file, format='audio/mp3')
#                 except Exception as e:
#                     st.error(f"An error occurred: {e}")
#             elif uploaded_file.type == "text/plain":
#                 try:
#                     # Read the content of the text file
#                     content = uploaded_file.read().decode("utf-8")

#                     # Translate the text to the selected language
#                     translated_text = translate_text(content, languages[target_language])

#                     # Display the original and translated text
#                     st.subheader("Original Text:")
#                     st.write(content)
#                     st.subheader("Translated Text:")
#                     st.write(translated_text)

#                     # Convert the translated text to speech and display the audio player
#                     audio_file = text_to_speech(translated_text, languages[target_language])
#                     st.audio(audio_file, format='audio/mp3')
#                 except Exception as e:
#                     st.error(f"An error occurred: {e}")
#         else:
#             if input_text:
#                 try:
#                     # Translate the input text to the selected language
#                     translated_text = translate_text(input_text, languages[target_language])

#                     # Display the original and translated text
#                     st.subheader("Original Text:")
#                     st.write(input_text)
#                     st.subheader("Translated Text:")
#                     st.write(translated_text)

#                     # Convert the translated text to speech and display the audio player
#                     audio_file = text_to_speech(translated_text, languages[target_language])
#                     st.audio(audio_file, format='audio/mp3')
#                 except Exception as e:
#                     st.error(f"An error occurred: {e}")
#             else:
#                 st.error("Please enter text or upload a file to translate.")


#-------------------------------------------------------------------------------------
import streamlit as st
from googletrans import Translator
from gtts import gTTS
import pytesseract
from PIL import Image
from pymongo import MongoClient
import bcrypt

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["language_translator"]
users_collection = db["users"]

# Function to hash passwords
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to check passwords
def check_password(hashed_password, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

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

# Streamlit app layout
st.title("Language Translator")
st.markdown("> \"Language is the road map of a culture. It tells you where its people come from and where they are going.\" - Rita Mae Brown")

# Check if the user is already registered
registered_usernames = [user['username'] for user in users_collection.find()]

# Display register section
st.header("Register")
new_username = st.text_input("Username", key="register_username")
new_password = st.text_input("Password", type="password", key="register_password")
email = st.text_input("Email", key="register_email")

if st.button("Create Account"):
    if new_username in registered_usernames:
        st.error("This username is already taken. Please choose another one.")
    else:
        hashed_password = hash_password(new_password)
        users_collection.insert_one({"username": new_username, "password": hashed_password, "email": email})
        st.success("Account created successfully! Now you can login.")

# Display login section
st.header("Login")
username = st.text_input("Username", key="login_username")
password = st.text_input("Password", type="password", key="login_password")

if st.button("Login"):
    user = users_collection.find_one({"username": username})

    if user:
        if check_password(user["password"], password):
            st.success(f"Logged in as {username}")
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("Incorrect password")
    else:
        st.error("User not found")

# Redirect to main page after successful login
if "logged_in" in st.session_state and st.session_state.logged_in:
    st.header(f"Welcome {st.session_state['username']}!")

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

    # Upload image or text file
    uploaded_file = st.file_uploader("Upload an image with text or a text file to translate", type=["jpg", "jpeg", "png", "txt"])

    # Translate button
    if st.button("Translate"):
        if uploaded_file is not None:
            # Check file type and process accordingly
            if uploaded_file.type.startswith('image'):
                try:
                    image = Image.open(uploaded_file)
                    st.image(image, caption="Uploaded Image", use_column_width=True)

                    # Extract text from the image using Tesseract OCR
                    extracted_text = pytesseract.image_to_string(image)

                    # Translate the extracted text to the selected language
                    translated_text = translate_text(extracted_text, languages[target_language])

                    # Display the extracted and translated text
                    st.subheader("Extracted Text:")
                    st.write(extracted_text)
                    st.subheader("Translated Text:")
                    st.write(translated_text)

                    # Convert the translated text to speech and display the audio player
                    audio_file = text_to_speech(translated_text, languages[target_language])
                    st.audio(audio_file, format='audio/mp3')
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            elif uploaded_file.type == "text/plain":
                try:
                    # Read the content of the text file
                    content = uploaded_file.read().decode("utf-8")

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
                    st.error(f"An error occurred: {e}")
        else:
            if input_text:
                try:
                    # Translate the input text to the selected language
                    translated_text = translate_text(input_text, languages[target_language])

                    # Display the original and translated text
                    st.subheader("Original Text:")
                    st.write(input_text)
                    st.subheader("Translated Text:")
                    st.write(translated_text)

                    # Convert the translated text to speech and display the audio player
                    audio_file = text_to_speech(translated_text, languages[target_language])
                    st.audio(audio_file, format='audio/mp3')
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.error("Please enter text or upload a file to translate.")



# import streamlit as st
# from googletrans import Translator
# from gtts import gTTS
# import pytesseract as tess
# from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
# from pymongo import MongoClient
# import bcrypt

# # Set the path to the Tesseract executable
# tess.pytesseract.tesseract_cmd = r'C:\Users\HP\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# # MongoDB setup
# client = MongoClient("mongodb://localhost:27017/")
# db = client["language_translator"]
# users_collection = db["users"]

# # Function to hash passwords
# def hash_password(password):
#     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# # Function to check passwords
# def check_password(hashed_password, password):
#     return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# # Function to translate text
# def translate_text(text, target_language):
#     translator = Translator()
#     translated = translator.translate(text, dest=target_language)
#     return translated.text

# # Function to convert text to speech
# def text_to_speech(text, lang):
#     tts = gTTS(text=text, lang=lang, slow=False)
#     filename = "translated_audio.mp3"
#     tts.save(filename)
#     return filename

# # Function to overlay text on image
# def overlay_text_on_image(image, text):
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.load_default()

#     # Optionally, you could use a specific font and size
#     # font = ImageFont.truetype("arial.ttf", 15)

#     # Position for the text
#     text_position = (10, 10)

#     # Draw the text on the image
#     draw.text(text_position, text, font=font, fill="red")

#     return image

# # Streamlit app layout
# st.title("Language Translator")
# st.markdown("> \"Language is the road map of a culture. It tells you where its people come from and where they are going.\" - Rita Mae Brown")

# # Check if the user is already registered
# registered_usernames = [user['username'] for user in users_collection.find()]

# # Display register section
# st.header("Register")
# new_username = st.text_input("Username", key="register_username")
# new_password = st.text_input("Password", type="password", key="register_password")
# email = st.text_input("Email", key="register_email")

# if st.button("Create Account"):
#     if new_username in registered_usernames:
#         st.error("This username is already taken. Please choose another one.")
#     else:
#         hashed_password = hash_password(new_password)
#         users_collection.insert_one({"username": new_username, "password": hashed_password, "email": email})
#         st.success("Account created successfully! Now you can login.")

# # Display login section
# st.header("Login")
# username = st.text_input("Username", key="login_username")
# password = st.text_input("Password", type="password", key="login_password")

# if st.button("Login"):
#     user = users_collection.find_one({"username": username})

#     if user:
#         if check_password(user["password"], password):
#             st.success(f"Logged in as {username}")
#             st.session_state.logged_in = True
#             st.session_state.username = username
#         else:
#             st.error("Incorrect password")
#     else:
#         st.error("User not found")

# # Redirect to main page after successful login
# if "logged_in" in st.session_state and st.session_state.logged_in:
#     st.header(f"Welcome {st.session_state['username']}!")

#     # Input field for text
#     input_text = st.text_area("Enter text to translate", height=150)

#     # Language selection
#     languages = {
#         'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Azerbaijani': 'az',
#         'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca',
#         'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese (Traditional)': 'zh-tw', 'Corsican': 'co', 'Croatian': 'hr',
#         'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl',
#         'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el',
#         'Gujarati': 'gu', 'Haitian Creole': 'ht', 'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'iw', 'Hindi': 'hi',
#         'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it',
#         'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Korean': 'ko', 'Kurdish': 'ku',
#         'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb',
#         'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi',
#         'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Odia': 'or', 'Pashto': 'ps',
#         'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm',
#         'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk',
#         'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg',
#         'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug',
#         'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'
#     }

#     target_language = st.selectbox("Select Target Language", list(languages.keys()))

#     # Upload image or text file
#     uploaded_file = st.file_uploader("Upload an image with text or a text file to translate", type=["jpg", "jpeg", "png", "txt"])

#     # Translate button
#     if st.button("Translate"):
#         if uploaded_file is not None:
#             # Check file type and process accordingly
#             if uploaded_file.type.startswith('image'):
#                 try:
#                     # Read the image
#                     image = Image.open(uploaded_file)

#                     # Enhance and preprocess the image
#                     image = image.convert('L')  # Convert to grayscale
#                     image = image.filter(ImageFilter.SHARPEN)  # Apply sharpening filter
#                     enhancer = ImageEnhance.Contrast(image)
#                     image = enhancer.enhance(2)  # Enhance contrast

#                     # Perform OCR on the image with additional configuration
#                     custom_config = r'--oem 3 --psm 6'
#                     extracted_text = tess.image_to_string(image, config=custom_config)

#                     # Translate the extracted text to the selected language
#                     translated_text = translate_text(extracted_text, languages[target_language])

#                     # Overlay the translated text on the image
#                     translated_image = overlay_text_on_image(image.copy(), translated_text)

#                     # Display the processed image
#                     st.image(translated_image, caption="Translated Image", use_column_width=True)

#                     # Display the extracted and translated text
#                     st.subheader("Extracted Text:")
#                     st.write(extracted_text)
#                     st.subheader("Translated Text:")
#                     st.write(translated_text)

#                     # Convert the translated text to speech and display the audio player
#                     audio_file = text_to_speech(translated_text, languages[target_language])
#                     st.audio(audio_file, format='audio/mp3')
#                 except Exception as e:
#                     st.error(f"An error occurred: {e}")
#             elif uploaded_file.type == "text/plain":
#                 try:
#                     # Read the content of the text file
#                     content = uploaded_file.read().decode("utf-8")

#                     # Translate the text to the selected language
#                     translated_text = translate_text(content, languages[target_language])

#                     # Display the original and translated text
#                     st.subheader("Original Text:")
#                     st.write(content)
#                     st.subheader("Translated Text:")
#                     st.write(translated_text)

#                     # Convert the translated text to speech and display the audio player
#                     audio_file = text_to_speech(translated_text, languages[target_language])
#                     st.audio(audio_file, format='audio/mp3')
#                 except Exception as e:
#                     st.error(f"An error occurred: {e}")
#         else:
#             if input_text:
#                 try:
#                     # Translate the input text to the selected language
#                     translated_text = translate_text(input_text, languages[target_language])

#                     # Display the original and translated text
#                     st.subheader("Original Text:")
#                     st.write(input_text)
#                     st.subheader("Translated Text:")
#                     st.write(translated_text)

#                     # Convert the translated text to speech and display the audio player
#                     audio_file = text_to_speech(translated_text, languages[target_language])
#                     st.audio(audio_file, format='audio/mp3')
#                 except Exception as e:
#                     st.error(f"An error occurred: {e}")
#             else:
#                 st.error("Please enter text or upload a file to translate.")

# # Required dependencies:
# # pip install streamlit googletrans==4.0.0-rc1 gtts pytesseract pillow pymongo bcrypt

