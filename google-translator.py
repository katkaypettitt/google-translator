from tkinter import Tk, ttk, Text, Label, END, Button, WORD
from googletrans import Translator, LANGUAGES  # Install googletrans==3.1.0a0 if NoneType error

root = Tk()  # Initialise tkinter
root.geometry('1080x350')  # Set width and height of window
root.resizable(0, 0)  # Set fixed size window
root.config(bg='ghost white')
root.title('Python Translator Engine')

# Heading
# 'pack' organises widget in block
Label(root, text='Language Translator', font='arial 20 bold', bg='ghost white', pady=10).pack()

# Input text widget
# 'wrap=WORD' will stop line after last word that will fit
input_text = Text(root, font='arial 12', height=11, wrap=WORD, padx=5, pady=5, width=60)
input_text.place(x=30, y=100)

# Output text widget
output_text = Text(root, font='arial 12', height=11, wrap=WORD, padx=5, pady=5, width=60)
output_text.place(x=600, y=100)

language = [language.title() for language in LANGUAGES.values()]  # Language list

# Input language drop-down box
src_lang = ttk.Combobox(root, values=language, width=22)
src_lang.place(x=20, y=60)
src_lang.set('Input Language')

# Output language drop-down box
dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=800, y=60)
dest_lang.set('Output Language')


def simple_translation():
    """Main translating function."""
    translator = Translator()
    translated = translator.translate(text=input_text.get(1.0, END), src=src_lang.get(), dest=dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)


# Translate button; 'command' is called when button is clicked
trans_btn = Button(root, text='Translate', font='arial 14 bold', pady=5, command=simple_translation, bg='royalblue1',
                   activebackground='sky blue')
trans_btn.place(x=500, y=180)
root.mainloop()
