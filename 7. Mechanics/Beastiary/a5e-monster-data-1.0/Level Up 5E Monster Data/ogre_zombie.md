---
statblock: true
name: 'Ogre Zombie - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Undead
cr: 2
ac: 11
hp: 59
hit_dice: '7d10 + 28'
speed: '30 ft.'
stats:
    - 18
    - 6
    - 18
    - 3
    - 8
    - 4
damage_immunities: poison
condition_immunities: 'fatigue, poisoned'
senses: 'darkvision 60 ft., passive Perception 8'
languages: "understands Giant but can't speak"
traits:
    - { name: 'Undead Fortitude (1/Day)', desc: "If the zombie is reduced to 0 hit points by damage that isn't radiant or from a critical hit, it's instead reduced to 1 hit point, falls prone, and is stunned until the end of its next turn, appearing to be dead." }
    - { name: 'Undead Nature', desc: "A zombie doesn't require air, sustenance, or sleep." }
actions:
    - { name: Greatclub, desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage, and if the target is a Medium or smaller creature, it makes a DC 14 Strength saving throw, falling prone on a failure.' }
    - { name: 'Sweeping Strike', desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., all creatures within 5 feet. Hit: 8 (1d8 + 4) bludgeoning damage, and if the target is a Medium or smaller creature, it makes a DC 14 Strength saving throw. On a failure, it is pushed 10 feet away from the ogre.' }
    - { name: Grab, desc: "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage, and the target is grappled if it's Medium or smaller (escape DC 14), and until the grapple ends, the zombie can't grab another target." }
    - { name: Bite, desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target grappled by a zombie. Hit: 15 (2d10 + 4) piercing damage, and the zombie regains hit points equal to the damage dealt.' }

---
```statblock
monster: Ogre Zombie - A5E
```
