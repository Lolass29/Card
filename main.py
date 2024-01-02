class Card:

    def __init__(self, suit, number, weight=None):
        self.suit = suit
        self.number = number
        self.weight = weight

    def __repr__(self):
        return (f" ------------\n"
                f"| {self._format_value(self.number)}        {self._format_mark(self.suit)} |\n"
                f"|            |\n"
                f"|            |\n"
                f"|            |\n"
                f"| {self._format_mark(self.suit)}        {self._format_value(self.number)} |\n"
                f" ------------\n")

    def _format_mark(self, mark):
        if mark == "Bubna":
            return "♦"
        elif mark == "Сross":
            return "♣"
        elif mark == "Сhirwa":
            return "♥"
        elif mark == "Peak":
            return "♠"

    def _format_value(self, value):
        if value == 1:
            return 'A'
        elif value == 11:
            return 'J'
        elif value == 12:
            return 'Q'
        elif value == 13:
            return 'K'
        else:
            return str(value)

    def sum_card(sum1, sum2):
        return sum1.number + sum2.number


one_card = Card('Bubna', 6)
print(one_card)

two_card = Card('Bubna', 7)
print(two_card)

sum_card = Card.sum_card(one_card, two_card)
print(sum_card)