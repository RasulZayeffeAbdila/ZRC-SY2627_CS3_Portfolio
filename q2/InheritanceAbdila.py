class PSHS_Galaxy:
    def __init__(self):
        self.name = "PSHS Galaxy"
        self.classification = "All"

    def quote(self):
        return "[Quiet Silence of the Galaxy]"

class Nationality(PSHS_Galaxy):
    def __init__(self):
        super().__init__()
        self.name = "Nationality"
        self.classification = "Nation"
        self.country = "Unknown"

    def quote(self):
        return "Wow im patriotic"

class Alien(PSHS_Galaxy):
    def __init__(self):
        super().__init__()
        self.name = "Alien"
        self.classification = "Undefined"
        self.planet = "Unknown"

    def quote(self):
        return "Zup Zeep Zurp"

class Filipino(Nationality):
    def __init__(self):
        super().__init__()
        self.name = "Filipino"
        self.country = "Philippines"
        self.favorite_food = "Ulam ni mama"

    def quote(self):
        return "Ma! Anong ulam?"

class Indonesian(Nationality):
    def __init__(self):
        super().__init__()
        self.name = "Indonesian"
        self.country = "Indonesia"
        self.favorite_food = "Idk"

    def quote(self):
        return "Berhenti berharap, mulailah bertindak."

class Spaniard(Nationality):
    def __init__(self):
        super().__init__()
        self.name = "Spaniard"
        self.country = "Spain"
        self.favorite_food = "Taco"

    def quote(self):
        return "Viva España!"

class Marvel(Alien):
    def __init__(self):
        super().__init__()
        self.name = "Marvel"
        self.planet = "Earth"
        self.size = "Universe"

    def quote(self):
        return "I am Iron Man [Fingers Snap]"

class Avengers(Alien):
    def __init__(self):
        super().__init__()
        self.name = "Avengers"
        self.planet = "Earth"
        self.size = "Team"

    def quote(self):
        return "ASSSEEMEBLEEE!!!"

everything = [PSHS_Galaxy(), Nationality(), Alien(), Filipino(),
            Indonesian(), Spaniard(), Marvel(), Avengers()]

print("Welcome to the PSHS Galaxy!")
for classes in everything:
    print(f"{classes.name} ({classes.classification}): {classes.quote()}")

print()
for nationality in [Filipino(), Indonesian(), Spaniard()]:
    print(nationality.country, "|", nationality.favorite_food)
