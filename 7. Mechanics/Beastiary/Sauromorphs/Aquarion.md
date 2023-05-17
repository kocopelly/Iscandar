---
statblock: true
name: 'Aquarion'
image: ![[Aquarion_Portrait.jpg]]
size: Gargantuan
type: Dragon
alignment: Neutral Good
cr: 20
ac: 22
hp: 400
hit_dice: '25d20 + 200'
speed: '40 ft., swim 60 ft., fly 80 ft.'
stats:
    - 30
    - 14
    - 28
    - 20
    - 18
    - 24
damage_resistances: fire
saves:
    - { dexterity: 9 }
    - { constitution: 15 }
    - { wisdom: 11 }
    - { charisma: 13 }
skillsaves:
    - { perception: 17 }
    - { insight: 11 }
senses: 'blindsight 120 ft., darkvision 240 ft., passive Perception 27'
languages: 'Common, Draconic, Aquan'
straits:
    - { name: 'Amphibious', desc: 'Aquarion can breathe air and water.' }
    - { name: 'Legendary Resistance (3/Day)', desc: 'If Aquarion fails a saving throw, it can choose to succeed instead.' }
spells: 
    - 'Aquarion is a 20th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 19, +11 to hit with spell attacks). It can innately cast the following spells, requiring no material components:'
    - 'At will: [[create or destroy water]], [[shape water]], [[water walk]]'
    - '3/day each: [[control water]], [[wall of water]], [[ice storm]], [[cone of cold]]'
    - '1/day each: [[tsunami]], [[mass heal]]'
actions:
    - { name: Multiattack, desc: 'Aquarion makes three attacks: one with its bite and two with its claws.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +16 to hit, reach 15 ft., one target. Hit: 18 (2d10 + 7) piercing damage.' }
    - { name: Claw, desc: 'Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 14 (2d6 + 7) slashing damage.' }
    - { name: Tail, desc: 'Melee Weapon Attack: +16 to hit, reach 20 ft., one target. Hit: 16 (2d8 + 7) bludgeoning damage.' }
    - { name: 'Water Breath (Recharge 5–6)', desc: 'Aquarion exhales a 90-foot cone of water. Each creature in that area must make a DC 24 Strength saving throw, being pushed 60 feet away and knocked prone on a failed save, or half as much on a successful one.' }
    - { name: 'Ice Breath (Recharge 5–6)', desc: 'Aquarion exhales a 90-foot cone of cold. Each creature in that area must make a DC 24 Constitution saving throw, taking 66 (12d10) cold damage on a failed save, or half as much damage on a successful one.' }
legendary_actions:
    - { name: 'Aquarion can take 3 legendary actions, choosing from the options below', desc: "Only one legendary action can be used at a time and only at the end of another creature's turn. Aquarion regains spent legendary actions at the start of its turn." } 
    - { name: Detect, desc: 'Aquarion makes a Wisdom (Perception) check.' } 
    - { name: 'Tail Attack', desc: 'Aquarion makes a tail attack.' } 
    - { name: 'Wing Attack (Costs 2 Actions)', desc: 'Aquarion beats its wings. Each creature within 15 feet of Aquarion must succeed on a DC 24 Dexterity saving throw or take 14 (2d6 + 7) bludgeoning damage and be knocked prone. Aquarion can then fly up to half its flying speed.' }
---
```statblock
monster: Aquarion
```