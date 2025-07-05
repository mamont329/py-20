import random
import time


class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.max_health = health
        self.health = health
        # Критические уровни здоровья (можно настроить)
        self.strong_attack_threshold = 0.5  # 50%
        self.bow_attack_threshold = 0.2  # 20%

        self.base_attacks = {
            "Обычная атака": (15, 25),
            "Сильный удар": (20, 30),
            "Критический удар": (25, 40),
            "Выстрел из лука": (10, 35)
        }

    def perform_attack(self):
        attack_name, (min_dmg, max_dmg) = random.choice(list(self.base_attacks.items()))
        current_health_percent = self.health / self.max_health

        # Проверка ограничений для атак
        if attack_name == "Сильный удар" and current_health_percent < self.strong_attack_threshold:
            return f"{self.name} попытался нанести {attack_name}, но слишком ослабел и не смог его сделать", 0

        if attack_name == "Выстрел из лука" and current_health_percent < self.bow_attack_threshold:
            return f"{self.name} попытался натянуть лук, но не смог... лук выпал из рук", 0

        # Если ограничений нет - нормальная атака
        base_power = random.randint(min_dmg, max_dmg)

        # Модификатор от здоровья (чем меньше здоровья, тем слабее атака)
        health_modifier = 0.5 + 0.5 * (self.health / self.max_health)  # от 0.5 до 1.0
        final_power = int(base_power * health_modifier)

        return f"{self.name} использует '{attack_name}'", final_power

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
        elif health_percent > 50:
            return "⚠️ Среднее"
        elif health_percent > 20:
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
        print("-" * 60)

    def perform_round(self, attacker, defender):
        print(f"\n🌀 Раунд {self.round_num}:")

        # Получаем информацию об атаке
        attack_message, attack_power = attacker.perform_attack()

        # Выводим информацию об атаке
        print(attack_message)
        if attack_power > 0:
            print(f"⚡ Наносит {attack_power} урона!")
        else:
            print("Никакого урона!")

        # Применяем урон
        defender.take_damage(attack_power)

        # Показываем состояние здоровья
        self.show_health()
        self.round_num += 1
        time.sleep(1.5)

    def start(self):
        print("\n⚔️" * 10 + " Битва Героев " + "⚔️" * 10)
        print(f"\n{self.player.name} vs {self.computer.name}")
        print("=" * 60)

        # Определяем кто атакует первым
        current_attacker = self.player if random.choice([True, False]) else self.computer

        while self.player.is_alive() and self.computer.is_alive():
            defender = self.computer if current_attacker == self.player else self.player
            self.perform_round(current_attacker, defender)
            current_attacker = defender

        self.declare_winner()

    def declare_winner(self):
        print("\n" + "=" * 60)
        if self.player.is_alive():
            print(f"🎉 Победа! {self.player.name} одержал победу! 🎉")
            print(f"Осталось здоровья: {self.player.health}/{self.player.max_health}")
        else:
            print(f"☠️ Поражение! {self.computer.name} победил! ☠️")
        print("=" * 60)

    def test_branch2(self):
        ...


if __name__ == "__main__":
    print("🔥" * 10 + " Битва Героев " + "🔥" * 10)
    while True:
        game = Game()
        game.start()

        play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
        if play_again != 'да':
            print("\nСпасибо за игру! До новых встреч!")
            break

    def test_branch():
        ...