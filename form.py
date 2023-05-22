# Setup
class Character:

    def __init__(self, name, laugh_type):
        self.name = name
        self.laugh_type = laugh_type

    def laugh(self):
        print(f"{self.name}: {self.laugh_type}")


sponge = Character("Spongebob", "Hahahaha")
paper_sponge = Character("Doodlebob", "NEHOY MENOY HOY MENYOY")
crab = Character("Mr. Krabs", "Ar ar ar ar")


# Function calls
sponge.laugh()
paper_sponge.laugh()
crab.laugh()
