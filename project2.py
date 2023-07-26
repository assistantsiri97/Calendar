import tkinter as tk
from tkcalendar import Calendar

def on_date_selected():
    selected_date = cal.get_date()
    selected_date_label.config(text="Today's Date Is " + selected_date)

# Create the main application window
fun = tk.Tk()
fun.title("Calendar")

# Create a frame to hold the Calendar widget
frame = tk.Frame(fun,)
frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Create the Calendar widget
cal = Calendar(frame, selectmode="day", year=2023,month=7,day=25,background="lightblue",foreground="black")
cal.pack(fill=tk.BOTH, expand=True)

# Create a label to display the selected date
selected_date_label = tk.Label(fun, background="pink")
selected_date_label.pack()

# Create a button to get the selected date
get_date_button = tk.Button(fun, text="Get Selected Date", command=on_date_selected,font=10,background="black",foreground="white")
get_date_button.pack(pady=20)


fun.mainloop()
