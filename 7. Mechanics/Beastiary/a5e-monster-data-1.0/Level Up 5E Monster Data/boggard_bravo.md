---
statblock: true
name: 'Boggard Bravo - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Humanoid
cr: 1
ac: 12
hp: 27
hit_dice: 6d8
speed: '20 ft., swim 40 ft.'
stats:
    - 12
    - 14
    - 10
    - 10
    - 10
    - 10
skillsaves:
    - { stealth: 4 }
    - { survival: 2 }
senses: 'passive Perception 10'
languages: Boggard
traits:
    - { name: Amphibious, desc: 'The boggard can breathe air and water.' }
    - { name: 'Speak with Frogs and Toads', desc: 'The boggard can communicate with frogs and toads.' }
actions:
    - { name: 'Vaulting Leap', desc: "The boggard jumps up to its Speed horizontally and half its Speed vertically without provoking opportunity attacks. If it's within 5 feet of a creature at the end of this movement, it may make a melee spear attack against that creature with advantage." }
    - { name: Spear, desc: 'Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.' }
'bonus actions':
    - { name: Tongue, desc: "Melee Weapon Attack: +3 to hit, reach 15 ft., one creature. Hit: The target must make a DC 11 Strength saving throw. On a failure, the boggard pulls the target up to 10 feet, or knocks the target prone, or forces the target to drop one item it is holding (boggard's choice)." }
combat:
    - { name: "The boggard uses Vaulting Leap to move around whenever it's not sneaking, essentially doubling its movement speed", desc: 'When attacking, it uses Vaulting Leap to close with its enemies and deliver a powerful spear attack. While next to a foe, it uses its more accurate bite attack. Once a group of boggards have been reduced to half their number, they retreat, trusting in their stealth to escape.' }

---
```statblock
monster: Boggard Bravo - A5E
```
