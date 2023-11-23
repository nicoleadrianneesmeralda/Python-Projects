import tkinter as tk
import pandas as pd

#Set up the window
window = tk.Tk()
window.title("Word List")
window.geometry("505x420")
window.configure(bg="#FFD142")
window.resizable(False, False)

#Read in the word list from a CSV file
df = pd.read_csv('20 Words.csv')
print(df)
words = df['20 Words'].tolist()

#Create the listbox widget to display the words
listbox = tk.Listbox(window, bg="#FFFFFF", fg="#000000", selectbackground="#0078D7", selectforeground="#FFFFFF", font=("Helvetica", 12))

#Add the words to the listbox
for item in df['20 Words']:
    listbox.insert(tk.END, item)

#Functions for sorting, searching, adding, and removing words
def sort():
    words.sort()
    update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for word in words:
        listbox.insert(tk.END, word)

def search_word():
    word = entry_search.get().lower()
    if word in words:
        searched_word = "Word exists."
        #Highlight the searched word
        listbox.selection_clear(0, tk.END)
        for i, w in enumerate(words):
            if w == word:
                listbox.selection_set(i)
                listbox.see(i)
                break
    else:
        searched_word = "Word not found."
    label_searched_word.config(text=searched_word)

def add():
    item = entry_add.get().lower()
    words.append(item)
    listbox.insert(tk.END, item)
    entry_add.delete(0, tk.END)

def remove():
    selected_item = listbox.curselection()
    if selected_item:
        index = int(selected_item[0])
        listbox.delete(index)
        words.pop(index)

#Creating widgets and arranging them
label_search = tk.Label(window, text="Search a word:", font=("Helvetica", 14), bg="#FFD142")
entry_search = tk.Entry(window, font=("Helvetica", 14))
button_search = tk.Button(window, text="Search", font=("Helvetica", 14), bg="#0078D7", fg="#FFFFFF", command=search_word)
label_searched_word = tk.Label(window, text="20 Words", font=("Helvetica", 13), bg="#FFD142")
label_add = tk.Label(window, text="Add a word:", font=("Helvetica", 14), bg="#FFD142")
entry_add = tk.Entry(window, font=("Helvetica", 14))
button_add = tk.Button(window, text="Add", font=("Helvetica", 14), bg="#0078D7", fg="#FFFFFF", command=add)
button_remove = tk.Button(window, text="Remove", font=("Helvetica", 14), bg="#0078D7", fg="#FFFFFF", command=remove)
sort_button = tk.Button(window, text="Sort", font=("Helvetica", 14), bg="#0078D7", fg="#FFFFFF", command=sort)

label_search.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_search.grid(row=0, column=1, padx=10, pady=10, sticky="w")
button_search.grid(row=0, column=2, padx=10, pady=10, sticky="e")
label_searched_word.grid(row=1, column=0,  padx=10, pady=0, sticky="w")
listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
sort_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")
label_add.grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_add.grid(row=4, column=1, padx=10, pady=10, sticky="w")
button_add.grid(row=4, column=2, padx=10, pady=10, sticky="e")
button_remove.grid(row=3, column=2, padx=10, pady=10, sticky="e")


window.mainloop()