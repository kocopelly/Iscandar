---
statblock: true
name: 'Raptor'
image: ![[Raptor.jpg]]
size: Medium
type: Humanoid
alignment: Neutral
cr: 3
ac: 15
hp: 58
hit_dice: '9d8 + 18'
speed: '50 ft.'
stats:
    - 16
    - 18
    - 14
    - 12
    - 14
    - 12
senses: 'darkvision 60 ft., passive Perception 12'
languages: 'Common, Draconic'
saves:
    - { dexterity: 6 }
    - { constitution: 4 }
skillsaves:
    - { athletics: 6 }
    - { perception: 4 }
actions:
    - { name: Multiattack, desc: 'The raptor makes two melee attacks with its claws.' }
    - { name: Claw, desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage.' }
straits:
    - { name: 'Keen Senses', desc: 'The raptor has advantage on Wisdom (Perception) checks that rely on sight or hearing.' }
    - { name: 'Pounce', desc: 'If the raptor moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 14 Strength saving throw or be knocked prone.' }
---
```statblock
monster: Raptor
```