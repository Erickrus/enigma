class Rotor:   
    def __init__(self, 
        name, 
        encoding,
        rotorPosition,
        notchPosition,
        ringSetting,
        overrideIsAtNotch = False
    ):
        self.name = name
        self.forwardWiring = self.decode_wiring(encoding)
        self.backwardWiring = self.inverse_wiring(self.forwardWiring)
        self.rotorPosition = rotorPosition
        self.notchPosition = notchPosition
        self.ringSetting = ringSetting
        self.overrideIsAtNotch = overrideIsAtNotch
    
    @staticmethod
    def create(name, rotorPosition, ringSetting):
        if name == "I":
            return Rotor("I","EKMFLGDQVZNTOWYHXUSPAIBRCJ", rotorPosition, 16, ringSetting)
        elif name == "II":
            return Rotor("II","AJDKSIRUXBLHWTMCQGZNPYFVOE", rotorPosition, 4, ringSetting)
        elif name == "III":
            return Rotor("III","BDFHJLCPRTXVZNYEIWGAKMUSQO", rotorPosition, 21, ringSetting)
        elif name == "IV":
            return Rotor("IV","ESOVPZJAYQUIRHXLNFTGKDCMWB", rotorPosition, 9, ringSetting)
        elif name == "V":
            return Rotor("V","VZBRGITYUPSDNHLXAWMJQOFECK", rotorPosition, 25, ringSetting)
        elif name == "VI":
            return Rotor("VI","JPGVOUMFYQBENHZRDKASXLICTW", rotorPosition, 0, ringSetting, True)
        elif name == "VII":
            return Rotor("VII","NZJHGRCXMYSWBOUFAIVLPEKQDT", rotorPosition, 0, ringSetting, True)
        elif name == "VIII":
                return Rotor("VIII","FKQHTLXOCBJSPDZRAMEWNIUYGV", rotorPosition, 0, ringSetting, True)
        else:
            return Rotor("Identity","ABCDEFGHIJKLMNOPQRSTUVWXYZ", rotorPosition, 0, ringSetting)

    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.rotorPosition
    
    @staticmethod
    def decode_wiring(encoding):
        charWiring = encoding
        wiring = []
        for i in range(len(charWiring)):
            wiring.append(ord(charWiring[i]) - 65)
        return wiring

    @staticmethod
    def inverse_wiring(wiring):
        inverse = list(range(len(wiring)))
        for i in range(len(wiring)):
            forward = wiring[i]
            inverse[forward] = i
        return inverse
    
    @staticmethod # protected static int
    def encipher(k, pos, ring, mapping):
        shift = pos - ring
        return (mapping[(k + shift + 26) % 26] - shift + 26) % 26
    
    def forward(self, c):
        return Rotor.encipher(c, self.rotorPosition, self.ringSetting, self.forwardWiring)
    
    def backward(self, c):
        return Rotor.encipher(c, self.rotorPosition, self.ringSetting, self.backwardWiring)
    

    def is_at_notch(self):
        if self.overrideIsAtNotch:
            return self.rotorPosition == 12 or self.rotorPosition == 25
        else:
            return self.notchPosition == self.rotorPosition

    def turnover(self):
        self.rotorPosition = (self.rotorPosition + 1) % 26