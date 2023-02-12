import socket
import webbrowser
import customtkinter
import paramiko
from PIL import Image


class App(customtkinter.CTk):
    """Container for the Swiss Application"""

    def __init__(self):
        customtkinter.CTk.__init__(self)
        self.title("Swiss Transfer")
        self.geometry("950x750")
        self.minsize(400, 400)

        container = customtkinter.CTkFrame(self)
        container.pack()

        # create a grid layout
        self.grid_rowconfigure(5, weight=0)
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

    def __init__(self, parent, controller):  # TODO implement controller for switching to the home page
        customtkinter.CTkFrame.__init__(self, parent)
        customtkinter.set_appearance_mode("system")

        product_name_label = customtkinter.CTkLabel(master=self, text="Swiss Transfer ®")
        product_name_label.grid(row=0, column=7, pady=10)

        label_username = customtkinter.CTkLabel(master=self, text="Username")
        label_username.grid(row=1, column=1, padx=0, pady=15, sticky="n")

        textbox_username = customtkinter.CTkEntry(self, width=100, height=5)
        textbox_username.grid(row=1, column=2, sticky="n", padx=5, pady=20)

        label_password = customtkinter.CTkLabel(master=self, text="Password")
        label_password.grid(row=1, column=3, padx=5, pady=15, sticky="n")
        textbox_password = customtkinter.CTkEntry(self, width=100, height=5, show="*")
        textbox_password.grid(row=1, column=4, sticky="n", padx=5, pady=20)

        label_password = customtkinter.CTkLabel(master=self, text="Domain: 22")
        label_password.grid(row=1, column=5, padx=5, pady=15, sticky="n")

        def login_button():
            """ This function is responsible for logging into the SSH Server using username and password fields"""
            uname = textbox_username.get()
            password = textbox_password.get()

            try:
                client.connect(hostname="swisstransfer.net",
                               port=22,
                               username=uname,
                               password=password,
                               auth_timeout=5
                               )
                client.open_sftp()  # opens channel for transferring files
                self.destroy()  # destroys login page
            except paramiko.BadHostKeyException:

                print()  # TODO change login error text
            except paramiko.AuthenticationException:
                login_error = customtkinter \
                    .CTkLabel(master=self,
                              text="Could not connect. Try again.",
                              text_color="red")
                login_error.grid(row=0, column=3, columnspan=2, pady=10)
            except paramiko.SSHException:
                print()  # TODO change login error text
            except socket.error:
                print()  # TODO change login error text

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

        my_image = customtkinter.CTkImage(light_image=Image.open("CTk Frame/Transfer Photo-850x330.jpeg"),
                                          dark_image=Image.open("CTk Frame/Transfer Photo-850x330.jpeg"),
                                          size=(800, 330))

        # For Michael
        # my_image = customtkinter.CTkImage(
        #     light_image=Image.open(
        #         "/home/paradox/PycharmProjects/SwissTransfer/Swiss Transfer/CTk Frame/Transfer Photo-850x330.jpeg"),
        #     dark_image=Image.open(
        #         "/home/paradox/PycharmProjects/SwissTransfer/Swiss Transfer/CTk Frame/Transfer Photo-850x330.jpeg"
        #     ),
        #     size=(800, 330))

        login_image = customtkinter.CTkButton(master=self, image=my_image, text="", hover=False, fg_color="#404040")
        login_image.grid(row=3, column=0, columnspan=8, padx=25)

        # Help Label
        # Redirects user from client
        # to helpful webpage explaining
        # how ssh works

        url = "https://www.a2hosting.com/kb/getting-started-guide/accessing-your-account/using-ssh-secure-shell"

        def open_url(this_url):
            webbrowser.open(this_url)
            print("button pressed")

        help_button_spacing = customtkinter.CTkLabel(master=self, text="")
        help_button_spacing.grid(row=4, column=0, padx=25)
        help_button = customtkinter.CTkButton(master=self, text="Help", command=lambda a_url=url: open_url(a_url))
        help_button.grid(row=4, column=7, pady=15)


class HomePage(customtkinter.CTkFrame):
    """This page purpose is to allow users to send and receive files on their system"""

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)


if __name__ == "__main__":
    client = paramiko.SSHClient()  # client connection
    client.load_system_host_keys()
    app = App()
    app.mainloop()
