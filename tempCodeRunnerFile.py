import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
from googletrans import Translator
from PIL import Image, ImageTk
import pytesseract
import pyttsx3  # Import the text-to-speech library

# Initialize the main window
root = tk.Tk()
root.title('Language Translator')
root.geometry('600x750')
root.config(bg='#282C34')

# Title frame
title_frame = tk.Frame(root, bg='#61AFEF')
title_frame.pack(fill='x')
title_label = tk.Label(title_frame, text="Language Translator", font=("Helvetica", 24, 'bold'), fg="white", bg='#61AFEF')
title_label.pack(pady=10)

# Function to perform translation
def translate():
    lang1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()
    
    if lang1 == '':
        messagebox.showerror('Language Translator', 'Enter the text to Translate!')
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(lang1, dest=cl)
        text_entry2.insert('end', output.text)
        speak_text(output.text)  # Call the function to speak the translated text

# Function to clear text fields
def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

# Function to speak the translated text
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to upload an image
def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        img = ImageTk.PhotoImage(image)
        img_label.config(image=img)
        img_label.image = img
        extract_text(file_path)

# Function to extract text from image and translate it
def extract_text(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    if text.strip():  # Ensure text is not empty
        text_entry1.delete(1.0, 'end')
        text_entry1.insert('end', text)
    else:
        messagebox.showerror('Language Translator', 'No text found in the image!')

# Create frames for layout
input_frame = tk.Frame(root, bg='#282C34')
input_frame.pack(pady=10)
output_frame = tk.Frame(root, bg='#282C34')
output_frame.pack(pady=10)
button_frame = tk.Frame(root, bg='#282C34')
button_frame.pack(pady=10)
image_frame = tk.Frame(root, bg='#282C34')
image_frame.pack(pady=10)

# Dropdown menus
languages = [
    'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani',
    'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan',
    'cebuano', 'chichewa', 'chinese (traditional)', 'corsican', 'croatian',
    'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino',
    'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek',
    'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi',
    'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian',
    'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish',
    'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish',
    'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori',
    'marathi', 'mongolian', 'myanmar', 'nepali', 'norwegian', 'odia', 'pashto',
    'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian',
    'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala',
    'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish',
    'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur',
    'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'
]

choose_language = ttk.Combobox(input_frame, values=languages, state='readonly', font=('Verdana', 10, 'bold'), width=30)
choose_language.set("Select Language")
choose_language.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Text entry fields
text_entry1 = tk.Text(input_frame, width=40, height=7, borderwidth=2, relief='ridge', font=('Verdana', 12))
text_entry1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

text_entry2 = tk.Text(input_frame, width=40, height=7, borderwidth=2, relief='ridge', font=('Verdana', 12))
text_entry2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Buttons
translate_btn = tk.Button(button_frame, text='Translate', command=translate, font=('Verdana', 12, 'bold'), bg='#61AFEF', fg='white', cursor="hand2", width=15)
translate_btn.grid(row=0, column=0, padx=10, pady=10)

clear_btn = tk.Button(button_frame, text='Clear', command=clear, font=('Verdana', 12, 'bold'), bg='#61AFEF', fg='white', cursor="hand2", width=15)
clear_btn.grid(row=0, column=1, padx=10, pady=10)

upload_btn = tk.Button(button_frame, text='Upload Image', command=upload_image, font=('Verdana', 12, 'bold'), bg='#61AFEF', fg='white', cursor="hand2", width=15)
upload_btn.grid(row=0, column=2, padx=10, pady=10)

# Image label
img_label = tk.Label(image_frame, bg='#282C34')
img_label.pack()

root.mainloop()



