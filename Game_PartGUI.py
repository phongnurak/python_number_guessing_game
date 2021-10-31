from tkinter import *
from random import randint
def randomNumber(Event):
    global number; number = randint(1, 100)
    return number
def enter(Event):
    windowTwo = Tk()
    windowTwo.geometry("300x300")
    windowTwo.title("Result")
    resultLabel = Label(windowTwo, text=" ")
    resultLabel.pack(pady=120)
    userEnter = int(entryNumber.get())
    if userEnter > number:
        resultLabel.configure(text="The number is over than Random number")
    elif userEnter < number:
        resultLabel.configure(text="The number is less than Random number")
    else:
        resultLabel.configure(text="%d is Correct!!" %(number))
    windowTwo.mainloop()

mainWindow = Tk()

mainWindow.title("Number Game")
mainWindow.geometry("600x150")

buttonRan = Button(mainWindow, text="Random", width=10, height=5)
buttonRan.grid(row=1, column=0, pady=20, padx=10, sticky=N)
buttonRan.bind("<Button-1>", randomNumber)

labelNumber = Label(mainWindow, text="This game is Guessing the number").grid(row=0, column=1)
labelRule = Label(mainWindow, text="How to play").grid(row=1, column=2, padx=30, sticky=N)
ruleOne = Label(mainWindow, text="1. Click \"Random\" button").grid(row=1, column=2, pady=20, sticky=NW)
ruleTwo = Label(mainWindow, text="2. Type the guess number in the space").grid(row=1, column=2, pady=40, sticky=NW)
ruleThree = Label(mainWindow, text="3. Click \"Random\" button").grid(row=1, column=2, pady=60, sticky=NW)
ruleFour = Label(mainWindow, text="4. If your answer is incorrect. You can Guessing again ").grid(row=1, column=2, pady=80, sticky=NW)
entryNumber = Entry(mainWindow)
entryNumber.grid(row=1, column=1, sticky=N, pady=20)

buttonEnter = Button(mainWindow, text="Enter", width=10, height=2)
buttonEnter.grid(row=1, column=1, pady=65, sticky=N)
buttonEnter.bind("<Button-1>", enter)

mainWindow.mainloop()