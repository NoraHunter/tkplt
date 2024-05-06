import tkinter as tk
from tests import tests

root = tk.Tk()
root.geometry("1280x200+50+50")
root.title('')
root.attributes("-transparentcolor", "green")
root.config(bg="green")
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
'''def print_size(e):
    print(root.winfo_screenwidth(), root.winfo_screenheight())
root.bind("<Configure>", print_size)'''


def move_window(e):
    global root
    root.geometry(f"+{e.x_root}+{e.y_root}")

minimized = False
def minimize_window(e):
    global minimized
    if minimized:
        root.geometry("1280x200")
    else:
        root.geometry("36x20")
    minimized = not minimized

title_bar = tk.Frame(root)

minimize_btn = tk.Button(title_bar, text="M", bd=-2, padx=10, bg="white", fg="#969696")
minimize_btn.grid(row=0, column=0)
minimize_btn.bind("<Button-1>", minimize_window)

win_name = tk.Label(title_bar, text="                                                    ", bg="white")
win_name.grid(row=0, column=1)
win_name.bind("<B1-Motion>", move_window)

title_bar.pack()



BUTTON_NAME = 0
BUTTON_CARDS = 1
test_set = tests

current_cards = test_set[0][BUTTON_CARDS]
card_el_index = 0
char_buttons = []

# horizontalCharsFrame
horizontalCharsFrame = tk.Frame(root)

def change_char(e, card):
    global card_el_index, current_cards, card_lbl, found_lbl
    card_el_index = 0
    current_cards = card
    found_lbl.config(text=f"  F : {len(current_cards)}  ")
    if len(current_cards) > 0:
        card_lbl.config(text=current_cards[card_el_index])
    #print(f"current_cards={current_cards}")

def search_in_cards(e):
    s =  inputtxt.get("1.0", "end-1c")
    print(f"Search value : '{s}'")
    result = []
    for chars in test_set:
        for card in chars[BUTTON_CARDS]:
            if s.lower() in card.lower():
                result.append(card)
    change_char(e, card=result)

def clear_input(e):
    inputtxt.delete("1.0", "end-1c")

def exit_event(e):
    root.destroy()

for i in range(len(test_set)):
    char_buttons.append(tk.Button(horizontalCharsFrame, text=test_set[i][BUTTON_NAME], bd=-2, bg="white", fg="#969696"))

for i in range(len(char_buttons)):
    char_buttons[i].grid(row = 0, column = i)
    char_buttons[i].bind('<Button-1>', lambda e, card=test_set[i][BUTTON_CARDS]: change_char(e, card))
else:
    charsLastBtnInd = len(char_buttons)
    found_lbl = tk.Label(horizontalCharsFrame, text=f"  F : {len(current_cards)}  ", bg="white", fg="#969696")
    found_lbl.grid(row=0, column=charsLastBtnInd)

    inputtxt = tk.Text(horizontalCharsFrame, width=10, height=1, bd=0, bg="white", fg="#969696")
    inputtxt.grid(row=0, column=charsLastBtnInd + 1)
    inputtxt.bind("<Key>", search_in_cards)

    clear_input_btn = tk.Button(horizontalCharsFrame, text="C", bd=-2, padx=10, bg="white", fg="#969696")
    clear_input_btn.grid(row=0, column=charsLastBtnInd + 2)
    clear_input_btn.bind("<Button-1>", clear_input)

    exit_btn = tk.Button(horizontalCharsFrame, text="E", bd=-2, padx=10, bg="white", fg="#969696")
    exit_btn.grid(row=0, column=charsLastBtnInd + 4)
    exit_btn.bind("<Double-Button-1>", exit_event)
    
horizontalCharsFrame.pack()
# horizontalCharsFrame

# cards start
card_lbl = tk.Label(root, text=current_cards[0], height=7, bg="white", fg="#969696")
card_lbl.pack()
# cards end


# horizontalCardsFrame start
horizontalCardsFrame = tk.Frame(root)

prev_ans_bt = tk.Button(horizontalCardsFrame, text="<", bd=-2, bg="white", fg="#969696")
prev_ans_bt.grid(row = 0, column = 0)
def prev_ans_ev(e):
    global card_el_index
    card_el_index -= 1
    if card_el_index < 0:
        card_el_index = len(current_cards) - 1
    card_lbl.config(text=current_cards[card_el_index])
prev_ans_bt.bind("<Button-1>", prev_ans_ev)

next_ans_bt = tk.Button(horizontalCardsFrame, text=">", bd=-2, bg="white", fg="#969696")
next_ans_bt.grid(row = 0, column = 1)
def next_ans_ev(e):
    global card_el_index
    card_el_index += 1
    if card_el_index >= len(current_cards):
        card_el_index = 0
    card_lbl.config(text=current_cards[card_el_index])
next_ans_bt.bind("<Button-1>", next_ans_ev)

horizontalCardsFrame.pack()
# horizontalCardsFrame end

root.mainloop()
