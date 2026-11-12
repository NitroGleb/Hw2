class Character:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Здоровье: {self.health}")
        print(f"Уровень: {self.level}")

    def attack(self):
        print(f"{self.name} атакует противника!")

class Mage(Character):
    def __init__(self, name, health, level, mana):
        super().__init__(name, health, level)
        self.mana = mana

    def cast_spell(self):
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.name} использует магический огненный шар!")
            print("Противник получает 50 урона!")
        else:
            print("Недостаточно маны!")

    def show_mana(self):
        print(f"Мана: {self.mana}")

mage = Mage("Артур", 100, 5, 60)

mage.show_info()
mage.show_mana()
mage.attack()
mage.cast_spell()
mage.show_mana()