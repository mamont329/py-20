import random
import time


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("\nНачинается битва героев!")
        print(f"{self.player.name} vs {self.computer.name}")
        print("=" * 30)

        current_attacker = self.player if random.choice([True, False]) else self.computer
        round_num = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {round_num}:")
            time.sleep(1)

            defender = self.computer if current_attacker == self.player else self.player
            current_attacker.attack(defender)

            print(f"У {defender.name} осталось {max(0, defender.health)} здоровья")

            current_attacker = defender
            round_num += 1
            time.sleep(1)

        self.declare_winner()

    def declare_winner(self):
        print("\n" + "=" * 30)
        if self.player.is_alive():
            print(f"{self.player.name} побеждает! Поздравляем!")
        else:
            print(f"{self.computer.name} побеждает. Попробуйте еще раз!")
        print("=" * 30)


if __name__ == "__main__":
    game = Game()
    game.start()