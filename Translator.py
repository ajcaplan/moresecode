from time import sleep
from winsound import Beep
from tkinter import *

class app(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        # Convert to Morse code
        self.detail = Label(self, text = "Letters to Morse Code:", borderwidth = 1, relief = "solid", padx = 3) # Section name
        self.detail.grid(row = 0, column = 0, columnspan = 2, sticky = W, padx = 3)
        
        self.instruction = Label(self, text = "Enter Letters................") # Input instruction
        self.instruction.grid(row = 1, column = 0, columnspan = 2, sticky = W, padx = 3)
        
        self.input = Entry(self) # Input box
        self.input.grid(row = 1, column = 1, sticky = W)
        
        self.submit_button = Button(self, text = "Convert", command = self.toMorse, padx = 10) # Convert button
        self.submit_button.grid(row = 3, column = 0, sticky = W, padx = 3)
        
        self.text = Text(self, width = 35, height = 5, wrap = WORD) # Output area
        self.text.grid(row = 2, column = 0, columnspan = 2, sticky = W, padx = 3)

        self.play = Button(self, text = "Play", command = self.read, padx = 5) # Button for beeps
        self.play.grid(row = 4, column = 0, sticky = W, padx = 3)

        # Convert to normal letters
        self.detail = Label(self, text = "Morse Code to Letters:", borderwidth = 1, relief = "solid", padx = 3) # Section name
        self.detail.grid(row = 0, column = 3, columnspan = 2, sticky = W, padx = 10)
        
        self.instruction2 = Label(self, text = "Enter morse code.........") # Input instruction
        self.instruction2.grid(row = 1, column = 3, columnspan = 2, sticky = W, padx = 10, pady = 2)
        
        self.engPut = Entry(self) # Input box
        self.engPut.grid(row = 1, column = 4, sticky = W, padx = 10, pady = 3)
        
        self.submit = Button(self, text = "Convert", command = self.toEng, padx = 10) # Convert button
        self.submit.grid(row = 3, column = 3, sticky = W, padx = 10)
        
        self.out = Text(self, width = 35, height = 5, wrap = WORD) # Output area
        self.out.grid(row = 2, column = 3, columnspan = 2, sticky = W, padx = 10, pady = 3)

        self.space = Label(self, text = "Input '/' for space") # Additional detail
        self.space.grid(row = 3, column = 4, columnspan = 2, sticky = W, padx = 10)
        
    def toMorse(self): # Convert normal text to morse code
        morse = list(".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- /".split(" "))
        ab = list("abcdefghijklmnopqrstuvwxyz1234567890 ")
        s = self.input.get() # Get contents of input box
        new = ""
        inval = False
        invals = []
        for i in s:
            if i not in ab:
                invals.append(i)
                inval = True
        self.text.delete(0.0, END)
        if len(invals) == 1:
            self.text.insert(0.0, "Invalid character: " + invals[0])
        elif len(invals) > 1:
            msg = "Invalid characters: "
            for i in invals:
                msg += i + ", "
            self.text.insert(0.0, msg[0: len(msg)-2])

        if inval == False:
            for i in s:
                for x in ab:
                    if i == x:
                        if s.index(i) != len(s) - 1:
                            new += morse[ab.index(x)] + " "
                        else: # So pointless space not added at end
                            new += morse[ab.index(x)]
            self.text.delete(0.0, END) # Remove text from previous conversion from output area
            self.text.insert(0.0, new) # Replace with new morse code in output area

    def read(self): # Beep morse code
        new = self.text.get(0.0, END) # Get morse code to play out
        for i in new:
            if i == ".":
                Beep(1000,200)
            elif i == "-":
                Beep(1000, 500)
            elif i == "/":
                sleep(0.6)
            else:
                sleep(0.4)

    def toEng(self): # Convert morse code to normal letters
        morse = list(".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- /".split(" "))
        ab = list("abcdefghijklmnopqrstuvwxyz1234567890 ")
        s = self.engPut.get().split(" ") # Get morse code from input box
        new = ""

        inval = False
        invals = []
        for i in s:
            for x in i:
                if x not in morse:
                    invals.append(x)
                    inval = True
        self.out.delete(0.0, END)
        if len(invals) == 1:
            self.out.insert(0.0, "Invalid character: " + invals[0])
        elif len(invals) > 1:
            msg = "Invalid characters: "
            for i in invals:
                msg += i + ", "
            self.out.insert(0.0, msg[0: len(msg)-2])

        if inval == False:
            for i in s:
                if i == "/":
                    new += " "
                else:
                    for x in morse:
                        if i == x:
                            new += ab[morse.index(x)]
            self.out.delete(0.0, END) # Remove text from previous conversion from output area
            self.out.insert(0.0, new) # Replace with new normal letters in output area

# Interface setup
root = Tk()
root.title("Morse Code Translator")
root.geometry("590x200")
app = app(root)
root.mainloop()
