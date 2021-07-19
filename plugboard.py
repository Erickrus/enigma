class Plugboard:
    def __init__(self, connections):
        self.wiring = self.decode_plugboard(connections)

    @staticmethod
    def non_alpha_split(text):
        res = []
        text = "#"+text
        for i in range(len(text)):
            ch = text[i]
            if ch.isalpha():
                prevCh = text[i-1]
                if prevCh.isalpha():
                    res[-1] += ch
                else:
                    res.append(ch)
        return res

    def forward(self, c):
        return self.wiring[c]
    
    @staticmethod
    def identity_plugboard():
        mapping = []
        for i in range(26):
            mapping.append(i)
        return mapping

    @staticmethod
    def get_unplugged_characters(plugboard):
        unpluggedCharacters = set()
        for i in range(26):
            unpluggedCharacters.add(i)
        
        if plugboard== "":
            return unpluggedCharacters
        
        pairings = Plugboard.non_alpha_split(plugboard)

        # Validate and create mapping
        for pair in pairings:
            c1 = ord(pair[0]) - 65
            c2 = ord(pair[1]) - 65
            unpluggedCharacters.remove(c1)
            unpluggedCharacters.remove(c2)
        
        return unpluggedCharacters
    
    @staticmethod
    def decode_plugboard(plugboard):
        if (plugboard == None or plugboard== ""):
            return Plugboard.identity_plugboard()
        
        pairings = Plugboard.non_alpha_split(plugboard)

        pluggedCharacters = set()
        mapping = Plugboard.identity_plugboard()

        # Validate and create mapping
        for pair in pairings:
            if (len(pair) != 2):
                return Plugboard.identity_plugboard()

            c1 = ord(pair[0]) - 65
            c2 = ord(pair[1]) - 65

            if (c1 in pluggedCharacters or c2 in pluggedCharacters):
                return Plugboard.identity_plugboard()
            
            pluggedCharacters.add(c1)
            pluggedCharacters.add(c2)

            mapping[c1] = c2
            mapping[c2] = c1

        return mapping