import random
import time


class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.attacks = {
            "Обычная атака": random.randint(15, 25),
            "Сильный удар": random.randint(20, 30),
            "Критический удар": random.randint(25, 40),
            "Точный выстрел": random.randint(10, 35)
        }

    def perform_attack(self):
        attack_name, attack_power = random.choice(list(self.attacks.items()))
        return attack_name, attack_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")
        self.round_num = 1

    def show_health(self):
        print(f"\n{self.player.name}: {self.player.health} HP  |  {self.computer.name}: {self.computer.health} HP")
        print("-" * 40)

    def perform_round(self, attacker, defender):
        print(f"\nРаунд {self.round_num}:")
        attack_name, attack_power = attacker.perform_attack()

        print(f"{attacker.name} использует '{attack_name}' и наносит {attack_power} урона!")
        defender.take_damage(attack_power)

        self.show_health()
        self.round_num += 1
        time.sleep(1.5)

    def start(self):
        print("\n⚔️ Начинается Битва Героев! ⚔️")
        print(f"{self.player.name} vs {self.computer.name}")
        print("=" * 40)

        # Определяем кто атакует первым случайным образом
        current_attacker = self.player if random.choice([True, False]) else self.computer

        while self.player.is_alive() and self.computer.is_alive():
            defender = self.computer if current_attacker == self.player else self.player
            self.perform_round(current_attacker, defender)
            current_attacker = defender

        self.declare_winner()

    def declare_winner(self):
        print("\n" + "=" * 40)
        if self.player.is_alive():
            print(f"🎉 {self.player.name} побеждает! Поздравляем! 🎉")
        else:
            print(f"☠️ {self.computer.name} побеждает. Попробуйте еще раз! ☠️")
        print("=" * 40)


if __name__ == "__main__":
    print("🔥 Добро пожаловать в игру 'Битва Героев'! 🔥")
    while True:
        game = Game()
        game.start()

        play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
        if play_again != 'да':
            print("\nСпасибо за игру! До встречи!")
            break