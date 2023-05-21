---
statblock: true
name: 'Empathos'
image: ![[Empathos.jpg]]
size: Medium
type: Humanoid
alignment: Neutral
cr: 2
ac: 14
hp: 34
hit_dice: '6d8 + 6'
speed: '30 ft.'
stats:
    - 12
    - 14
    - 12
    - 16
    - 18
    - 20
senses: 'darkvision 60 ft., passive Perception 14'
languages: 'Common, Draconic'
saves:
    - { wisdom: 7 }
    - { charisma: 8 }
skillsaves:
    - { persuasion: 8 }
    - { insight: 7 }
actions:
    - { name: Emotional Attunement, desc: 'The empathos can sense the emotional state of any creature within 60 feet of it that isnt an undead or a construct. It knows the creatures current emotional state and can influence it by succeeding a DC 15 Charisma (Persuasion) check.' }
    - { name: Soothing Presence, desc: 'The empathos targets one creature it can see within 30 feet of it. The target must succeed on a DC 15 Wisdom saving throw or be calmed for 1 minute. While calmed, the target is pacified and cant take aggressive actions.' }
straits:
    - { name: 'Empathic', desc: 'The empathos has advantage on Wisdom (Insight) and Charisma (Persuasion) checks.' }
---
```statblock
monster: Empathos
```