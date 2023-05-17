---
statblock: true
name: 'Peryton - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Monstrosity
cr: 2
ac: 13
hp: 34
hit_dice: '4d10 + 12'
speed: '30 ft., fly 60 ft.'
stats:
    - 16
    - 16
    - 16
    - 10
    - 12
    - 12
damage_resistances: 'damage from nonmagical weapons'
skillsaves:
    - { perception: 3 }
senses: 'passive Perception 13'
languages: "understands Common and Sylvan but can't speak"
traits:
    - { name: 'Keen Sight and Smell', desc: 'The peryton has advantage on Perception checks that rely on sight or smell.' }
actions:
    - { name: Multiattack, desc: 'The peryton attacks with its gore and talons.' }
    - { name: Gore, desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage. This attack scores a critical hit on a roll of 18, 19, or 20. If this critical hit reduces a humanoid to 0 hit points, the peryton can use a bonus action to rip the target's heart out with its teeth, killing it." }
    - { name: Talons, desc: 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage, or 10 (2d6 + 3) damage if the peryton moves at least 20 feet straight towards the target before the attack.' }
combat:
    - { name: 'The peryton dives at humanoid prey', desc: "It continues fighting in melee until it rips out a creature's heart, and then flies away with the heart." }

---
```statblock
monster: Peryton - A5E
```
