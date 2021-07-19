from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

class Enigma:
    def __init__(self,
        rotors,
        reflector,
        rotorPositions,
        ringSettings,
        plugboardConnections
    ):
        # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        # A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
        self.leftRotor = Rotor.create(rotors[0], rotorPositions[0], ringSettings[0])
        self.middleRotor = Rotor.create(rotors[1], rotorPositions[1], ringSettings[1])
        self.rightRotor = Rotor.create(rotors[2], rotorPositions[2], ringSettings[2])
        self.reflector = Reflector.create(reflector)
        self.plugboard = Plugboard(plugboardConnections)

    @staticmethod
    def init_by_key(key):
        return Enigma(key.rotors, "B", key.indicators, key.rings, key.plugboard)

    def rotate(self):
        # If middle rotor notch - double-stepping
        if (self.middleRotor.is_at_notch()):
            self.middleRotor.turnover()
            self.leftRotor.turnover()
        # If left-rotor notch
        elif (self.rightRotor.is_at_notch()):
            self.middleRotor.turnover()

        # Increment right-most rotor
        self.rightRotor.turnover()

    def encrypt(self, c):
        self.rotate()

        # Plugboard in
        c = self.plugboard.forward(c)

        # Right to left
        c1 = self.rightRotor.forward(c)
        c2 = self.middleRotor.forward(c1)
        c3 = self.leftRotor.forward(c2)

        # Reflector
        c4 = self.reflector.forward(c3)

        # Left to right
        c5 = self.leftRotor.backward(c4)
        c6 = self.middleRotor.backward(c5)
        c7 = self.rightRotor.backward(c6)

        # Plugboard out
        c7 = self.plugboard.forward(c7)

        return c7
    
    def encrypt_ch(self, c):
        return chr(self.encrypt(ord(c) - 65) + 65)
    

    def encrypt_text(self, text):
        output = []
        for i in range(len(text)):
            output.append(self.encrypt_ch(text[i]))
        return output
   
if __name__ == "__main__":
    print(
"""This is an Enigma machine, written by Eric 2021
This code based on Mike Pound's github repository:
https://github.com/mikepound/enigma
It is rewritten in pure Python code

Let's set the key for enigma machine as followings:
e = Engima(
    ["VII", "V", "IV"], "B", 
    [10,5,12], [1,2,3],
    "AD FT WH JO PN"
    )

Please input your text to process: """)

    e = Enigma(
        ["VII", "V", "IV"], 
        "B", 
        [10,5,12], 
        [1,2,3], 
        "AD FT WH JO PN"
    )

    #text = "HELLO WORLD"
    text = input().upper()
    print("\nFollowing is the output from Enigma Machine:")
    texts = text.split(" ")
    for t in texts:
        print(t, "".join(e.encrypt_text(t)))


