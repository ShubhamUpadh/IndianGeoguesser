import random
from tkinter import *
from tkinter.ttk import *

states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi", "Goa", "Gujarat",
          "Haryana",
          "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
          "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Tripura", "Sikkim", "Tamil Nadu",
          "Uttar Pradesh", "West Bengal"]
# print(len(states))
states_lower = list(map(lambda x: x.lower(), states))  # stores the names of the states in lowercase

state_n = random.choice(states)

root = Tk()
root.geometry("1368x768")
root.title("Indian GeoGuesser")

label = Label(root, text="Welcome to Indian GeoGuesser", font=("Arial", 20))
label.pack(padx=5, pady=5)

'''
def fx_stateimg():
    global state_n
    str1 = "C:\\Users\\91995\\PycharmProjects\\Desi_Worldle\\States\\" + state_n + ".png"

    photo = PhotoImage(file=str1)
    photo_label = Label(image=photo)
    photo_label.pack()
'''

frame = Frame(root)
frame.pack(side="top", expand=True, fill="both")
Label(frame, text="Enter the Password", font=('Helvetica', 20)).pack(pady=20)


def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()


button = Button(root, text="Enter", command=clear_frame)
button.pack()
root.mainloop()
