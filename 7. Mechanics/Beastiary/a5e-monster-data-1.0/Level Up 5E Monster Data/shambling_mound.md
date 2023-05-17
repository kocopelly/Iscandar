---
statblock: true
name: 'Shambling Mound - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Plant
cr: 6
ac: 15
hp: 123
hit_dice: '13d10 + 52'
speed: '20 ft., swim 20 ft.'
stats:
    - 18
    - 10
    - 18
    - 6
    - 12
    - 6
damage_resistances: 'cold, fire, piercing'
damage_immunities: lightning
condition_immunities: 'blinded, deafened, fatigue'
skillsaves:
    - { stealth: 3 }
senses: 'blindsight 60 ft. (blind beyond this radius), passive Perception 11'
traits:
    - { name: 'Lightning Absorption', desc: 'When the shambling mound would be subjected to lightning damage, it instead regains hit points equal to the lightning damage dealt.' }
actions:
    - { name: Multiattack, desc: 'The shambling mound takes two slam attacks. If both attacks hit one Medium or smaller creature, the target is grappled (escape DC 15), and the shambling mound uses Engulf against it.' }
    - { name: Slam, desc: 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage.' }
    - { name: Engulf, desc: "The shambling mound absorbs a Medium or smaller grappled creature into its body. The engulfed creature is blinded, restrained, can't breathe, and moves with the shambling mound. At the start of each of the shambling mound's turns, the target takes 11 (2d6 + 4) bludgeoning damage." }
combat:
    - { name: 'The shambling mound can rarely catch fleeing enemies, so it tries to attack from hiding', desc: 'It makes both its slam attacks against a single creature and then Engulfs that opponent. If reduced to 30 hit points or fewer, it wilts and pretends to be dead.' }

---
```statblock
monster: Shambling Mound - A5E
```
