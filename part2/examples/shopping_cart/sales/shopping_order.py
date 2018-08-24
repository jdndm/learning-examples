
class Order:
    def __init__(self):
        self.add = False
        self.delete = False
        self.quit = False
        self.status = False
        self.item = None

    def get_input(self):
        print ("[command] [item] (command [a]dd [d]elete [s]tatus [q]uit)")
        line = input()

        command = line[:1]
        self.item = line[2:]

        if command == "a":
            self.add = True
        elif command == "d":
            self.delete = True
        elif command == "s":
            self.status = True
        elif command == "q":
            self.quit = True
