class Snack:
    def __init__(self, calories: int):
        self.calories = int(calories)

    def __repr__(self):
        return f'Snack with {self.calories} calories'


class Elve:
    def __init__(self, snacks: list[Snack]):
        self.snacks = snacks
        self.total_calories = sum([snack.calories for snack in snacks])

    def add_snack(self, snack: Snack):
        self.snacks.append(snack)
        self.total_calories += snack.calories

    def __repr__(self):
        return f'Elve - {self.total_calories} total calories'
