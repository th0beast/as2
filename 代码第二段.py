class Arena:
    def __init__(self, combatants):
        self.combatants = combatants

    def start_battle(self):
        print("The battle begins!")
        while len([c for c in self.combatants if c.is_alive()]) > 1:
            for combatant in self.combatants:
                if combatant.is_alive():
                    opponent = random.choice([c for c in self.combatants if c != combatant and c.is_alive()])
                    print(f"{combatant.name} attacks {opponent.name}!")
                    combatant.attack(opponent)
                    print(opponent)
                    if not opponent.is_alive():
                        print(f"{opponent.name} has been defeated!")
        winner = [c for c in self.combatants if c.is_alive()][0]
        print(f"The winner is {winner.name}!")

if __name__ == "__main__":
    warrior = Warrior("Warrior", 100, 10, 5)
    mage = Mage("Mage", 80, 12, 3)
    archer = Archer("Archer", 90, 8, 4)
    arena = Arena([warrior, mage, archer])
    arena.start_battle()
