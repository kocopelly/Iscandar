---
statblock: true
name: 'Hell Hound - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Fiend
cr: 3
ac: 15
hp: 52
hit_dice: '7d8 + 21'
speed: '50 ft.'
stats:
    - 16
    - 14
    - 16
    - 6
    - 12
    - 8
damage_immunities: fire
skillsaves:
    - { perception: 3 }
senses: 'darkvision 60 ft., passive Perception 15'
languages: "understands Infernal but can't speak"
traits:
    - { name: 'Keen Hearing and Smell', desc: 'The hound has advantage on Perception checks that rely on hearing and smell.' }
    - { name: 'Lawful Evil', desc: 'The hound radiates a Lawful and Evil aura.' }
    - { name: 'Pack Tactics', desc: "The hound has advantage on attack rolls against a creature if at least one of the hound's allies is within 5 feet of the creature and not incapacitated." }
actions:
    - { name: Bite, desc: 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage plus 7 (2d6) fire damage.' }
    - { name: 'Fire Breath (Recharge 5-6)', desc: 'The hound exhales fire in a 15-foot cone. Each creature in that area makes a DC 12 Dexterity saving throw, taking 21 (6d6) fire damage on a failed save or half damage on a success.' }
combat:
    - { name: "The hound attacks with its fire breath when it's available", desc: 'It chases down enemies who try to flee.' }

---
```statblock
monster: Hell Hound - A5E
```
