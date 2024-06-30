import unittest

class TestCombatant(unittest.TestCase):
    def test_warrior_attack(self):
        warrior = Warrior("Warrior", 100, 10, 5)
        mage = Mage("Mage", 80, 12, 3)
        warrior.attack(mage)
        self.assertEqual(mage.health, 73)

    def test_mage_attack(self):
        mage = Mage("Mage", 80, 12, 3)
        archer = Archer("Archer", 90, 8, 4)
        mage.attack(archer)
        self.assertTrue(archer.health < 82 and archer.health >= 78)

    def test_archer_attack(self):
        archer = Archer("Archer", 90, 8, 4)
        warrior = Warrior("Warrior", 100, 10, 5)
        archer.attack(warrior)
        self.assertTrue(warrior.health < 97 and warrior.health >= 93)

if __name__ == "__main__":
    unittest.main()
