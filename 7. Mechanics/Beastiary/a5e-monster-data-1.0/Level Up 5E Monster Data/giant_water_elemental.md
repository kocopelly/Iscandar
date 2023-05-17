---
statblock: true
name: 'Giant Water Elemental - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Elemental
cr: 9
ac: 14
hp: 157
hit_dice: '15d12 + 60'
speed: '30 ft., swim 90 ft.'
stats:
    - 18
    - 14
    - 18
    - 6
    - 10
    - 6
damage_resistances: 'acid; damage from nonmagical weapons'
damage_immunities: poison
condition_immunities: 'fatigue, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious'
senses: 'darkvision 60 ft., passive Perception 10'
languages: Aquan
traits:
    - { name: Conductive, desc: 'If the elemental takes lightning damage, each creature sharing its space takes the same amount of lightning damage.' }
    - { name: 'Fluid Form', desc: "The elemental can enter and end its turn in other creatures' spaces and move through a space as narrow as 1 inch wide without squeezing." }
    - { name: Freeze, desc: 'If the elemental takes cold damage, its speed is reduced by 15 feet until the end of its next turn.' }
actions:
    - { name: Multiattack, desc: 'The elemental makes two slam attacks.' }
    - { name: Slam, desc: 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 22 (4d8 + 4) bludgeoning damage.' }
    - { name: Whelm, desc: 'The elemental targets each Large or smaller creature in its space. Each target makes a DC 15 Strength saving throw. On a failure, the target is grappled (escape DC 15). Until this grapple ends, the target is restrained and unable to breathe air. The elemental can move at full speed while carrying grappled creatures inside its space. It can grapple one Large creature or up to four Medium or smaller creatures.' }
combat:
    - { name: "The water elemental uses Whelm to drown two or more creatures, beating them with slam attacks while they're restrained in the elemental's space", desc: 'While on dry land, the elemental seeks cover from mobile ranged attackers. Elementals retreat only if ordered to do so.' }

---
```statblock
monster: Giant Water Elemental - A5E
```
