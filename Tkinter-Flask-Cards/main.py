from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
current_card = {}
language_data = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    language_data = original_data.to_dict(orient="records")
else:
    language_data = data.to_dict(orient="records")



def get_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(language_data)
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card["English"], fill="white")

def remove_card():
    language_data.remove(current_card)
    data_to_save = pandas.DataFrame(language_data)
    data_to_save.to_csv("data/words_to_learn.csv", index=False)
    get_random_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

language_label = canvas.create_text(400, 150, text="" , font=(FONT_NAME, 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")

wrong_button = Button(image=wrong_image, highlightthickness=0, command=get_random_word)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

get_random_word()

window.mainloop()
