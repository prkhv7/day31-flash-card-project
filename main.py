from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    random_word = random.choice(to_learn)
    french_word = random_word['French']
    flash_card.itemconfig(word, text=french_word)
    flash_card.itemconfig(title, text='French')


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Images
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Flash card
flash_card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card.create_image(400, 263, image=card_back_img)
flash_card.create_image(400, 263, image=card_front_img)
title = flash_card.create_text(400, 150, font=("Ariel", 40, "italic"), text="", fill="black")
word = flash_card.create_text(400, 263, font=("Ariel", 60, "bold"), text="", fill="black")
flash_card.grid(column=0, row=0, columnspan=2)

# Buttons
right_button = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
