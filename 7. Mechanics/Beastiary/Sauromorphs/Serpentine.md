---
statblock: true
name: 'Serpentine'
image: ![[Serpentine.jpg]]
size: Medium
type: Humanoid
alignment: Neutral
cr: 4
ac: 16
hp: 58
hit_dice: '9d8 + 18'
speed: '40 ft., climb 40 ft.'
stats:
    - 14
    - 20
    - 16
    - 12
    - 16
    - 14
senses: 'darkvision 60 ft., passive Perception 13'
languages: 'Common, Draconic'
saves:
    - { dexterity: 7 }
    - { constitution: 5 }
skillsaves:
    - { stealth: 9 }
    - { acrobatics: 9 }
actions:
    - { name: Multiattack, desc: 'The serpentine makes two melee attacks, one with its bite and one with its claws.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d6 + 5) piercing damage plus 7 (2d6) poison damage.' }
    - { name: Claw, desc: 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d4 + 5) slashing damage.' }
straits:
    - { name: 'Stealth Mastery', desc: 'The serpentine has advantage on Dexterity (Stealth) checks and can take the Hide action as a bonus action.' }
    - { name: 'Venomous', desc: 'The serpentine’s bite attack deals additional poison damage (included in the attack).' }
---
```statblock
monster: Serpentine
```