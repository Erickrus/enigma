class Reflector:
    def __init__(self, encoding):
        self.forwardWiring = Reflector.decode_wiring(encoding)
    
    @staticmethod
    def create(name):
        if name == "B":
            return Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        elif name == "C":
            return Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
        else:
            return Reflector("ZYXWVUTSRQPONMLKJIHGFEDCBA")

    @staticmethod
    def decode_wiring(encoding):
        charWiring = encoding
        wiring = []
        for i in range(len(charWiring)):
            wiring.append(ord(charWiring[i]) - 65)
        return wiring
    
    def forward(self, c):
        return self.forwardWiring[c]