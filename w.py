import tkinter as tk
from tkinter import messagebox
import os
def handle_response():
    answer = response_var.get()
    if answer.lower() == "y":
        messagebox.showinfo("Response", "Keep working hard, buddy! 😊")
    elif answer.lower() == "n":
        problem_window()
    else:
        messagebox.showinfo("Response", "Invalid input. Please choose 'y' or 'n'.")

def problem_window():
    def solve():
        problem = problem_var.get()
        if problem == "1":
            messagebox.showinfo("Response", "Make a coffee, buddy! ☕ or do some exercise 💪")
        elif problem == "2":
            messagebox.showinfo("Response", "Take a 10-20 minute nap, dream chaser! 😴")
        elif problem == "3":
            messagebox.showinfo("Response", "Remove distractions and find a quiet space to work. 🤫")
        elif problem == "4":
            solve_problem = messagebox.askyesno("Question", "Can you solve this problem?")
            if solve_problem:
                messagebox.showinfo("Response", "Now let's do it!")
            else:
                messagebox.showinfo("Response", "Let's avoid this problem and move on.")
        elif problem == "5":
            messagebox.showinfo("Response", "Take a 5-minute meditation break. 🧘‍♂️")
        elif problem == "6":
            messagebox.showinfo("Response", "Watch motivational videos and switch to an interesting task. 😁")
            os.startfile("C:\\Users\\anura\\OneDrive\\Desktop\\TV\\motivation.xspf")

        elif problem == "7":
            messagebox.showinfo("Response", "This app is designed to help! You can watch motivation videos. 😊")
            os.startfile("C:\\Users\\anura\\OneDrive\\Desktop\\TV\\motivation.xspf")

        elif problem == "8":
            messagebox.showinfo("Response", "Watch happy core videos and bhajans. 🎶")
        elif problem == "9":
            messagebox.showinfo("Response", "check your routine buddy. now go my lion")
        
        else:
            messagebox.showinfo("Response", "Either it's not a problem, or I can't solve it. 🤓")
        problem_window.destroy()

    problem_window = tk.Toplevel(root)
    problem_window.title("What's the problem?")

    tk.Label(problem_window, text="What's the problem? (1-8) \n Why 😕 choose a number:\n1. Laziness\n2. Tiredness\n3. Distractions\n4. Problems\n5. Brain already loaded\n6. No mood/demotivation\n7. Procrastination\n8. Negativity\n9. confused what todo\n").pack()
    tk.Entry(problem_window, textvariable=problem_var).pack()
    tk.Button(problem_window, text="Submit", command=solve).pack()

# Create the main window
root = tk.Tk()
root.title("Buddy's Work Assistant")

# Create widgets
response_var = tk.StringVar()
problem_var = tk.StringVar()

tk.Label(root, text="Are you working buddy? 🧐 (y/n)").pack()
tk.Entry(root, textvariable=response_var).pack()
tk.Button(root, text="Submit", command=handle_response).pack()

root.mainloop()
