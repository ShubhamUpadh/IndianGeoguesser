'''
It comprises eight states – Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland,
Tripura and Sikkim.
'''
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

# state_n = "Uttar Pradesh"


# STATE NAME AND STRING DECLARED
counter = 1  # counting variable
ans = False  # Check if answer has already been entered
# HEADING AND TEXT START
root = Tk()
root.geometry("1368x768")
root.title("Indian GeoGuesser")

label = Label(root, text="Welcome to Indian GeoGuesser", font=("Arial", 20))
label.pack(padx=5, pady=5)

label = Label(root, text="You will be shown image of an Indian State.", font=("Arial", 15))
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


label1 = Label(root, text="You will be given THREE chances", font=("Arial", 15))
label1.pack(padx=5, pady=0)
e = Entry(root, width=25)
e.pack()


def fx_NameCheck1():
    flag = True

    global counter, ans

    if ans:
        alabel = Label(root, text=" Correct Answer has already been entered ", font=("Arial", 15))
        alabel.pack()

    if counter <= 3 and not ans:
        if not e.get().lower() in states_lower:
            flag = False

            slabel = Label(root, text="Your input is invalid.Please RECHECK your input. Attempt #" + str(counter),
                           font=("Arial", 15))
            slabel.pack()

        if e.get().lower().strip() == state_n.lower():

            ans = True
            slabel = Label(root, text="Correct Input, The name of the state is "
                                      + state_n.upper() + " !! Attempt #" + str(counter), font=("Arial", 15))
            slabel.pack()
            counter += 1

        else:
            if flag:

                klabel = Label(root, text=" Incorrect. The name of the state is not "
                                          + e.get().upper() + " ! Please try again ! Attempt #" + str(counter),
                               font=("Arial", 15))
                klabel.pack()
                counter += 1

    if counter > 3 and not ans:
        clabel = Label(root, text=" Number of attempts has been exceeded.", font=("Arial", 15))
        clabel.pack()

    # counter += 1


label = Label(root, text="")
label.pack()

button = Button(root, text="Enter", command=fx_NameCheck1)
button.pack()

root.mainloop()
