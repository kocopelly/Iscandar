---
statblock: true
name: 'Behemoth'
image: ![[Behemoth.jpg]]
size: Large
type: Humanoid
alignment: Neutral
cr: 4
ac: 17 (natural armor)
hp: 85
hit_dice: '10d10 + 30'
speed: '30 ft.'
stats:
    - 20
    - 8
    - 18
    - 10
    - 12
    - 10
senses: 'passive Perception 11'
languages: 'Common, Draconic'
saves:
    - { strength: 7 }
    - { constitution: 6 }
actions:
    - { name: Multiattack, desc: 'The behemoth makes two attacks with its gore.' }
    - { name: Gore, desc: 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage.' }
    - { name: Trample, desc: 'If the behemoth moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, the target must succeed on a DC 15 Strength saving throw or be knocked prone. If the target is prone, the behemoth can make one stomp attack against it as a bonus action.' }
straits:
    - { name: 'Charge', desc: 'If the behemoth moves at least 20 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) piercing damage.' }
    - { name: 'Armored Hide', desc: 'The behemoth has resistance to nonmagical bludgeoning, piercing, and slashing damage.' }
---
```statblock
monster: Behemoth
```