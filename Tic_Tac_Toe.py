import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if button[combo[0]]["text"] == button[combo[1]]["text"] == button[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe",f"Player {button[combo[0]]["text"]} wins")
            root.quit()
            
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        button[index]["text"] = current_player
        check_winner()
        toggle_player()
        
def toggle_player():
    global current_player
    current_player = "x" if current_player == "0" else "O"
    label.config(text=f"Player {current_player}'s turn")

root=tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root,text="", font=("normal",25), width = 4, height = 4, command=lambda i=1: button_click(i)) for i in range(9)]

for i,button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)
    
current_player = "x"
winner=False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal",19))

root.mainloop()