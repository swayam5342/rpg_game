from random import choices


# ------------ class setup ------------
class Weapon:
    def __init__(self,
                name: str,
                weapon_type: str,
                damage: int,
                value: int,
                DamageWeights:dict
                ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.base_damage = damage
        self.value = value
        self.weapon_damage_weights = DamageWeights

    def damgae(self) -> int:
        """Calculates the actual damage for an attack."""
        if not hasattr(self, 'weapon_damage_weights'):
            raise AttributeError("weapon_damage_weights not defined for weapon")
        damage_options = list(self.weapon_damage_weights.keys())
        damage_weights = list(self.weapon_damage_weights.values())
        actual_damage = choices(damage_options, weights=damage_weights)[0]
        return self.base_damage + actual_damage



# ------------ object creation -----------

fists = Weapon(name="Fists",weapon_type="blunt",damage=5,DamageWeights={0:0.7,1:0.5,2:0.2,3:0.1},value=0)
Quarterstaff = Weapon(name='Quarterstaff',	weapon_type='Melee (Two-Handed)',damage=11,DamageWeights={9: 0.4, 10: 0.4, 11: 0.2}, value=	100)
Flail=Weapon(name='Flail',weapon_type='Melee (Two-Handed)',damage=10,DamageWeights={8: 0.4, 9: 0.4, 10: 0.2},value=120)
Trident=Weapon(name='Trident',weapon_type='Melee (Two-Handed)',damage=9,DamageWeights={7: 0.4, 8: 0.4, 9: 0.2},value=	80)
Katana=Weapon(name='Katana',weapon_type='Melee (One-Handed)',damage=8,DamageWeights={7: 0.6, 8: 0.3, 9: 0.1},value=	150)
Wakizashi=Weapon(name='Wakizashi',weapon_type='Melee (One-Handed)',damage=6,DamageWeights={5: 0.6, 6: 0.3, 7: 0.1},value=	70)
Curved_Dagger=Weapon(name='Curved Dagger',weapon_type='Melee (One-Handed)',damage=5,DamageWeights={4: 0.7, 5: 0.2, 6: 0.1},value=	40)
Scimitar=Weapon(name='Scimitar',weapon_type='Melee (One-Handed)',damage=7,DamageWeights={6: 0.6, 7: 0.3, 8: 0.1},value=	200)
Battle_Axe=Weapon(name='Battle Axe',weapon_type='Melee (Two-Handed)',damage=14,DamageWeights={12: 0.4, 13: 0.4, 14: 0.2},value=	200)
Warhammer=Weapon(name='Warhammer',weapon_type='	Melee (Two-Handed)',damage=	15,DamageWeights={13: 0.4, 14: 0.4, 15: 0.2},value=	220)
Hunting_Bow=Weapon(name='Hunting Bow',weapon_type='	Ranged',damage=	8,DamageWeights={7: 0.5, 8: 0.4, 9: 0.1},value=	120)
Longbow_elven=Weapon(name='Longbow (elven)',weapon_type='	Ranged',damage=	11,DamageWeights={9: 0.4, 10: 0.4, 11: 0.2},value=	250)
Crossbow_Repeating=Weapon(name='Crossbow (Repeating)',weapon_type='	Ranged',damage=	9,DamageWeights={8: 0.5, 9: 0.4, 10: 0.1},value=	180)
Sling=Weapon(name='Sling (Improved)',weapon_type='	Ranged',damage=	6,DamageWeights={5: 0.6, 6: 0.3, 7: 0.1},value=	60)
Staff=Weapon(name='Staff (Healing)',weapon_type='	Magic',damage=	4,DamageWeights={3: 0.6, 4: 0.3, 5: 0.1},value=	15)
Iron_Sword=Weapon(name='Iron Sword	',weapon_type='Melee (One-Handed)',damage=	8,DamageWeights={7: 0.6, 8: 0.3, 9: 0.1},value=	50)
Broadsword=Weapon(name='Broadsword',weapon_type='	Melee (Two-Handed)',damage=	12,DamageWeights={10: 0.4, 11: 0.4, 12: 0.2, 13: 0.05},value=	100)
War_Axe=Weapon(name='War Axe',weapon_type='	Melee (Two-Handed)',damage=	15,DamageWeights={13: 0.3, 14: 0.5, 15: 0.2},value=	120)
Dagger=Weapon(name='Dagger',weapon_type='Melee (One-Handed)',damage=	5,DamageWeights={4: 0.7, 5: 0.2, 6: 0.1},value=	20)
Hunting_Bow=Weapon(name='Hunting Bow',weapon_type='	Ranged',damage=	7,DamageWeights={6: 0.6, 7: 0.3, 8: 0.1},value=	70)
Longbow=Weapon(name='Longbow',weapon_type='Ranged',damage=	10,DamageWeights={8: 0.4, 9: 0.4, 10: 0.2, 11: 0.05}	,value=150)
Crossbow=Weapon(name='Crossbow',weapon_type='Ranged',damage=	8,DamageWeights={7: 0.5, 8: 0.4, 9: 0.1},value=	80)
Club=Weapon(name='Club',weapon_type='Melee (One-Handed)',damage=7,DamageWeights={6: 0.6, 7: 0.3, 8: 0.1},value=	30)
Mace=Weapon(name='Mac',weapon_type='Melee (One-Handed)',damage=	9,DamageWeights={8: 0.5, 9: 0.4, 10: 0.1},value=	40)
Spear=Weapon(name='Spear',weapon_type='	Melee (Two-Handed)',damage=	10,DamageWeights={8: 0.4, 9: 0.4, 10: 0.2, 11: 0.05},value=	80)
Staff=Weapon(name='Staff',weapon_type=' (Basic) Magic',damage=6,DamageWeights={5: 0.6, 6: 0.3, 7: 0.1},value=	60)
Short=Weapon(name='Short',weapon_type=' Staff (Fire)	Magic',damage=	5, DamageWeights={4: 0.5, 5: 0.4, 6: 0.1} ,value=	100)
Whip=Weapon(name='Whip',weapon_type='	Melee (One-Handed)',damage=	4,DamageWeights={3: 0.7, 4: 0.2, 5: 0.1} ,value=	25)
Scimitar=Weapon(name='Scimitar',weapon_type='	Melee (One-Handed)',damage=	7,DamageWeights={6: 0.6, 7: 0.3, 8: 0.1} 	,value=80)
Battle_Axe=Weapon(name='Battle Axe',weapon_type='	Melee (Two-Handed)',damage=	13,DamageWeights={11: 0.4, 12: 0.4, 13: 0.2},value=	150)
Warhammer=Weapon(name='Warhammer',weapon_type='	Melee (Two-Handed)',damage=	14,DamageWeights={12: 0.4, 13: 0.4, 14: 0.2},value=	180)
Hunting_Knife=Weapon(name='Hunting Knife',weapon_type='	Melee (One-Handed)',damage=	6,DamageWeights={5: 0.6, 6: 0.3, 7: 0.1},value=	30)
Throwing_Axe=Weapon(name='Throwing Axe',weapon_type='	Ranged',damage=	8,DamageWeights={7: 0.5, 8: 0.4, 9: 0.1},value=	50)
Shortsword=Weapon(name='Shortsword',weapon_type='	Melee (One-Handed)',damage=	9,DamageWeights={8: 0.5, 9: 0.4, 10: 0.1},value=	90)
Rapier=Weapon(name='Rapier',weapon_type='	Melee (One-Handed)',damage=	7,DamageWeights={6: 0.4, 7: 0.4, 8: 0.2} ,value=	120)
Steel_Axe = Weapon(name= 'Steel Axe', weapon_type= 'melee', damage= 8, DamageWeights={6: 0.6, 7: 0.3, 8: 0.1},value =  12)
Silver_Dagger = Weapon(name= 'Silver Dagger', weapon_type='melee', DamageWeights={6: 0.6, 7: 0.3, 8: 0.1},damage= 5, value= 16)
Short_Bow=Weapon(name= 'Short Bow', weapon_type= 'ranged', damage= 6, DamageWeights={4: 0.7, 5: 0.2, 6: 0.1},value= 15)
Magic_Staff=Weapon(name= 'Magic Staff', weapon_type= 'magic', damage= 9,DamageWeights={4: 0.7, 5: 0.2, 6: 0.1}, value= 23)
Fire_Wand=Weapon(name= 'Fire Wand', weapon_type= 'magic', damage= 7, DamageWeights={4: 0.5, 5: 0.4, 6: 0.1},value= 17)
Ice_Staff=Weapon(name= 'Ice Staff', weapon_type= 'magic', damage= 8,DamageWeights={4: 0.7, 5: 0.2, 6: 0.1}, value= 16)
Thunder_Rod=Weapon(name= 'Thunder Rod', weapon_type= 'magic', damage= 8, DamageWeights={4: 0.7, 5: 0.2, 6: 0.1},value= 19)