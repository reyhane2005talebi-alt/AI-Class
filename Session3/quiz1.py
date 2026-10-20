class Character:
    def --init--(self, name, power, health, coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1

    def show_info(self):
        print(f"{self.name} | Level: {self.level} | Power: {self.power} | Health: {self.health} | Coins: {self.coins}")

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        other.health -= self.power
        print(f"{self.name} attacked {other.name}. {other.name}'s health: {other.health}")

    def earn_coins(self, amount):
        self.coins += amount

    def buy_potion(self):
        if self.coins >= 20:
            self.coins -= 20
            self.health += 30
        else:
            print("Not coins")

    def level_up(self):
        self.level += 1
        self.power += 5
        print(f"{self.name} level {self.level} New power: {self.power}")


chrac1 = Character("Arya", 10, 100, 50)
chrac2 = Character("Bran", 8, 100, 30)

chrac1.attack(chrac2)
chrac2.attack(chrac1)
chrac1.attack(chrac2)
chrac1.attack(chrac2)

chrac1.buy_potion()

chrac2.level_up()

chrac1.show_info()
chrac2.show_info()


