---
statblock: true
name: 'Revenant - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Undead
cr: 5
ac: 13
hp: 110
hit_dice: '13d8 + 52'
speed: '30 ft.'
stats:
    - 18
    - 16
    - 18
    - 10
    - 12
    - 18
damage_resistances: 'necrotic, psychic'
damage_immunities: poison
condition_immunities: 'charmed, fatigue, frightened, paralyzed, poisoned, stunned'
saves:
    - { strength: 7 }
    - { constitution: 7 }
    - { wisdom: 4 }
    - { charisma: 7 }
senses: 'darkvision 60 ft., passive Perception 11'
languages: 'the languages it knew in life'
traits:
    - { name: 'Fearsome Pursuit', desc: "The revenant can spend 1 minute focusing on a creature against which it has sworn vengeance. If the creature is dead or on another plane of existence, it learns that. Otherwise, after focusing, it knows the distance and direction to that creature, and so long as it's moving in pursuit of that creature, it ignores difficult terrain. This effect ends if the revenant takes damage or ends its turn without moving for any reason." }
    - { name: 'Magic Resistance', desc: 'The revenant has advantage on saving throws against spells and other magical effects.' }
    - { name: 'Rapid Recovery', desc: 'If the revenant goes 1 minute without taking damage, it regains all its missing hit points.' }
    - { name: Relentless, desc: 'When the revenant is reduced to 0 hit points, its body turns to dust. One minute later, its spirit inhabits a recently-dead humanoid corpse of its choice on the same plane of existence, awakening with 1 hit point.' }
actions:
    - { name: Multiattack, desc: 'The revenant makes two strangle attacks. It can replace one attack with Burning Hatred, if available.' }
    - { name: Strangle, desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage, and the target is grappled (escape DC 15) if it's a Large or smaller creature. Until this grapple ends, the creature can't breathe, and the revenant can't strangle any other creature." }
    - { name: 'Burning Hatred (Recharge 46)', desc: 'The revenant targets the focus of its Fearsome Pursuit, assuming the creature is within 30 feet. The target makes a DC 15 Wisdom saving throw. On a failure, it takes 14 (4d6) psychic damage and is paralyzed until the end of its next turn. On a success, it takes half damage and is frightened until the end of its next turn.' }
combat:
    - { name: 'THE REVENANT USES BURNING HATRED AND STRANGLES ITS CHOSEN ENEMY', desc: 'IT STRANGLES ANYONE THAT TRIES TO STOP IT FROM REACHING ITS ENEMY.' }

---
```statblock
monster: Revenant - A5E
```
