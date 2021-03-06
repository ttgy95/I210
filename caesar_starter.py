from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.title_lbl = Label(self, text = "Caesar Cipher Encoder")
        self.title_lbl.grid()
        
        self.key_lbl = Label(self, text = "Key: ")
        self.key_lbl.grid()

        self.key_ent = Entry(self)
        self.key_ent.insert(0,"0")
        self.key_ent.grid()

        self.plaintext = Text(self, width = 50, height = 5, wrap = WORD)
        self.plaintext.grid()

        self.submit_bttn = Button(self, text = "Encode", command = self.encode)
        self.submit_bttn.grid()

        self.ciphertext = Text(self, width = 50, height = 5, wrap = WORD)
        self.ciphertext.grid()

    def caesar(self, letter, key):
        """ letter is a single text character, and key is an integer"""
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in alpha:
            if self.letter==alpha[i]:
                alpha[i+key]
                self.key=int(key)
            else:
                print("Can't encode")


        #alpha is a string containing all the lowercase letters in English.

        #you can use the index position of the letter, together with the key
        #to compute the new letter

        #Newlines and other punctuation should be ignored, so check for that
        

    def encode(self):
        #you need to get the text out of the plaintext box

        #send it through the caesar method

        #and output it to the ciphertext box

        #remember, pass is just here so this will execute while empty
        pass

# main
root = Tk()
root.title("Caeser Cipher")
root.geometry("410x270")
root.resizable(width = TRUE, height = TRUE)

app = Application(root)
root.mainloop()
