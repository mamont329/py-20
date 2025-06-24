import random
import time


class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.max_health = health
        self.health = health
        self.base_attacks = {
            "Обычная атака": (15, 25),
            "Сильный удар": (20, 30),
            "Критический удар": (30, 45),
            "Точный выстрел": (10, 35)
        }

    def get_health_multiplier(self):
        """Возвращает множитель силы атаки в зависимости от здоровья"""
        health_percent = self.health / self.max_health
        # Чем меньше здоровья, тем слабее атака (но не менее 50% силы)
        return max(0.5, health_percent * 0.7 + 0.3)

    def perform_attack(self):
        attack_name, (min_dmg, max_dmg) = random.choice(list(self.base_attacks.items()))

        # Базовая сила атаки
        base_power = random.randint(min_dmg, max_dmg)

        # Модификатор от здоровья
        health_modifier = self.get_health_multiplier()

        # Шанс на "ярость" при низком здоровье (20% шанс если здоровье < 30%)
        fury_chance = 0.2 if self.health < self.max_health * 0.3 else 0
        is_fury = random.random() < fury_chance

        if is_fury:
            attack_name = "Яростный " + attack_name.lower()
            health_modifier *= 1.5  # Усиление атаки в ярости

        final_power = int(base_power * health_modifier)

        return attack_name, final_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def get_health_status(self):
        health_percent = self.health / self.max_health * 100
        if health_percent > 70:
            return "✅ Отличное"
        elif health_percent > 40:
            return "⚠️ Среднее"
        elif health_percent > 15:
            return "❗ Низкое"
        else:
            return "☠️ Критическое"


class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")
        self.round_num = 1

    def show_health(self):
        print(f"\n{self.player.name}: {self.player.health} HP ({self.player.get_health_status()})")
        print(f"{self.computer.name}: {self.computer.health} HP ({self.computer.get_health_status()})")
        print("-" * 50)

    def perform_round(self, attacker, defender):
        print(f"\n🌀 Раунд {self.round_num}:")

        # Получаем информацию об атаке
        attack_name, attack_power = attacker.perform_attack()

        # Выводим информацию об атаке
        print(f"{attacker.name} использует '{attack_name}'!")
        time.sleep(0.5)
        print(f"⚡ Наносит {attack_power} урона!")

        # Применяем урон
        defender.take_damage(attack_power)

        # Показываем состояние здоровья
        self.show_health()
        self.round_num += 1
        time.sleep(1.5)

    def start(self):
        print("\n⚔️" * 10 + " Битва Героев " + "⚔️" * 10)
        print(f"\n{self.player.name} vs {self.computer.name}")
        print("=" * 50)

        # Определяем кто атакует первым
        current_attacker = self.player if random.choice([True, False]) else self.computer

        while self.player.is_alive() and self.computer.is_alive():
            defender = self.computer if current_attacker == self.player else self.player
            self.perform_round(current_attacker, defender)
            current_attacker = defender

        self.declare_winner()

    def declare_winner(self):
        print("\n" + "=" * 50)
        if self.player.is_alive():
            print(f"🎉 Победа! {self.player.name} одержал победу! 🎉")
            print(f"Осталось здоровья: {self.player.health}/{self.player.max_health}")
        else:
            print(f"☠️ Поражение! {self.computer.name} победил! ☠️")
        print("=" * 50)


if __name__ == "__main__":
    print("🔥" * 10 + " Битва Героев " + "🔥" * 10)
    while True:
        game = Game()
        game.start()

        play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
        if play_again != 'да':
            print("\nСпасибо за игру! До новых встреч!")
            break