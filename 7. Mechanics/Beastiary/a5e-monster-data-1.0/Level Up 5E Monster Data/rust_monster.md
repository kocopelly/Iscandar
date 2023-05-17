---
statblock: true
name: 'Rust Monster - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Monstrosity
cr: 1
ac: 15
hp: 27
hit_dice: '5d8 + 5'
speed: '40 ft.'
stats:
    - 12
    - 12
    - 12
    - 2
    - 12
    - 6
senses: 'darkvision 60 ft., passive Perception 11'
traits:
    - { name: 'Metal Detection', desc: 'The rust monster can smell metal within 30 feet.' }
    - { name: 'Rust Metal', desc: 'A nonmagical weapon made of metal that hits the rust monster corrodes after dealing damage, taking a permanent -1 penalty to damage rolls per hit. If this penalty reaches -5, the weapon is destroyed. Metal nonmagical ammunition is destroyed after dealing damage.' }
actions:
    - { name: Antennae, desc: "The rust monster corrodes a nonmagic metal object within 5 feet. It can destroy up to a 1-foot-square portion of an unattended object. If the object is worn or carried, the object's owner makes a DC 11 Dexterity saving throw, avoiding the rust monster's antennae on a success." }
    - { name: 'Metal shields or armor the rust monster touches with its antennae corrode, taking a permanent -1 penalty to its AC protection per hit', desc: "If the penalty reduces the armor's AC protection to 10, the armor is destroyed. If a metal weapon is touched, it is subject to the Rust Metal trait." }
    - { name: Bite, desc: 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) piercing damage.' }
reactions:
    - { name: 'Defensive Bite', desc: 'When the rust monster is hit by a melee attack made by a creature it can see within 5 feet, it bites the attacker.' }
combat:
    - { name: 'On its turn, the rust monster uses its antennae if there is any metal nearby', desc: 'Otherwise, it runs away. It also runs away if bloodied. It uses its reaction to bite if attacked.' }

---
```statblock
monster: Rust Monster - A5E
```
