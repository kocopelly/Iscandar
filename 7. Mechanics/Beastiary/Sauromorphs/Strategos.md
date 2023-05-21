---
statblock: true
name: 'Strategos'
image: ![[Strategos.jpg]]
size: Medium
type: Humanoid
alignment: Lawful Neutral
cr: 7
ac: 18
hp: 82
hit_dice: '11d8 + 33'
speed: '30 ft.'
stats:
    - 18
    - 12
    - 16
    - 20
    - 18
    - 16
senses: 'darkvision 60 ft., passive Perception 14'
languages: 'Common, Draconic'
saves:
    - { intelligence: 9 }
    - { wisdom: 8 }
skillsaves:
    - { insight: 8 }
    - { perception: 8 }
actions:
    - { name: Multiattack, desc: 'The strategos makes two melee attacks.' }
    - { name: Tail, desc: 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 11 (1d10 + 6) bludgeoning damage.' }
straits:
    - { name: 'Tactical Mastermind', desc: 'The strategos can take 3 reactions each round, instead of 1.' }
    - { name: 'Strategist’s Insight', desc: 'The strategos adds its Intelligence modifier to its AC.' }
---
```statblock
monster: Strategos
```