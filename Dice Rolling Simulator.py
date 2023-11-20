import tkinter as tk #Importing the tkinter module as tk for easier usage
import random #Importing the random module

def roll_dice(): #Define a function called roll_dice
    num_dice = int(num_dice_entry.get()) #Get the number of dice from the entry field and convert it to an integer
    num_sides = int(num_sides_entry.get()) #Get the number of sides from the entry field and convert it to an integer

    results = [random.randint(1, num_sides) for _ in range(num_dice)] #Generate a list of random numbers representing dice rolls
    results_text.delete("1.0", tk.END) #Clear the previous results from the text widget
    results_text.insert(tk.END, f"{', '.join(map(str, results))}") #Insert the new results into the text widget

root = tk.Tk() #Create the main window
root.title("Dice Rolling Simulator") #Set the title of the window

root.geometry("361x390") #Set the size of the window
root.resizable(False, False) # Disable window resizing

#Define a variable for the window bg color, color of the labels, and, bg and fg color of the button.
bg_color = "#FFE77A" #Yellow
label_color = "#000000" #Black
button_bgcolor = "#2C5F2D" #Verdant Green
button_fgcolor = "#FFFFFF" #White

root.configure(bg=bg_color) #Set the background color of the window

#Create labels and entries for input
num_dice_label = tk.Label(root, text="Number of dice:", font=("Arial", 14), fg=label_color, bg=bg_color) #Create a label widget for the number of dice
num_dice_label.grid(row=0, column=0, padx=10, pady=10, sticky="w") #Position the label using the grid layout manager
num_dice_entry = tk.Entry(root, width=15, font=("Arial", 14)) #Create an entry widget for entering the number of dice
num_dice_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w") #Position the entry widget using the grid layout manager

num_sides_label = tk.Label(root, text="Number of sides:", font=("Arial", 14), fg=label_color, bg=bg_color) #Create a label widget for the number of sides
num_sides_label.grid(row=1, column=0, padx=10, pady=10, sticky="w") #Position the label using the grid layout manager
num_sides_entry = tk.Entry(root, width=15, font=("Arial", 14)) #Create an entry widget for entering the number of sides
num_sides_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w") #Position the entry widget using the grid layout manager

roll_button = tk.Button(root, text="Roll dice", command=roll_dice, font=("Arial", 14), fg=button_fgcolor, bg=button_bgcolor, width=8)  #Create a button widget for rolling the dice
roll_button.grid(row=2, column=1, padx=10, pady=10, sticky="e") #Position the button widget using the grid layout manager

results_label = tk.Label(root, text="Roll Results:", font=("Arial", 14), fg=label_color, bg=bg_color) #Create a label widget for the roll results
results_label.grid(row=3, column=0, padx=10, pady=5, sticky="w") #Position the label using the grid layout manager

results_text = tk.Text(root, font=("Arial", 14), width=30, height=8) #Create text widget for output
results_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew") #Position the text widget using the grid layout manager

root.mainloop() #Start the main event loop