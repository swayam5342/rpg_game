# ------------ imports ------------
import os
from charactor import Hero, Enemy
from weapon import Iron_Sword

# ------------ setup ------------


hero = Hero(name="Hero", health=100)
hero.equip(Iron_Sword)
enemy = Enemy(name="Enemy", health=100)
def main() -> None:
    try:
        while  hero.health >= 0 and enemy.health >= 0:
            os.system("cls")
            hero.attack(enemy)
            enemy.attack(hero)
            print(hero.health, enemy.health)
            hero.show_health()
            enemy.show_health()
            if enemy.health == 0:
                print("You  Won")
                input(">")
                break
            if hero.health == 0:
                print("You  Lost")
                input(">")
                break
            r = input("press 1 to change weapon or press any key continue : ")
            if r == '1':
                hero.switch_weapon()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
