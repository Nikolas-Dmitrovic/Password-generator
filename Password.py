import random

class password:
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = ["@", "#", "$", "%"]

    def __init__(self, passwordLength):
        self.passwordLength = passwordLength
        self.uppercase = True
        self.numbers = True
        self.symbols = True

    def lowercase(self):
        if self.uppercase:
            self.uppercase = False
        else:
            return

    def uppercase(self):
        if not self.uppercase:
            self.uppercase = True
        else:
            return

    def disableNumbers(self):
        if self.numbers:
            self.numbers = True
        else:
            return

    def enableNumbers(self):
        if not self.numbers:
            self.numbers = True
        else:
            return

    def disableSymbols(self):
        if self.symbols:
            self.symbols = True
        else:
            return

    def enableSymbols(self): 
        if not self.symbols:
            self.symbols = True
        else:
            return

    def genorator(self):
        passwordcontents = []

        try:
            val = int(self.passwordLength)
            print("Input is an integer number. Number = ", val)
        except ValueError:
            try:
                val = float(self.passwordLength)
                print("Input is a float  number. Number = ", val)
            except ValueError:
                print("No.. input is not a number. It's a string")

        count = 0

        while count != val:
            count += 1

            pick = random.randrange(4)
            print(pick)
            if pick == 0:
                character = random.choice(password.letters)
            if pick == 1:
                if self.uppercase:
                    character = random.choice(password.letters)
                    character = character.upper()
                else:
                    character = None
            if pick == 2:
                if self.numbers:
                    character = random.choice(password.numbers)
                else:
                    character = None
            if pick == 3:
                if self.symbols:
                    character = random.choice(password.symbols)
                else:
                    character = None

            if character == None:
                count -= 1
            if character != None:
                passwordcontents.append(character)

        passwordcontents = ','.join(str(x) for x in passwordcontents)
        return (passwordcontents.replace(',', ''))

