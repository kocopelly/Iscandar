---
statblock: true
name: 'Hill Giant - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Giant
cr: 6
ac: 13
hp: 105
hit_dice: '10d12 + 40'
speed: '40 ft.'
stats:
    - 20
    - 8
    - 18
    - 6
    - 10
    - 6
saves:
    - { strength: 8 }
    - { constitution: 7 }
senses: 'passive Perception 10'
languages: Giant
traits:
    - { name: Gullible, desc: 'The giant makes Insight checks with disadvantage.' }
actions:
    - { name: Multiattack, desc: 'The giant attacks twice with its greatclub.' }
    - { name: Greatclub, desc: 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 18 (3d8 + 5) bludgeoning damage. If the target is a Medium or smaller creature, it makes a DC 16 Strength saving throw, falling prone on a failure.' }
    - { name: Rock, desc: 'Ranged Weapon Attack: +8 to hit, range 60/240 ft., one target. Hit: 26 (6d6 + 5) bludgeoning damage. If the target is a Medium or smaller creature, it makes a DC 16 Strength saving throw, falling prone on a failure. In lieu of a rock, the giant can throw a grappled Medium or smaller creature up to 30 feet. On a hit, the target and the thrown creature both take 15 (3d6 + 5) bludgeoning damage. On a miss, only the thrown creature takes the damage. The thrown creature falls prone in an unoccupied space 5 feet from the target.' }
    - { name: 'Greatclub Sweep (1/Day, While Bloodied)', desc: 'Each creature within 10 feet makes a DC 16 Dexterity saving throw. On a failure, a creature takes 18 (3d8 + 5) bludgeoning damage, is pushed 10 feet away from the giant, and falls prone.' }
'bonus actions':
    - { name: Grab, desc: "One creature within 5 feet makes a DC 10 Dexterity saving throw. On a failure, it is grappled (escape DC 16). Until this grapple ends, the giant can't grab another target, and it makes greatclub attacks with advantage against the grappled target." }
combat:
    - { name: 'The giant uses its greatclub and grabs opponents whenever it can', desc: "When it has a creature grabbed, it's not always clever enough to focus its attacks on that target. The giant might surrender if it's damaged by a particularly flashy magical effect while it's bloodied." }

---
```statblock
monster: Hill Giant - A5E
```
