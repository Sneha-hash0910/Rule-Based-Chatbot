import tkinter as tk
from tkinter import scrolledtext,messagebox
import datetime
import random
import re
from chatbot import chatbot_response

#clear chat function   
def clear_chat():
    chat_area.config(state = "normal")
    chat_area.delete("1.0", tk.END)
    chat_area.config(state = "disabled")

def save_chat():
    with open("chat_history.txt", "w", encoding = "utf-8") as file:
        file.write(chat_area.get("1.0", tk.END))
    
def send_message(event = None):
    user_message = entry.get().strip()

    if user_message == "":
        return
    
    current_time = datetime.datetime.now().strftime("%H:%M")  

    chat_area.config(state = "normal")
    chat_area.insert(tk.END, f"[{current_time}] you: {user_message}\n", "user")

    response = chatbot_response(user_message)

    chat_area.insert(tk.END, f"[{current_time}] bot: {response}\n\n", "bot")
    chat_area.config(state = "disabled")
    chat_area.yview(tk.END)

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Rule Based AI Chatbot")
root.geometry("750x650")
root.configure(bg = "#1e1e1e")
root.resizable(False, False)

#menu bar
menu = tk.Menu(root)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Save Chat", command=save_chat)
file_menu.add_command(label="Clear Chat", command=clear_chat)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

menu.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu, tearoff=0)
help_menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo(
        "About",
        "Rule-Based AI Chatbot\nDeveloped by Sneha\nCodSoft AI Internship"
    )
)

menu.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu)

#chat area
chat_area = scrolledtext.ScrolledText(root, wrap = tk.WORD, font = ("Segoe UI", 12), bg = "#2b2b2b", fg = "white", insertbackground = "white", state = "disabled") 
chat_area.pack(padx = 15, pady = 15, fill = "both", expand = True)

chat_area.tag_config("user", foreground = "#00BFFF", font = ("Segoe UI", 11, "bold"))
chat_area.tag_config("bot", foreground = "#7CFC00", font = ("Segoe UI", 11),)

chat_area.config(state = "normal")
chat_area.insert(tk.END, "Bot: Welcome to rule-based AI Chatbot!\n")
chat_area.insert(tk.END, "Bot: I can help you with:\n")
chat_area.insert(tk.END, " Date and time, Calculator, Definitions, Jokes, Fun Facts and motivate you a little\n")
chat_area.insert(tk.END, "Type 'help' anytime to see all available commands\n")
chat_area.config(state = "disabled")

entry = tk.Entry(root, font = ("Segoe UI", 12), bg = "white")
entry.pack(fill = "x", padx = 15, pady =5)
entry.bind("<Return>", send_message)

button_frame = tk.Frame(root, bg = "#1e1e1e")
button_frame.pack(pady = 10)

send_button = tk.Button(button_frame, text = "Send", width = 12, font = ("Segoe UI", 10, "bold"), command = send_message) 
send_button.grid(row = 0, column = 0, padx = 5)

clear_button = tk.Button(button_frame, text = "Clear Chat", width = 12, font = ("Segoe UI", 10, "bold"), command = clear_chat)
clear_button.grid(row = 0, column = 1, padx = 5)

save_button = tk.Button(button_frame, text = "Save Chat", width = 12, font = ("Segoe UI", 10, "bold"), command = save_chat)
save_button.grid(row = 0, column = 2, padx = 5)

root.mainloop()