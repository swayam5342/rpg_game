# ------------ imports ------------
import os
from charactor import Hero, Enemy
from weapon import Iron_Sword,Short_Bow,Silver_Dagger,Crossbow

# ------------ setup ------------


hero = Hero(name="Hero", health=100)
hero.equip(Iron_Sword)
enemy = Enemy(name="Enemy", health=100, weapon=Crossbow)

def main():
    with open('data.txt', '+a') as f:
        while True:
            os.system("cls")
            hero.attack(enemy)
            enemy.attack(hero)
            print(hero.health, enemy.health)
            f.write(f'{hero.health}  {enemy.health} \n')
            if enemy.health == 0:
                print("You  Won")
                input(">")
                f.write("round end you won \n")
                break
            if hero.health == 0:
                print("You  Lost")
                input(">")
                f.write("round end you lost \n ")
                break
            input(">")


if __name__ == '__main__':
    main()
