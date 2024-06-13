import random
import time
f = open('elden.txt', 'r')
file_contents = f.read()
print (file_contents)
f.close()
class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, enemy):
        print(f"{self.name} атакует {enemy.name}.")
        time.sleep(1)


        critical = random.random() < 0.3
        damage = 20 if not critical else 40

        enemy.health -= damage
        if enemy.health <= 0:
            print(f"{enemy.name} проиграл! Победил {self.name}.")
            time.sleep(1)
            return False

        print(f"{'Критический урон! ' if critical else ''}У {enemy.name} осталось {enemy.health} здоровья.")
        time.sleep(1)
        return True

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health = min(100, self.health + heal_amount)
        print(f"{self.name} восстанавливает себе {heal_amount} здоровья. Теперь у него {self.health} здоровья.")
        time.sleep(1)

warrior1 = Warrior("Погасшая душа")
warrior2 = Warrior("Древо эледен")

while warrior1.health > 0 and warrior2.health > 0:
    attacker = random.choice([warrior1, warrior2])
    enemy = warrior2 if attacker == warrior1 else warrior1


    if random.random() < 0.2:
        attacker.heal()
    else:
        if not attacker.attack(enemy):
            break

    time.sleep(1)

