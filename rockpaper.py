import tkinter as tk
import random

def play(choice):
    comp = random.choice(options)
    user_choice_label.config(text=choice)
    comp_choice_label.config(text=comp)
    result = ""
    if choice == comp:
        result = "It's a Tie!"
    elif (
        (choice == "Rock" and comp == "Scissors") or
        (choice == "Paper" and comp == "Rock") or
        (choice == "Scissors" and comp == "Paper")
    ):
        scores['user'] += 1
        result = "You Win!"
    else:
        scores['comp'] += 1
        result = "Computer Wins!"
    user_score_label.config(text=str(scores['user']))
    comp_score_label.config(text=str(scores['comp']))
    result_label.config(text=result)

def reset_game():
    scores['user'] = 0
    scores['comp'] = 0
    user_score_label.config(text="0")
    comp_score_label.config(text="0")
    user_choice_label.config(text="")
    comp_choice_label.config(text="")
    result_label.config(text="")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x330")

options = ["Rock", "Paper", "Scissors"]
scores = {'user': 0, 'comp': 0}

tk.Label(root, text="Rock Paper Scissors", font=('Arial', 18, 'bold')).pack(pady=10)

score_frame = tk.Frame(root)
score_frame.pack()
tk.Label(score_frame, text="Your Score:", font=('Arial', 12)).grid(row=0, column=0)
user_score_label = tk.Label(score_frame, text="0", font=('Arial', 14, 'bold'), fg='green')
user_score_label.grid(row=0, column=1)
tk.Label(score_frame, text="Computer Score:", font=('Arial', 12)).grid(row=0, column=2)
comp_score_label = tk.Label(score_frame, text="0", font=('Arial', 14, 'bold'), fg='red')
comp_score_label.grid(row=0, column=3)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)
for i, opt in enumerate(options):
    tk.Button(btn_frame, text=opt, width=12, font=('Arial', 12),
              command=lambda o=opt: play(o)).grid(row=0, column=i, padx=5)

result_frame = tk.Frame(root)
result_frame.pack(pady=5)

tk.Label(result_frame, text="Your Choice:", font=('Arial', 12)).grid(row=0, column=0)
user_choice_label = tk.Label(result_frame, text="", font=('Arial', 12, 'bold'), fg='blue')
user_choice_label.grid(row=0, column=1)
tk.Label(result_frame, text="Computer's Choice:", font=('Arial', 12)).grid(row=1, column=0)
comp_choice_label = tk.Label(result_frame, text="", font=('Arial', 12, 'bold'), fg='red')
comp_choice_label.grid(row=1, column=1)
result_label = tk.Label(root, text="", font=('Arial', 16, 'bold'), fg='#f1c40f')
result_label.pack(pady=15)

tk.Button(root, text="Reset Game", command=reset_game, width=15).pack(pady=7)

root.mainloop()
