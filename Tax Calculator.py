import tkinter as tk

def calculate_tax():
    gross_income = float(ent_gross_income.get())
    dependents = int(ent_dependents.get())
    filing_status = var_filing_status.get()

    if filing_status == 1:
        tax_rate = 0.2
    elif filing_status == 2:
        tax_rate = 0.15
    elif filing_status == 3:
        tax_rate = 0.1

    total_tax = float((tax_rate * gross_income) / dependents)

    result_total_tax.config(text=f"{total_tax:.2f}")

window = tk.Tk()
window.title("Tax Calculator")
window.geometry("400x180")
window.resizable(False, False)

lbl_gross_income = tk.Label(window, text="Gross income:")
lbl_gross_income.grid(row=0, column=0, padx=5, pady=5)

ent_gross_income = tk.Entry(window)
ent_gross_income.grid(row=0, column=1, padx=5, pady=5)

lbl_dependents = tk.Label(window, text="Dependents:")
lbl_dependents.grid(row=1, column=0, padx=5, pady=5)

ent_dependents = tk.Entry(window)
ent_dependents.grid(row=1, column=1, padx=5, pady=5)

lbl_filing_status = tk.Label(window, text="Filing status:")
lbl_filing_status.grid(row=2, column=0, padx=5, pady=5)

var_filing_status = tk.IntVar()
radio_single = tk.Radiobutton(window, text="Single", variable=var_filing_status, value=1)
radio_married = tk.Radiobutton(window, text="Married", variable=var_filing_status, value=2)
radio_divorced = tk.Radiobutton(window, text="Divorced", variable=var_filing_status, value=3)
var_filing_status.set(1) #default single

radio_single.grid(row=2, column=1, padx=5, pady=5)
radio_married.grid(row=2, column=2, padx=5, pady=5)
radio_divorced.grid(row=2, column=3, padx=5, pady=5)

btn_calculate = tk.Button(window, text="Calculate", command=calculate_tax)
btn_calculate.grid(row=3, column=1, padx=5, pady=5)

lbl_total_tax = tk.Label(window, text="Total tax:")
lbl_total_tax.grid(row=4, column=0, padx=5, pady=5)

result_total_tax = tk.Label(window, text="0.0", width=17, borderwidth=1, relief="sunken", bg="white", anchor="w")
result_total_tax.grid(row=4, column=1, padx=5, pady=5)

window.mainloop()
