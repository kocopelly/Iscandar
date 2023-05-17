---
statblock: true
name: 'Gnoll Pack Leader - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Humanoid
cr: 2
ac: 14
hp: 45
hit_dice: 10d8
speed: '40 ft.'
stats:
    - 14
    - 12
    - 10
    - 10
    - 8
    - 10
senses: 'darkvision 60 ft., passive Perception 9'
languages: Gnoll
traits:
    - { name: 'Pack Tactics', desc: "The gnoll has advantage on attack rolls against a creature if at least one of the gnoll's allies is within 5 feet of the creature and not incapacitated." }
actions:
    - { name: Spear, desc: 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d6 + 2) piercing damage.' }
    - { name: Multiattack, desc: 'The gnoll attacks twice with its spear.' }
    - { name: 'Chilling Laughter (Recharge 6)', desc: "The gnoll's barking laughter drives allies into a frenzy. Each other creature of the gnoll's choice within 30 feet that can hear it and has a Rampaging Bite bonus action can use its reaction to make a Rampaging Bite." }
'bonus actions':
    - { name: 'Rampaging Bite', desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one bloodied creature. Hit: 4 (1d4 + 2) piercing damage.' }
combat:
    - { name: 'Gnolls attack fearlessly, preferring to target bloodied creatures', desc: 'If no such target is present, they attack whichever enemy is nearest.' }

---
```statblock
monster: Gnoll Pack Leader - A5E
```
