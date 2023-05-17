---
statblock: true
name: 'Psynapse'
image: ![[Psynapse.jpg]]
size: Medium
type: Humanoid
alignment: Neutral
cr: 4
ac: 15
hp: 65
hit_dice: '10d8+20'
speed: '30 ft.'
stats:
    - 10
    - 14
    - 14
    - 24
    - 16
    - 20
saves:
    - { intelligence: 10 }
    - { charisma: 9 }
skills:
    - { arcana: 10 }
    - { deception: 9 }
    - { insight: 8 }
    - { perception: 8 }
    - { persuasion: 9 }
damage_resistances: psychic
senses: 'darkvision 60 ft., passive Perception 18'
languages: 'Common, Draconic'
straits:
    - { name: 'Psionic Mastery', desc: 'Psynapses have a deep understanding of psionics and their potential, allowing them to harness psychic energy with ease. They have advantage on saving throws against spells and other magical effects.' }
    - { name: 'Mind Reading', desc: 'Psynapses can read the thoughts of creatures within 60 feet of them. The creature can make a DC 17 Wisdom saving throw to resist this effect.' }
actions:
    - { name: 'Multiattack', desc: 'The Psynapse makes two attacks with its psychic lash.' }
    - { name: 'Psychic Lash', desc: 'Ranged Spell Attack: +10 to hit, range 30 ft., one target. Hit: 11 (2d6 + 4) psychic damage.' }
    - { name: 'Mind Blast (Recharge 5-6)', desc: 'The Psynapse emits a blast of psychic energy in a 60-foot cone. Each creature in the area must make a DC 17 Intelligence saving throw, taking 22 (4d10) psychic damage on a failed save, or half as much damage on a successful one.' }
---
```statblock
monster: Psynapse
```