---
statblock: true
name: 'Rug of Smothering - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Construct
cr: 2
ac: 12
hp: 45
hit_dice: '7d8 + 14'
speed: '30 ft.'
stats:
    - 16
    - 14
    - 14
    - 1
    - 10
    - 1
damage_resistances: bludgeoning
damage_immunities: 'poison, psychic'
condition_immunities: 'blinded, charmed, deafened, exhaustion, frightened, paralyzed, petrified, poisoned'
senses: 'blindsight 60 ft. (blind beyond this radius), passive Perception 10'
traits:
    - { name: Spell-created, desc: 'The DC for dispel magic to destroy this creature is 19.' }
    - { name: 'False Appearance', desc: 'While motionless, the rug is indistinguishable from a normal rug.' }
actions:
    - { name: Smother, desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one Large or smaller creature. Hit: The target is grappled (escape DC 13). Until this grapple ends, the target is restrained and can't breathe. When the rug is dealt damage while it is grappling, it takes half the damage (rounded down) and the other half is dealt to the grappled target. The rug can only have one creature grappled at once." }
    - { name: Squeeze, desc: 'One creature grappled by the rug takes 10 (2d6 + 3) bludgeoning damage.' }
combat:
    - { name: 'Animated objects usually wait immobile until touched or approached, and then attack the closest creature', desc: 'Some follow more complicated routines. Animated objects follow the commands last given them by their creators and show no initiative.' }
    - { name: 'A rug of smothering lies in wait in a well-furnished room', desc: "When a victim steps on or sits on the rug, it rolls up around the victim and squeezes the life out of them. A nearby skeleton might betray the rug's dangerous nature." }
    - { name: 'A rug of smothering can also be used as a curtain or tapestry, in which case it may attack creatures that touch it or merely move within 5 feet', desc: '' }

---
```statblock
monster: Rug of Smothering - A5E
```
