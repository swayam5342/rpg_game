#from healthbar import HealthBar
from weapon import Weapon,fists ,Iron_Sword ,Steel_Axe ,Silver_Dagger ,Short_Bow ,Longbow,Crossbow ,Magic_Staff ,Fire_Wand ,Ice_Staff,Thunder_Rod

class Character:
    def __init__(self, name : str, health : int) -> None:
        self.name:str = name
        self.health: int = health
        self.health_max :int  = health
        self.weapon : Weapon = fists


    def attack(self, target) -> None:
        self.damage = self.weapon.damgae()
        target.health -= self.damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.weapon.damage} damage to "
            f"{target.name} with {self.weapon.name}")


    def equip(self, weapon : Weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")


    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon


    def switch_weapon(self):
        print(''' List of available weapons
            1 : fists
            2 : Iron_Sword
            3 : Steel_Axe
            4 : Silver_Dagger
            5 : Short_Bow
            6 : Longbow
            7 : Crossbow
            8 : Magic_Staff
            9 : Fire_Wand
            10 : Ice_Staff
            11 : Thunder_Rod''')
        li_of_weapon = {
            1: fists,
            2: Iron_Sword,
            3: Steel_Axe,
            4: Silver_Dagger,
            5: Short_Bow,
            6: Longbow,
            7: Crossbow,
            8: Magic_Staff,
            9: Fire_Wand,
            10: Ice_Staff,
            11: Thunder_Rod
        }
        wea = int(input('select the weapon no.'))
        selected_weapon = li_of_weapon.get(wea, fists)  # Default to fists if input is invalid
        print(selected_weapon)
        self.equip(selected_weapon)


class Hero(Character):
    def __init__(self,
                name: str,
                health: int
                ) -> None:
        super().__init__(name=name, health=health)
        self.default_weapon = self.weapon

class Enemy(Character):
    def __init__(self,
                name: str,
                health: int,
                weapon,
                ) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon

