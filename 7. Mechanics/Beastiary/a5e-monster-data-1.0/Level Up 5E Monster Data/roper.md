---
statblock: true
name: 'Roper - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Monstrosity
cr: 5
ac: 20
hp: 93
hit_dice: '11d10 + 33'
speed: '10 ft., climb 10 ft.'
stats:
    - 18
    - 8
    - 16
    - 6
    - 14
    - 4
senses: 'blindsight 30 ft., darkvision 60 ft., passive Perception 12'
traits:
    - { name: 'False Appearance', desc: 'While motionless, the roper is indistinguishable from a normal stalactite or stalagmite.' }
    - { name: 'Spider Climb', desc: 'The roper can climb even on difficult surfaces and upside down on ceilings.' }
    - { name: Tendrils, desc: 'The roper has eight tendrils. Each tendril has AC 20, 15 hit points, vulnerability to slashing damage, and immunity to psychic damage. A creature can also break a tendril by taking an action to make a DC 15 Strength check. A tendril takes no damage from sources other than attacks. The roper grows back any destroyed tendrils after a long rest.' }
actions:
    - { name: Multiattack, desc: 'The roper makes up to four tendril attacks, then uses Reel, then attacks with its bite.' }
    - { name: Tendril, desc: "Melee Weapon Attack: +7 to hit, reach 50 ft., one target. Hit: The target is grappled (escape DC 15). Until this grapple ends, the target is restrained and the roper can't use this tendril on another target." }
    - { name: Reel, desc: 'The roper pulls each creature it is grappling up to 25 feet straight towards it.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage plus 9 (2d8) acid damage.' }
combat:
    - { name: 'The roper keeps its eye closed, remaining immobile and nearly undetectable, until a creature approaches within 30 feet (the range of its blindsight)', desc: 'It then opens its eyes and attacks as many creatures as possible within range of its tendrils. It fights to the death.' }

---
```statblock
monster: Roper - A5E
```
