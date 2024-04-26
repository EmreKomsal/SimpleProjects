import tkinter as tk

def miles_to_km(miles):
    return miles * 1.60934

def km_to_miles(km):
    return km / 1.60934

window = tk.Tk()

window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=100)


my_label = tk.Label(text="Enter Miles:")
my_label.pack()

my_entry = tk.Entry()
my_entry.pack()

my_label2 = tk.Label(text="Kilometers:")
my_label2.pack()

my_label3 = tk.Label(text="0")
my_label3.pack()

def calculate_km():
    miles = float(my_entry.get())
    km = miles_to_km(miles)
    my_label3.config(text=km)
    
my_button = tk.Button(text="Calculate", command=calculate_km)
my_button.pack()

my_label4 = tk.Label(text="Enter Kilometers:")
my_label4.pack()

my_entry2 = tk.Entry()
my_entry2.pack()

my_label5 = tk.Label(text="Miles:")
my_label5.pack()

my_label6 = tk.Label(text="0")
my_label6.pack()

def calculate_miles():
    km = float(my_entry2.get())
    miles = km_to_miles(km)
    my_label6.config(text=miles)
    
my_button2 = tk.Button(text="Calculate", command=calculate_miles)
my_button2.pack()

window.mainloop()