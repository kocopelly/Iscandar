---
statblock: true
name: 'Marilith - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Fiend
cr: 16
ac: 18
hp: 220
hit_dice: '21d10 + 105'
speed: '40 ft.'
stats:
    - 20
    - 22
    - 20
    - 20
    - 18
    - 20
damage_resistances: 'cold, fire, lightning; damage from nonmagical weapons'
damage_immunities: poison
condition_immunities: poisoned
saves:
    - { strength: 10 }
    - { dexterity: 11 }
    - { constitution: 10 }
    - { wisdom: 9 }
    - { charisma: 10 }
senses: 'truesight 120 ft., passive Perception 14'
languages: 'Abyssal, telepathy 120 ft.'
traits:
    - { name: 'Chaotic Evil', desc: 'The marilith radiates a Chaotic and Evil aura.' }
    - { name: 'Magic Resistance', desc: 'The marilith has advantage on saving throws against spells and magical effects.' }
actions:
    - { name: Multiattack, desc: 'The marilith makes six attacks with its longswords.' }
    - { name: Longsword, desc: 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) slashing damage.' }
reactions:
    - { name: 'Reactive Teleport', desc: 'When the marilith is hit or missed by a ranged attack, it uses Teleport. If it teleports within 5 feet of a creature, it can attack with its tail.' }
'bonus actions':
    - { name: Tail, desc: 'Melee Weapon Attack: +10 to hit, reach 10 ft., one creature. Hit: 10 (2d4 + 5) bludgeoning damage, and the target is grappled (escape DC 19).' }
    - { name: Teleport, desc: 'The marilith magically teleports up to 120 feet to an unoccupied space it can see.' }
combat:
    - { name: 'The marilith starts combat by engaging the strongest melee opponent, focusing its attacks against that enemy', desc: 'It uses its tail to prevent its enemy from retreating. If troubled by ranged attacks, the marilith uses Reactive Teleport to move next to the ranged attacker and grapple them, so that it can attack the target with its longswords on its next turn. If reduced to 55 hit points or fewer, it uses Teleport to escape.' }

---
```statblock
monster: Marilith - A5E
```
