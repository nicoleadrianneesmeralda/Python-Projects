import tkinter as tk
from tkinter import messagebox

def compute_netpay():
    name = ent_name.get()
    hours_worked = float(ent_hours.get())
    hourly_rate = float(ent_rate.get())
    salary_time = str(ent_time.get())
    withholding_tax = 0
    bonus = 0
    net_pay = 0

    if salary_time.upper() == '1':
        salary_time = "Day shift"
        basic_pay = hours_worked * hourly_rate
        withholding_tax = basic_pay * 0.15
        bonus = basic_pay * 0.1
        net_pay = basic_pay - withholding_tax + bonus

    elif salary_time == '2':
        salary_time = "Night shift"
        night_hourly_rate = hourly_rate * 1.10
        basic_pay = hours_worked * night_hourly_rate
        net_pay = basic_pay

    else:
        messagebox.showerror('Error', 'Salary time input is invalid. You should only enter "1" for day shift or "2" for night shift.')


    lbl_result["text"] = f"Name: {name}\nSalary Time: {salary_time}\nHours Worked: {hours_worked}\nRate Per Hour: {hourly_rate}\nWithholding Tax: {withholding_tax}\nBonus: {bonus}\nNet Pay: {net_pay}"

window = tk.Tk()
window.title("Net Pay Calculator")

lbl_name = tk.Label(window, text="Name:")
ent_name = tk.Entry(window)
lbl_hours = tk.Label(window, text="Hours Worked:")
ent_hours = tk.Entry(window)
lbl_rate = tk.Label(window, text="Hourly Rate:")
ent_rate = tk.Entry(window)
lbl_time = tk.Label(window, text='Salary time (enter "1" for day shift or "2" for night shift):')
ent_time = tk.Entry(window)
btn_calculate = tk.Button(window, text="Calculate", command=compute_netpay)
lbl_result = tk.Label(window, text="")

lbl_name.pack()
ent_name.pack()
lbl_hours.pack()
ent_hours.pack()
lbl_rate.pack()
ent_rate.pack()
lbl_time.pack()
ent_time.pack()
btn_calculate.pack()
lbl_result.pack()

window.mainloop()