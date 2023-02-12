import sys
import paramiko

"""
author's    Michael Waller
            Mathew Hall
"""


class Client:

    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()

    def connect(self, args):
        #  TODO: Cover all exceptions
        if len(args) < 2:
            raise Exception("Not enough arguments")
        self.client.connect(hostname="swisstransfer.net", port=22, username=args[1], password=args[2], auth_timeout=5)

        fileTransfer = self.client.open_sftp() #  opens channel for transferring files
        fileTransfer.put("/home/paradox/PycharmProjects/SwissTransfer/ServerSocket/test.txt", "home/test.txt")

if __name__ == "__main__":
    client = Client()
    client.connect(sys.argv)
    print("")


