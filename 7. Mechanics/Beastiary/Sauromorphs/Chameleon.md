---
statblock: true
name: 'Chameleon'
image: ![[Chameleon.jpg]]
size: Medium
type: Humanoid
alignment: Neutral
cr: 3
ac: 15
hp: 52
hit_dice: '8d8 + 16'
speed: '30 ft., climb 30 ft.'
stats:
    - 16
    - 18
    - 14
    - 12
    - 14
    - 16
senses: 'darkvision 60 ft., passive Perception 12'
languages: 'Common, Draconic'
saves:
    - { dexterity: 6 }
    - { constitution: 4 }
skillsaves:
    - { stealth: 8 }
    - { acrobatics: 8 }
actions:
    - { name: Multiattack, desc: 'The chameleon makes two melee attacks.' }
    - { name: Claw, desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage.' }
straits:
    - { name: 'Shapechanger', desc: 'The chameleon can use its action to polymorph into a humanoid it has seen, or back into its true form. Its statistics, apart from its size, are the same in each form.' }
    - { name: 'Camouflage', desc: 'The chameleon has advantage on Dexterity (Stealth) checks made to hide.' }
---
```statblock
monster: Chameleon
```