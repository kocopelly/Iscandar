---
statblock: true
name: 'Dire Tyrannosaurus Rex - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Beast
cr: 8
ac: 13
hp: 253
hit_dice: '22d12 + 110'
speed: '50 ft.'
stats:
    - 22
    - 10
    - 20
    - 6
    - 16
    - 5
senses: 'passive Perception 11'
actions:
    - { name: Multiattack, desc: 'The tyrannosaurus makes a bite attack and a tail attack against two different targets.' }
    - { name: Bite, desc: "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 25 (3d12 + 6) piercing damage. If the target is a creature, it is grappled (escape DC 17). Until this grapple ends, the tyrannosaurus can't bite a different creature and it has advantage on bite attacks against the grappled creature." }
    - { name: Tail, desc: 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage.' }
'bonus actions':
    'bonus actions': ['The dire tyrannosaurus rex has the following additional bonus actions, which it can use only while bloodied:']
    0: { name: 'Elite Recovery', desc: 'The dire tyrannosaurus rex ends one negative effect currently affecting it. It can use this bonus action as long as it has at least 1 hit point, even while unconscious or incapacitated.' }
    1: { name: Trample, desc: 'The dire tyrannosaurus rex moves up to its speed in a straight line. It can move through the spaces of Large and smaller creatures. Each of these creatures makes a DC 17 Dexterity saving throw, taking 19 (3d8 + 6) bludgeoning damage and falling prone on a failure.' }
    2: { name: 'Tail Sweep', desc: 'The dire tyrannosaurus rex makes a tail attack against each creature within 10 feet. A creature hit by an attack makes a DC 17 Strength saving throw, falling prone on a failure.' }
    3: { name: 'Roar (1/Day)', desc: "Each creature of the dire tyrannosaurus rex's choice within 120 feet that hears its roar makes a DC 14 Charisma saving throw. On a failure, a creature is frightened for 1 minute. A creature repeats the saving throw at the end of its turns, ending the effect on itself on a success." }

---
```statblock
monster: Dire Tyrannosaurus Rex - A5E
```
