---
statblock: true
name: 'Ghoul - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Undead
cr: 1
ac: 12
hp: 22
hit_dice: 5d8
speed: '30 ft.'
stats:
    - 12
    - 14
    - 10
    - 6
    - 10
    - 6
damage_resistances: necrotic
damage_immunities: poison
condition_immunities: 'charmed, fatigue, paralyzed, poisoned'
senses: 'darkvision 60 ft., passive Perception 10'
languages: Common
traits:
    - { name: 'Radiant Sensitivity', desc: 'When the ghoul takes radiant damage, it has disadvantage on attack rolls and on Perception checks that rely on sight until the end of its next turn.' }
    - { name: 'Undead Nature', desc: "Ghouls and ghasts don't require air, sustenance, or sleep." }
actions:
    - { name: 'Paralyzing Claw', desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage. If the target is a living creature other than an elf, it makes a DC 10 Constitution saving throw. On a failure, the target is paralyzed for 1 minute. The target repeats the saving throw at the end of its turns, ending the effect on itself on a success. If the target's saving throw is successful or the effect ends for it, it is immune to any Paralyzing Claw for 24 hours." }
    - { name: Bite, desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one incapacitated creature. Hit: 6 (1d8 + 2) piercing damage.' }
combat:
    - { name: 'Ghouls rarely attack when they are outnumbered', desc: 'They prefer to swarm their enemies, with at least two ghouls attacking one target, preferably an unarmored non-elf. They retreat if they take radiant damage but try to drag paralyzed victims with them.' }

---
```statblock
monster: Ghoul - A5E
```
