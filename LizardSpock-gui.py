from tkinter import *
# Import random number function to generate a random number.
import random

# Build the window
window = Tk()
window.title("LizardSpock")
window.geometry("300x300")


class LizardSpock:
    computerscore = 0
    tiescore = 0
    playerscore = 0
    optionslist = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]

    def __init__(self, master):
        # build the items for the form

        self.cnameLabel = Label(text="Computer: ")
        self.computerLabel = Label(text="0")
        self.cguessLabel = Label(text=" ")

        self.tnameLabel = Label(text="Tie: ")
        self.tieLabel = Label(text="0")

        self.pnameLabel = Label(text="Player: ")
        self.playerLabel = Label(text="0")
        self.pguessLabel = Label(text=" ")

        self.rockButton = Button(master, text="Rock", command=lambda:self.play(0))
        self.paperButton = Button(master, text="Paper", command=lambda:self.play(1))
        self.scissorsButton = Button(master, text="Scissors", command=lambda:self.play(2))
        self.lizardButton = Button(master, text="Lizard", command=lambda:self.play(4))
        self.spockButton = Button(master, text="Spock", command=lambda:self.play(3))

        self.winnerLabel = Label(text=" ")

        # display the items on the form
        self.cnameLabel.grid(row=0, column=0)
        self.computerLabel.grid(row=1, column=0)
        self.cguessLabel.grid(row=2, column=0)

        self.tnameLabel.grid(row=0, column=1, padx=10)
        self.tieLabel.grid(row=1, column=1, padx=10)

        self.pnameLabel.grid(row=0, column=2, padx=10)
        self.playerLabel.grid(row=1, column=2, padx=10)
        self.pguessLabel.grid(row=2, column=2, padx=10)

        self.rockButton.grid(row=3, column=0, pady=10, padx=35)
        self.paperButton.grid(row=3, column=2, pady=10, padx=20)
        self.scissorsButton.grid(row=4, column=0, pady=10, padx=35)
        self.lizardButton.grid(row=4, column=2, pady=10, padx=20)
        self.spockButton .grid(row=5, column=1, pady=10, padx=10)

    def play(self, p):

        # Destroy the old data to make way for new data
        self.computerLabel.destroy()
        self.cguessLabel.destroy()
        self.playerLabel.destroy()
        self.pguessLabel.destroy()
        self.tieLabel.destroy()
        self.winnerLabel.destroy()

        # Let the computer chose a random number to select the computer's guess
        c = random.randint(0, 4)
        '''
        First check to see if there is a tie by comparing the number for the computer's guess with the number
        for the player's guess.  If the number associated with the player's guess minus the number for the 
        computer's guess modulus five (p-c)%5 is even the computer wins.  Else the player wins. 
        '''
        if p == c:
            winner="There's a tie."
            LizardSpock.tiescore = LizardSpock.tiescore + 1
        else:
            w = (p-c)%5
            if w%2 == 0:
                winner = "The Computer wins."
                LizardSpock.computerscore = LizardSpock.computerscore + 1

            else:
                winner = "YOU WIN!!"
                LizardSpock.playerscore=LizardSpock.playerscore +1

        # get the updated data for the form
        self.cguessLabel = Label(text=LizardSpock.optionslist[c])
        self.pguessLabel = Label(text=self.optionslist[p])
        self.computerLabel = Label(text=LizardSpock.computerscore)
        self.tieLabel = Label(text=LizardSpock.tiescore)
        self.playerLabel = Label(text=LizardSpock.playerscore)
        self.winnerLabel = Label(text=winner)

        # display the updated data on the form
        self.computerLabel.grid(row=1, column=0)
        self.cguessLabel.grid(row=2, column=0)
        self.tieLabel.grid(row=1, column=1)
        self.playerLabel.grid(row=1, column=2)
        self.pguessLabel.grid(row=2, column=2)
        self.winnerLabel.grid(row=8, column=0, columnspan=3)


run = LizardSpock(window)

window.mainloop()
