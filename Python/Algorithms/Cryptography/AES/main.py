#!/usr/bin/env python3

""" Implementation of Advanced Encryption Standard (AES-128)
    P.S - Found this code from my college assignment submissions
"""

__version__ = "2.0.0"

from binascii import unhexlify
from os import path
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from Algorithms.Cryptography.AES.aes_block import AESBlock


class TkGui:
    def __init__(self, master):
        self.master = master
        master.title("AES Encryptor/Decryptor")
        self.selected = IntVar()
        self.var = StringVar()
        self.var.set("Choose option")
        self.file = self.file2 = None
        self.plaintext = None
        self.ciphertext = None

        self.mainframe = Frame(self.master)
        self.topFrame = Frame(self.master)
        self.midFrame = Frame(self.master)
        self.bottomFrame = Frame(self.master)
        self.mainframe.pack()

        option = OptionMenu(self.mainframe, self.var, "Encryption", "Decryption", command=self.select_method)
        option.pack()

        self.choices = []
        self.choices.append(Radiobutton(self.topFrame, text="128-bit", value=1, variable=self.selected))
        self.choices.append(Radiobutton(self.topFrame, text="196-bit", value=2, variable=self.selected,
                                        state=DISABLED))
        self.choices.append(Radiobutton(self.topFrame, text="256-bit", value=3, variable=self.selected,
                                        state=DISABLED))

        self.txt1 = Label(self.midFrame, text="Plaintext: ")
        self.ptext_entry = Entry(self.midFrame, width=100)
        self.browse_btn = Button(self.midFrame, text="Browse", command=self.browse_choice)
        self.txt2 = Label(self.midFrame, text="Key: ")
        self.key_entry = Entry(self.midFrame, width=100)
        self.encrypt_btn = Button(self.midFrame, text="Encrypt!", command=self.aes_encrypt)

        self.txt3 = Label(self.midFrame, text="Ciphertext: ")
        self.ctext_entry = Entry(self.midFrame, width=100)
        self.browse_btn2 = Button(self.midFrame, text="Browse", command=self.browse_choice2)
        self.txt4 = Label(self.midFrame, text="Key: ")
        self.key_entry2 = Entry(self.midFrame, width=100)
        self.decrypt_btn = Button(self.midFrame, text="Decrypt!", command=self.aes_decrypt)

        self.help_button = Button(self.bottomFrame, text="Help ?", command=self.help)

    def aes_encrypt(self):
        self.plaintext = None
        self.encryption_choice = self.selected.get()
        key_size = 128
        if self.encryption_choice == 2:
            key_size = 196
        elif self.encryption_choice == 3:
            key_size = 256
        self.key = self.key_entry.get()
        if self.key == "":
            self.aes = AESBlock(type=key_size)
            self.key = self.aes.key.val
            self.key_entry.delete(0, END)
            self.key_entry.insert(0, hex(self.key))
            self.key_entry.configure(state=DISABLED)
        else:
            self.aes = AESBlock(key=self.key, type=key_size)

        if self.file is not None:
            if path.getsize(self.file) > 10000000:
                if not messagebox.askyesno("Warning!",
                                           "Input file exceeds 10KB and encryption might take time. Do you want to proceed?"):
                    self.ptext_entry.configure(state=NORMAL)
                    self.ptext_entry.delete(0, END)
                    self.key_entry.configure(state=NORMAL)
                    return
            with open(self.file, 'rb') as f:
                file_content = f.read()
            self.plaintext = file_content
            self.ciphertext = self.aes.encrypt(self.plaintext)
            with open(self.file + '.crypt', 'wb') as f:
                f.write(unhexlify(hex(self.ciphertext.val)[2:]))
            self.on_closing()
            return

        self.plaintext = self.ptext_entry.get().strip()
        if self.plaintext == "":
            raise Exception
        elif self.plaintext[0] == '"' or self.plaintext[0] == "'":
            self.plaintext = self.plaintext[1:-1]
        elif self.plaintext[:2].lower() == "0x":
            self.plaintext = int(self.plaintext, base=16)
        self.ciphertext = self.aes.encrypt(self.plaintext)

        if self.file is None:
            self.showresult = Toplevel(self.master)
            self.showresult.title = "Result"
            Label(self.showresult, text=self.ciphertext.__repr__()).pack()
            self.showresult.protocol("WM_DELETE_WINDOW", self.on_closing)

    def aes_decrypt(self):
        self.ciphertext = None
        self.encryption_choice = self.selected.get()
        key_size = 128
        if self.encryption_choice == 2:
            key_size = 196
        elif self.encryption_choice == 3:
            key_size = 256
        self.key2 = self.key_entry2.get()
        if self.key2 == "":
            self.aes = AESBlock(type=key_size)
            self.key2 = self.aes.key.val
            self.key_entry2.delete(0, END)
            self.key_entry2.insert(0, hex(self.key2))
            self.key_entry2.configure(state=DISABLED)
        else:
            self.aes = AESBlock(key=self.key, type=key_size)

        if self.file2 is not None:
            if path.getsize(self.file2) > 10000000:
                if not messagebox.askyesno("Warning!",
                                           "Input file exceeds 10KB and decryption might take time. Do you want to proceed?"):
                    self.key_entry2.configure(state=NORMAL)
                    self.ctext_entry.configure(state=NORMAL)
                    self.ctext_entry.delete(0, END)
                    return
            with open(self.file2, 'rb') as f:
                file_content = f.read()
            self.ciphertext = file_content
            self.plaintext = self.aes.decrypt(self.ciphertext)
            if self.file2[-6:] == ".crypt":
                self.file2 = self.file2[:-6]
            else:
                self.file2 += ".decrypt"
            with open(self.file2, 'wb') as f:
                f.write(unhexlify(hex(self.plaintext.val)[2:]))
            self.on_closing()
            return

        self.ciphertext = self.ctext_entry.get().strip()
        if self.ciphertext == "":
            raise Exception
        elif self.ciphertext[0] == '"' or self.ciphertext[0] == "'":
            self.ciphertext = self.ciphertext[1:-1]
        elif self.ciphertext[:2].lower() == "0x":
            self.ciphertext = int(self.ciphertext, base=16)
        self.plaintext = self.aes.decrypt(self.ciphertext)

        if self.file2 is None:
            self.showresult = Toplevel(self.master)
            self.showresult.title = "Result"
            Label(self.showresult, text=self.plaintext.__repr__()).pack()
            self.showresult.protocol("WM_DELETE_WINDOW", self.on_closing)

    def browse_choice(self):
        self.file = filedialog.askopenfilename()
        self.ptext_entry.configure(state=NORMAL)
        self.ptext_entry.delete(0, END)
        self.ptext_entry.insert(0, self.file)
        self.ptext_entry.configure(state=DISABLED)

    def browse_choice2(self):
        self.file2 = filedialog.askopenfilename()
        self.ctext_entry.configure(state=NORMAL)
        self.ctext_entry.delete(0, END)
        self.ctext_entry.insert(0, self.file2)
        self.ctext_entry.configure(state=DISABLED)

    def select_method(self, *args):
        self.topFrame.pack()
        self.midFrame.pack()
        for self.choice in self.choices:
            self.choice.pack(side=LEFT)
        if self.var.get() == "Encryption":
            self.txt1.pack()
            self.ptext_entry.pack(side=TOP, padx=2, pady=2, anchor=W)
            self.browse_btn.pack(padx=2, pady=2)
            self.txt2.pack()
            self.key_entry.pack(padx=2, pady=2)
            self.encrypt_btn.pack(padx=2, pady=5)
        else:
            self.txt3.pack()
            self.ctext_entry.pack(side=TOP, padx=2, pady=2, anchor=W)
            self.browse_btn2.pack(padx=2, pady=2)
            self.txt4.pack()
            self.key_entry2.pack(padx=2, pady=2)
            self.decrypt_btn.pack(padx=2, pady=5)
        self.bottomFrame.pack()
        self.help_button.pack(side=BOTTOM)

    def help(self):
        self.help_box = Toplevel(self.master)
        var1 = "Input formats: "
        var2 = "You can give your input (plaintext/ciphertext) in hexadecimal. " \
               "Example : 0x0123456789abcdeffedcba9876543210"
        var3 = "You can give your input (plaintext/ciphertext) as a string (include quotes). " \
               "Example: \"Save yourself!\""
        var4 = "You can encrypt or decrypt a file by hitting the browse button. " \
               "This will disable other modes of input"
        var5 = "Key must be in hexadecimal form with no spaces in between."
        Label(self.help_box, text=var1).pack()
        Label(self.help_box, text=var2).pack()
        Label(self.help_box, text=var3).pack()
        Label(self.help_box, text=var4).pack()
        Label(self.help_box, text=var5).pack()

    def on_closing(self):
        self.ctext_entry.configure(state=NORMAL)
        self.ptext_entry.configure(state=NORMAL)
        self.file = self.file2 = None
        self.key_entry.configure(state=NORMAL)
        self.key_entry2.configure(state=NORMAL)
        self.showresult.destroy()


# Usage examples
if __name__ == "__main__":
    root = Tk()
    gui = TkGui(root)
    root.mainloop()

    ######################################################
    #### Uncomment below code to run default examples ####
    ######################################################
    # # Input format 1: Plaintext = String, random key
    # print("{:-^40}".format("Input 1"))
    # plaintext = "Save yourself"
    # aes = AESBlock()
    # aes.display_key()
    # ciphertext = aes.encrypt(plaintext)
    # print("Plain-text: {}".format(aes.plaintext))
    # print("Cipher-text: {}".format(ciphertext))
    # recovered_text = aes.decrypt(ciphertext.val)
    # print(recovered_text)

    # # Input format 2: Plaintext = Hex integer, key specified
    # print("{:-^40}".format("Input 2"))
    # plaintext = 0x0123456789abcdeffedcba9876543210
    # aes = AESBlock(0x0f1571c947d9e8590cb7add6af7f6798)
    # aes.display_key()
    # cipher = aes.encrypt(plaintext)
    # print("Plain-text: {:#x}".format(aes.plaintext.val))
    # aes.matrix_print(aes.bytes_to_matrix(aes.plaintext.val))
    # print("Cipher-text: {:#x}".format(cipher.val))
    # aes.matrix_print(aes.bytes_to_matrix(cipher.val))
    # recovered_text = aes.decrypt(cipher.val)
    # print(recovered_text)

    # # Input format 3: Plaintext = File contents, key specified
    # print("{:-^40}".format("Input 3"))
    # path = "requirements.txt"
    # with open(path, 'rb') as f:
    #     file_content = f.read()
    # plaintext = file_content
    # aes = AESBlock(0x0e1571c947d9e8590cb7add6af7f6798)
    # aes.display_key()
    # cipher = aes.encrypt(plaintext)
    # with open(path + '.crypt', 'wb') as f:
    #     f.write(unhexlify(hex(cipher.val)[2:]))
    # ## Do not uncomment below lines if size of plaintext is huge
    # # print("Plain-text: {}".format(aes.plaintext), end='\n')
    # # print("Cipher-text: {}".format(cipher))
