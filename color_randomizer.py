from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.configure(background = "light grey")
root.title("Color Randomizer")

label = Label(root, text = "Text")
label.place(relx = 0.5, rely = 0.2, anchor = CENTER)


class randomizer():
    
    def __init__(self):
        self.__score = 0
        
    def updateGame(self):
        self.text = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE"]
        self.random_num = random.randint(0,5)
        self.color = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.color_random = random.randint(0,5)
        
        label["text"] = self.text[self.random_num]
        label["fg"] - self.color[self.color_random]
        
random = randomizer()
      
btn = Button(root, text = "Randomize", command = random.updateGame)
btn.place(relx = 0.5, rely = 0.3, anchor = CENTER)

root.mainloop()
    