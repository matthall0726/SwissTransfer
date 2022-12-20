import os
import platform
import webbrowser
# from tkinter import *
import customtkinter
from PIL import Image


class App(customtkinter.CTk):
    """Container for the Swiss Application"""

    def __init__(self):
        customtkinter.CTk.__init__(self)
        self.title("Swiss Transfer")
        self.geometry("950x750")
        self.minsize(400, 300)
        self.resizable(False, False)
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        # create a grid layout
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(7, weight=0)
        self.frames = {}

        for page in (LandingPage, HomePage):
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LandingPage)

    def show_frame(self, content):
        frame = self.frames[content]
        frame.tkraise()


class LandingPage(customtkinter.CTkFrame):
    """Login Page for the Swiss Transfer Application"""

    def __init__(self, parent, controller): # TODO implement controller for switching to the home page
        customtkinter.CTkFrame.__init__(self, parent)
        customtkinter.set_appearance_mode("system")

        product_name_label = customtkinter.CTkLabel(master=self, text="Swiss Transfer ®")
        product_name_label.grid(row=0, column=7, pady=10)

        space_label = customtkinter.CTkLabel(master=self, text="")
        space_label.grid(row=1, column=0, padx=25)

        label_username = customtkinter.CTkLabel(master=self, text="Username")
        label_username.grid(row=1, column=1, padx=0, pady=15, sticky="n")

        textbox_username = customtkinter.CTkEntry(self, width=100, height=5)
        textbox_username.grid(row=1, column=2, sticky="n", padx=5, pady=20)

        label_password = customtkinter.CTkLabel(master=self, text="Password", )
        label_password.grid(row=1, column=3, padx=5, pady=15, sticky="n")
        textbox_password = customtkinter.CTkEntry(self, width=100, height=5, show="*")
        textbox_password.grid(row=1, column=4, sticky="n", padx=5, pady=20)

        label_password = customtkinter.CTkLabel(master=self, text="Domain")
        label_password.grid(row=1, column=5, padx=5, pady=15, sticky="n")

        # need to change domain name to something else @Matthew
        # textbox_password = customtkinter.CTkEntry(self, width=100, height=5)
        # textbox_password.grid(row=1, column=6, sticky="n", padx=5, pady=20)

        def login_button():
            """ This function is responsible for logging into the SSH Server using username and password fields"""

            system_info = platform.system().lower()
            uname = textbox_username.get()
            password = textbox_password.get()

            if system_info.__contains__("linux"):  # Detects if the user is running the application from linux
                terminal_command = "sshpass -p \"{0}\" ssh -o StrictHostKeyChecking=no {1}@swisstransfer.net"
                terminal_command = terminal_command.format(password, uname)
                os.system(terminal_command)
                # TODO implement a way to check if the user has been authenticated then destroy the landing page will
                #  be destroyed -> self.destroy()

            elif system_info.__contains__("mac os"):  # TODO needs to correctly detect os x (mac)
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

        login_button = customtkinter.CTkButton(
            master=self,
            text="Login", fg_color="grey",
            text_color="white",
            hover_color="#404040",
            command=login_button
        )
        login_button.grid(row=1, column=7, sticky="n", padx=10, pady=18)

        # Login Image
        # Creates a CTkImage and then
        # appends it to the button where
        # it gets filled to the size of the
        # image

        # my_image = customtkinter.CTkImage(light_image=Image.open("CTk Frame/Transfer Photo-850x330.jpeg"),
        #                                   dark_image=Image.open("CTk Frame/Transfer Photo-850x330.jpeg"),
        #                                   size=(800, 330))

        # For Michael
        my_image = customtkinter.CTkImage(
            light_image=Image.open(
                "/home/paradox/PycharmProjects/SwissTransfer/Swiss Transfer/CTk Frame/Transfer Photo-850x330.jpeg"),
            dark_image=Image.open(
                "/home/paradox/PycharmProjects/SwissTransfer/Swiss Transfer/CTk Frame/Transfer Photo-850x330.jpeg"
            ),
            size=(800, 330))

        login_image = customtkinter.CTkButton(master=self, image=my_image, text="", hover=False, fg_color="#404040")
        login_image.grid(row=2, column=1, columnspan=7)

        # Help Label
        # Redirects user from client
        # to helpful webpage explaining
        # how ssh works

        url = "https://www.a2hosting.com/kb/getting-started-guide/accessing-your-account/using-ssh-secure-shell"

        def open_url(this_url):
            webbrowser.open(this_url)
            print("button pressed")

        help_button_spacing = customtkinter.CTkLabel(master=self, text="")
        help_button_spacing.grid(row=3, column=0, padx=25)
        help_button = customtkinter.CTkButton(master=self, text="Help", command=lambda a_url=url: open_url(a_url))
        help_button.grid(row=3, column=7, pady=15)


class HomePage(customtkinter.CTkFrame):
    """This page purpose is to allow users to send and receive files on their system"""

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)


if __name__ == "__main__":
    app = App()
    app.mainloop()
