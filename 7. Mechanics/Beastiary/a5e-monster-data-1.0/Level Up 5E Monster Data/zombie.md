---
statblock: true
name: 'Zombie - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Undead
cr: 1
ac: 8
hp: 15
hit_dice: '2d8 + 6'
speed: '20 ft.'
stats:
    - 12
    - 6
    - 16
    - 3
    - 6
    - 4
damage_immunities: poison
condition_immunities: 'fatigue, poisoned'
senses: 'darkvision 60 ft., passive Perception 8'
languages: "understands the languages it knew in life but can't speak"
traits:
    - { name: 'Undead Fortitude (1/Day)', desc: "If the zombie is reduced to 0 hit points by damage that isn't radiant or from a critical hit, it's instead reduced to 1 hit point, falls prone, and is stunned until the end of its next turn, appearing to be dead." }
    - { name: 'Undead Nature', desc: "A zombie doesn't require air, sustenance, or sleep." }
actions:
    - { name: Grab, desc: "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage. If the target is a Medium or smaller creature, it is grappled (escape DC 11). Until the grapple ends, the zombie can't grab another target." }
    - { name: Bite, desc: 'Melee Weapon Attack: +3 to hit, reach 5 ft., one grappled target. Hit: 6 (1d10 + 1) piercing damage, and the zombie regains the same number of hit points.' }

---
```statblock
monster: Zombie - A5E
```
