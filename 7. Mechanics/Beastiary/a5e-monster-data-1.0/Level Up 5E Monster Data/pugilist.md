---
statblock: true
name: 'Pugilist - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Humanoid
cr: 4
ac: 14
hp: 75
hit_dice: '10d8 + 30'
speed: '40 ft.'
stats:
    - 16
    - 14
    - 16
    - 10
    - 14
    - 10
saves:
    - { strength: 5 }
    - { dexterity: 4 }
skillsaves:
    - { athletics: 5 }
    - { intimidation: 2 }
senses: 'passive Perception 12'
languages: 'any one'
traits:
    - { name: 'Unarmored Defense', desc: "The pugilist's AC equals 10 + their Dexterity modifier + their Wisdom modifier." }
actions:
    - { name: Multiattack, desc: 'The pugilist attacks three times with their fists.' }
    - { name: Fists, desc: 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage.' }
reactions:
    - { name: 'Opportune Jab', desc: 'If a creature attempts to grapple the pugilist, the pugilist attacks that creature with their fists.' }
    - { name: 'Pugilists include skilled boxers, wrestlers, and pit fighters', desc: "They sometimes work as bodyguards or gangsters, though they're most often found in the ring, challenging all comers." }
'bonus actions':
    - { name: 'Haymaker (1/Day)', desc: 'The pugilist attacks with their fists. On a hit, the attack deals an extra 7 (2d6) damage.' }
    - { name: 'Head Shot (1/Day)', desc: "The pugilist attacks with their fists. On a hit, the target makes a DC 13 Constitution saving throw. On a failure, it is stunned until the end of the pugilist's next turn." }

---
```statblock
monster: Pugilist - A5E
```
