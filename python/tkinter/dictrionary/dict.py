from tkinter import *
import sys

# ---------------------------------------------------------
# Load words from file
lines = []
with open(sys.path[0]+"/words.csv", "r")as file:
    lines = file.readlines()
print(lines)

# ---------------------------------------------------------
# Make a cleaner dict (IS LIKE a JSON) from our lines list
words = {}
for line in lines:
    line = line.replace("\n", "")
    key, value = line.split(",")
    words[key] = value
print(words)

# ---------------------------------------------------------
# Function to translate


def translate():
    try:
        word = text_box.get()  # Get the text from text_box
        trans_label.config(text=words[word])
    except:
        trans_label.config("")


# ---------------------------------------------------------
# Make a window and set the dimensions
win = Tk()
win.geometry("300x100")
win.title("Dictionary")

# ---------------------------------------------------------
# Make a label
label = Label(text="Enter word")
label.pack()

# ---------------------------------------------------------
# Make a place to enter a text
text_box = Entry()
text_box.pack()

# ---------------------------------------------------------
# Make a button to translate a file
button = Button(text="Translate", command=translate)
button.pack()

# ---------------------------------------------------------
# Make a label to show the translation
trans_label = Label(text="")
trans_label.pack()

# ---------------------------------------------------------
win.mainloop()
