class Card:
    def __init__(self, value, color="rainbow", special_state="None"):
        self.color = color
        self.value = value

    def __repr__(self):
        if self.color == "rainbow":
            return f"{self.value}"
        return f"{self.color} {self.value}"
