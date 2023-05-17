---
statblock: true
name: 'Giant Fire Elemental - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Elemental
cr: 9
ac: 14
hp: 127
hit_dice: '15d12 + 30'
speed: '50 ft.'
stats:
    - 10
    - 18
    - 14
    - 6
    - 10
    - 6
damage_resistances: 'damage from nonmagical weapons'
damage_immunities: 'fire, poison'
condition_immunities: 'fatigue, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious'
senses: 'darkvision 60 ft., passive Perception 10'
languages: Ignan
traits:
    - { name: 'Fire Form', desc: 'The elemental can move through a space as narrow as 1 inch wide without squeezing.' }
    - { name: 'Fiery Aura', desc: 'A creature that ends its turn within 5 feet of the fire elemental takes 5 (1d10) fire damage. A creature that touches the elemental or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire damage. The elemental sheds bright light in a 30-foot radius and dim light for an additional 30 feet.' }
    - { name: 'Water Weakness', desc: "The elemental takes 6 (1d12) cold damage if it enters a body of water or starts its turn in a body of water, is splashed with at least 5 gallons of water, or is hit by a water elemental's slam attack." }
    - { name: 'Elemental Nature', desc: "An elemental doesn't require air, sustenance, or sleep." }
actions:
    - { name: Multiattack, desc: 'The elemental makes two slam attacks.' }
    - { name: Slam, desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 24 (4d8 + 4) fire damage, and the target suffers 5 (1d10) ongoing fire damage. A creature can use an action to end the ongoing damage.' }
    - { name: 'Wildfire (Recharge 46)', desc: "The elemental moves up to half its Speed without provoking opportunity attacks. It can enter the spaces of hostile creatures but not end this movement there. When a creature shares its space with the elemental for the first time during this movement, the creature is subject to the elemental's Fiery Aura and the elemental can make a slam attack against that creature." }
combat:
    - { name: 'The elemental uses Wildfire whenever it can move through the spaces of at least two enemies', desc: 'It prioritizes enemies who are not yet on fire. Elementals retreat only if ordered to do so.' }

---
```statblock
monster: Giant Fire Elemental - A5E
```
