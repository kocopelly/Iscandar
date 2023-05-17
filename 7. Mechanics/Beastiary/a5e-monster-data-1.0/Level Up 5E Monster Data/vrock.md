---
statblock: true
name: 'Vrock - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Fiend
cr: 6
ac: 15
hp: 104
hit_dice: '11d10 + 44'
speed: '40 ft., fly 60 ft.'
stats:
    - 18
    - 16
    - 18
    - 8
    - 14
    - 10
damage_resistances: 'cold, fire, lightning; damage from nonmagical weapons'
damage_immunities: poison
condition_immunities: poisoned
saves:
    - { dexterity: 6 }
    - { intelligence: 2 }
    - { wisdom: 5 }
    - { charisma: 3 }
senses: 'darkvision 120 ft., passive Perception 12'
languages: 'Abyssal, telepathy 120 ft.'
traits:
    - { name: 'Chaotic Evil', desc: 'The vrock radiates a Chaotic and Evil aura.' }
    - { name: 'Magic Resistance', desc: 'The vrock has advantage on saving throws against spells and magical effects.' }
actions:
    - { name: Multiattack, desc: 'The vrock attacks with its beak and its talons.' }
    - { name: Beak, desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage. If the vrock has advantage on the attack roll, it deals an additional 7 (2d6) damage.' }
    - { name: Talons, desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 14 (2d10 + 3) slashing damage.' }
    - { name: 'Spores (1/Day)', desc: 'A 15-foot-radius cloud of spores emanates from the vrock, spreading around corners. Each creature in the area makes a DC 14 Constitution saving throw, becoming poisoned for 1 minute on a failure. While poisoned in this way, the target takes ongoing 5 (1d10) poison damage. The target repeats the saving throw at the end of each of its turns, ending the effect on itself on a success.' }
'bonus actions':
    - { name: 'Stunning Screech (1/Day)', desc: "The vrock screeches. Each non-demon creature within 20 feet that can hear it makes a DC 14 Constitution saving throw. On a failure, it is stunned until the end of the vrock's next turn." }
combat:
    - { name: 'The vrock uses Stunning Screech early in the battle to ground flying enemies', desc: 'It attacks a stunned enemy with its beak and talons. It uses Spores when it is within range of three or more foes (ignoring devil foes, which are immune to its spores). The vrock retreats only if ordered to by a more powerful demon.' }

---
```statblock
monster: Vrock - A5E
```
