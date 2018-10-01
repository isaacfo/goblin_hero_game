


class Hero():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, goblin):
        goblin.health -= self.power
        print("You do %d damage to the goblin." % self.power)
        if goblin.health <= 0:
            print("The goblin is dead.")
    def alive(self):
         if self.health <= 0:
            return False
         else:
            return True
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))



class Goblin():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does %d damage to you." % self.power)
        if hero.health <= 0:
          print("You are dead.")
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))


def main():
    Guy = Hero(10, 5)
    Ugly_thing = Goblin(6,2)

    while Ugly_thing.alive() and Guy.alive():
        Guy.print_status()
        Ugly_thing.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
           Guy.attack(Ugly_thing)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if Ugly_thing.alive():
            # Goblin attacks hero
           Ugly_thing.attack(Guy)

main()