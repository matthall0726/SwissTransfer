import time
from tkinter import *
import os
from applescript import tell
from PIL import Image, ImageTk
import customtkinter
import webbrowser

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("system")




        self.title("")

        self.geometry("950x750")
        self.resizable(False,False)
        self.minsize(400, 300)

        #create a grid layout
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(7, weight=0)



        productName_label = customtkinter.CTkLabel(master=self, text="Swiss Transfer ®")
        productName_label.grid(row=0,column=7,pady=10)

        space_label = customtkinter.CTkLabel(master=self, text="")
        space_label.grid(row=1,column=0,padx=25)

        label_username = customtkinter.CTkLabel(master=self, text="Username")
        label_username.grid(row=1, column=1, padx=0,pady=15, sticky="n")

        textbox_username = customtkinter.CTkEntry(self, width=100,height=5)
        textbox_username.grid(row=1, column=2, sticky="n", padx=5, pady=20)

        label_password = customtkinter.CTkLabel(master=self, text="Password", )
        label_password.grid(row=1, column=3, padx=5, pady=15, sticky="n")
        textbox_password = customtkinter.CTkEntry(self, width=100, height=5, show="*")
        textbox_password.grid(row=1, column=4, sticky="n", padx=5, pady=20)

        label_password = customtkinter.CTkLabel(master=self, text="Domain")
        label_password.grid(row=1, column=5, padx=5, pady=15, sticky="n")

        textbox_password = customtkinter.CTkEntry(self, width=100, height=5)
        textbox_password.grid(row=1, column=6, sticky="n", padx=5, pady=20)

        def loginbutton():
            print("Button Pressed")
            terminal_command = """ osascript -e '
            
            tell application "Terminal"
                reopen
                activate
                do script "ssh mhall087@swisstransfer.net" in front window
                delay 2
                do script "Mrh0726!." in front window
            end tell
            
            '"""

            os.system(terminal_command)







        login_button = customtkinter.CTkButton(master=self,
                                               text="Login",fg_color="grey",
                                               text_color="white",
                                               hover_color="#404040",
                                               command=loginbutton)
        login_button.grid(row=1, column=7, sticky="n", padx=10, pady=18)

        # Login Image
        # Creates a CTkImage and then
        # appends it to the button where
        # it gets filled to the size of the
        # image
        my_image = customtkinter.CTkImage(light_image=Image.open("CTk Frame/Transfer Photo-850x330.jpeg"),
                                          dark_image=Image.open("CTk Frame/Transfer Photo-850x330.jpeg"),
                                          size=(800, 330))

        login_image = customtkinter.CTkButton(master=self,
                                              image=my_image,
                                              text="",hover=False,
                                              fg_color="#404040")

        login_image.grid(row=2,column=1,columnspan=7)

        # Help Label
        # Redirects user from client
        # to helpful webpage explaining
        # how ssh works

        url = "https://www.a2hosting.com/kb/getting-started-guide/accessing-your-account/using-ssh-secure-shell"
        def OpenUrl(url):
            webbrowser.open(url)
            print("button pressed")
        help_button_spacing = customtkinter.CTkLabel(master=self, text="")
        #help_button_spacing.grid(row=3,column=0,padx=25)

        help_button = customtkinter.CTkButton(master=self, text="Help",command=lambda aurl=url:OpenUrl(aurl))
        help_button.grid(row=3, column=7, pady=15)





if __name__ == "__main__":
    app = App()
    app.mainloop()
