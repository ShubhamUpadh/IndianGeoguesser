'''
It comprises eight states – Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland,
Tripura and Sikkim.
'''
import random
from tkinter import *
from tkinter.ttk import *

states = ["Arunachal Pradesh", "Assam", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
          "Tripura", "Sikkim", "Maharashtra", "Uttar Pradesh"]

states_lower = list(map(lambda x: x.lower(), states))  # stores the names of the states in lowercase

state_n = random.choice(states)

# state_n = "Uttar Pradesh"


# STATE NAME AND STRING DECLARED
counter = 1  # counting variable

# HEADING AND TEXT START
root = Tk()
root.geometry("1368x768")
root.title("Indian GeoGuesser")

label = Label(root, text="Welcome to Indian GeoGuesser", font=("Arial", 20))
label.pack(padx=5, pady=5)

label = Label(root, text="You will be shown image of an Indian State. You have to enter its "
                         "correct name in three chances \n", font=("Arial", 15))
label.pack(padx=5, pady=5)
# HEADING AND TEXT END


# DISPLAY IMAGE START
str1 = "C:\\Users\\91995\\PycharmProjects\\Desi_Worldle\\States\\" + state_n + ".png"

photo = PhotoImage(file=str1)
photo_label = Label(image=photo)
photo_label.pack()
root.resizable(False, False)  # prevents resizing of the window
# DISPLAY IMAGE END


# ENTER STATE NAME START

label = Label(root, text="Enter the state's name ", font=("Arial", 12))
label.pack(padx=5, pady=5)

label1 = Label(root, text="You will be given THREE chances", font=("Arial", 15))
label1.pack(padx=5, pady=0)
e = Entry(root, width=25)
e.pack()


def fx_NameCheck1():
    flag = True
    global counter

    if counter <= 3:
        if not e.get().lower() in states_lower:
            flag = False

            slabel = Label(root, text="Your input is invalid.Please RECHECK your input. Attempt #" + str(counter),
                           font=("Arial", 15))
            slabel.pack()

        if e.get().lower().strip() == state_n.lower():
            slabel = Label(root, text="Correct Input, The name of the state is "
                                      + state_n.upper() + " !! Attempt #" + str(counter), font=("Arial", 15))
            slabel.pack()

        else:
            if flag:
                klabel = Label(root, text=" Incorrect. The name of the state is not "
                                          + e.get().upper() + " ! Please try again ! Attempt #" + str(counter),
                               font=("Arial", 15))
                klabel.pack()

    if counter > 3:
        clabel = Label(root, text=" Number of attempts has been exceeded.", font=("Arial", 15))
        clabel.pack()

    counter += 1


def fx_Delete():
    dlabel = Label(root, text=" Closing the game!!!", font=("Arial", 15))
    dlabel.pack()

    var = IntVar()
    root.after(1000, var.set, 1)
    root.wait_variable(var)
    root.destroy()


label = Label(root, text="")
label.pack()

button = Button(root, text="Enter", command=fx_NameCheck1)
button.pack()

button = Button(root, text="Close", command=fx_Delete)
button.pack()

root.mainloop()
