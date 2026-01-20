import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Rome", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["Python", "Java", "HTML", "C++"],
        "answer": "HTML"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["5", "8", "10", "15"],
        "answer": "8"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Unit",
            "Control Processing Unit"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which programming language is best for data science?",
        "options": ["Python", "HTML", "CSS", "PHP"],
        "answer": "Python"
    },
    {
        "question": "Who developed Python?",
        "options": [
            "Dennis Ritchie",
            "James Gosling",
            "Guido van Rossum",
            "Bjarne Stroustrup"
        ],
        "answer": "Guido van Rossum"
    },
    {
        "question": "What is the result of 10 / 2?",
        "options": ["2", "5", "10", "20"],
        "answer": "5"
    },
    {
        "question": "Which symbol is used to comment in Python?",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": "#"
    },
    {
        "question": "Which device is used to input data?",
        "options": ["Monitor", "Printer", "Keyboard", "Speaker"],
        "answer": "Keyboard"
    },
    {
        "question": "Which operating system is open-source?",
        "options": ["Windows", "macOS", "Linux", "DOS"],
        "answer": "Linux"
    },
    {
        "question": "What is the extension of a Python file?",
        "options": [".java", ".py", ".html", ".exe"],
        "answer": ".py"
    }
]

root = tk.Tk()
root.title("GUI Quiz App")
root.geometry("400x300")

current_question = 0
score = 0

def show_question():
    question_label.config(text=questions[current_question]["question"])
    for i in range(4):
        option_buttons[i].config(
            text=questions[current_question]["options"][i],
            state=tk.NORMAL
        )

def check_answer(selected):
    global current_question, score
    if selected == questions[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        messagebox.showinfo(
            "Quiz Finished",
            f"Your score: {score} / {len(questions)}"
        )
        root.quit()

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    wraplength=350
)
question_label.pack(pady=20)

option_buttons = []

for i in range(4):
    btn = tk.Button(
        root,
        text="",
        width=20,
        command=lambda i=i: check_answer(option_buttons[i]["text"])
    )
    btn.pack(pady=5)
    option_buttons.append(btn)

show_question()
root.mainloop()
