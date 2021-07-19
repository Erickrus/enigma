class EnigmaKey:
    def __init__(self, 
        rotors, 
        indicators, 
        rings, 
        plugboardConnections
    ):
        if rotors == None:
            self.rotors ["I", "II", "III"]
        else:
            self.rotors = rotors

        if indicators == None:
            self.indicators = [0,0,0]
        else:
            self.indicators = indicators

        if rings == None:
            self.rings = [0,0,0]
        else:
            self.rings = rings

        if plugboardConnections ==None:
            self.plugboard = ""
        else:
            self.plugboard = plugboardConnections