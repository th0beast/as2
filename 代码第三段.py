class Field:
    def __init__(self, type):
        self.type = type

    def apply_effect(self, combatant):
        if self.type == "forest":
            combatant.defense += 2
        elif self.type == "desert":
            combatant.attack_power += 2

if __name__ == "__main__":
    warrior = Warrior("Warrior", 100, 10, 5)
    mage = Mage("Mage", 80, 12, 3)
    archer = Archer("Archer", 90, 8, 4)
    forest = Field("forest")
    forest.apply_effect(warrior)
    forest.apply_effect(mage)
    forest.apply_effect(archer)
    arena = Arena([warrior, mage, archer])
    arena.start_battle()
