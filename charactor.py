from healthbar import HealthBar
from weapon import Weapon ,fists ,Iron_Sword ,Steel_Axe ,Silver_Dagger ,Short_Bow ,Longbow,Crossbow ,Magic_Staff ,Fire_Wand ,Ice_Staff,Thunder_Rod

class Character:
    def __init__(self, name : str, health : int,color : str) -> None:
        self.name:str = name
        self.health: int = health
        self.health_max :int  = health
        self.weapon : Weapon = fists
        self.color = color

    def attack(self, targets: list) -> None:
        total_damage = self.weapon.damgae()
        self.damage = total_damage // len(targets)  # Divide damage among targets
        for target in targets:
            target.health -= self.damage
            target.health = max(target.health, 0)
            print(f"{self.name} dealt {self.damage} damage to {target.name} with {self.weapon.name}")


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

    def show_health(self):
        health_bar = HealthBar(self, length=20, is_colored=True, color=self.color)
        health_bar.update()
        health_bar.draw()

class Hero(Character):
    def __init__(self,
                name: str,
                health: int,
                color : str = "green"
                ) -> None:
        super().__init__(name=name, health=health,color=color)
        self.default_weapon : Weapon = self.weapon

class Enemy(Character):
    def __init__(self,
                name: str,
                health: int,
                color : str = "red"
                ) -> None:
        super().__init__(name=name, health=health, color=color)
