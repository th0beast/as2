from abc import ABC, abstractmethod
import random

class Combatant(ABC):
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    @abstractmethod
    def attack(self, other):
        pass

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health} HP"

class Warrior(Combatant):
    def attack(self, other):
        damage = self.attack_power
        other.take_damage(damage)

class Mage(Combatant):
    def attack(self, other):
        damage = self.attack_power + random.randint(0, 5)
        other.take_damage(damage)

class Archer(Combatant):
    def attack(self, other):
        damage = self.attack_power - 2 + random.randint(0, 4)
        other.take_damage(damage)
