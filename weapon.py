from random import choices


# ------------ class setup ------------
class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 damage: int,
                 value: int
                 ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.base_damage = damage
        self.value = value
    def damgae(self) -> int:
        self.damage =choices(list(weapon_damage_weights[self.name].keys()), weights=list(weapon_damage_weights[self.name].values()), k=1)[0]
        return self.damage     


# ------------ object creation ------------
fists = Weapon(name="Fists",weapon_type="blunt",damage=5,value=0)
Iron_Sword=Weapon(name='Iron Sword', weapon_type= 'melee', damage= 8, value=  10)
Steel_Axe = Weapon(name= 'Steel Axe', weapon_type= 'melee', damage= 8, value =  12)
Silver_Dagger = Weapon(name= 'Silver Dagger', weapon_type='melee', damage= 5, value= 16)
Short_Bow=Weapon(name= 'Short Bow', weapon_type= 'ranged', damage= 6, value= 15)
Longbow=Weapon(name= 'Longbow', weapon_type= 'ranged', damage= 8, value= 19)
Crossbow= Weapon(name= 'Crossbow', weapon_type= 'ranged', damage= 9, value= 20)
Magic_Staff=Weapon(name= 'Magic Staff', weapon_type= 'magic', damage= 9, value= 23)
Fire_Wand=Weapon(name= 'Fire Wand', weapon_type= 'magic', damage= 7, value= 17)
Ice_Staff=Weapon(name= 'Ice Staff', weapon_type= 'magic', damage= 8, value= 16)
Thunder_Rod=Weapon(name= 'Thunder Rod', weapon_type= 'magic', damage= 8, value= 19)

weapon_damage_weights={'Fists': {2: 10, 3: 10, 4: 10, 5: 70, 6: 20, 7: 20}, 'Iron Sword': {5: 10, 6: 30, 7: 45, 8: 50, 9: 10, 10: 5}, 'Steel Axe': {5: 10, 6: 10, 7: 10, 8: 70, 9: 20, 10: 20}, 'Silver Dagger': {2: 10, 3: 10, 4: 10, 5: 70, 6: 20, 7: 20}, 'Short Bow': {3: 10, 4: 10, 5: 10, 6: 70, 7: 20, 8: 20}, 'Longbow': {5: 10, 6: 10, 7: 10, 8: 70, 9: 20, 10: 20}, 'Crossbow': {6: 10, 7: 10, 8: 10, 9: 70, 10: 20, 11: 20}, 'Magic Staff': {6: 10, 7: 10, 8: 10, 9: 70, 10: 20, 11: 20}, 'Fire Wand': {4: 10, 5: 10, 6: 10, 7: 70, 8: 20, 9: 20}, 'Ice Staff': {5: 10, 6: 10, 7: 10, 8: 70, 9: 20, 10: 20}, 'Thunder Rod': {5: 10, 6: 10, 7: 10, 8: 70, 9: 20, 10: 20}}