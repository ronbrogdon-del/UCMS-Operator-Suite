"""
Coherence Substrate S = (E, G, C)
"""

class Substrate:
    def __init__(self, E=None, G=None, C=None):
        self.E = E
        self.G = G
        self.C = C

    def as_dict(self):
        return {"E": self.E, "G": self.G, "C": self.C}
