class Cart:

    def __init__(self):
        self._contents = dict()

    def __repr__(self):
        return "{0} {1}".format(Cart, self.__dict__)

    def process (self, order):
        if order.add:
            if not order.item in self._contents:
                self._contents[order.item] = 0
            self._contents[order.item] += 1
        elif order.delete:
            if order.item in self._contents:
                self._contents[order.item] -= 1
                if self._contents[order.item] <= 0:
                    del   self._contents[order.item]

    def list_content(self):
        for key, val in self._contents.items():
            print(val, key)

class Order:
    def __init__(self):
        self.add = False
        self.delete = False
        self.quit = False
        self.item = None

    def get_input(self):
        print ("[command] [item] (command a -add d -delete q - quit)")
        line = input()

        command = line[:1]
        self.item = line[2:]

        if command == "a":
            self.add = True
        elif command == "d":
            self.delete = True
        elif command == "q":
            self.quit = True


cart = Cart ()
order = Order ()

order.get_input()

while not order.quit:
    cart.process(order)
    order = Order ()
    order.get_input()


cart.list_content()
