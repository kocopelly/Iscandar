---
statblock: true
name: 'Pyrothar'
image: ![[Pyrothar.jpg]]
size: Gargantuan
type: Dragon
alignment: Chaotic Evil
cr: 22
ac: 22
hp: 500
hit_dice: '28d20 + 280'
speed: '40 ft., climb 40 ft., fly 80 ft.'
stats:
    - 30
    - 14
    - 30
    - 20
    - 18
    - 24
damage_immunities: fire
saves:
    - { strength: 16 }
    - { constitution: 16 }
    - { wisdom: 11 }
    - { charisma: 14 }
skillsaves:
    - { intimidation: 14 }
    - { perception: 18 }
senses: 'blindsight 120 ft., darkvision 240 ft., passive Perception 28'
languages: 'Common, Draconic'
straits:
    - { name: 'Fire Aura', desc: 'Pyrothar exudes an aura of intense heat. Each creature that starts its turn within 10 feet of him takes fire damage.' }
    - { name: 'Legendary Resistance (3/Day)', desc: 'If Pyrothar fails a saving throw, he can choose to succeed instead.' }
spells: 
    - 'Pyrothar is a 20th-level spellcaster. His spellcasting ability is Charisma (spell save DC 21). He can innately cast the following spells, requiring no material components:'
    - 'At will: [[burning hands]], [[flaming sphere]], [[fireball]], [[wall of fire]]'
    - '3/day each: [[fire storm]], [[incendiary cloud]]'
actions:
    - { name: Multiattack, desc: 'Pyrothar makes three attacks: one with his bite and two with his claws.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +17 to hit, reach 15 ft., one target. Hit: 21 (2d10 + 10) piercing damage plus 7 (2d6) fire damage.' }
    - { name: Claw, desc: 'Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit: 17 (2d6 + 10) slashing damage.' }
    - { name: Tail, desc: 'Melee Weapon Attack: +17 to hit, reach 20 ft., one target. Hit: 19 (2d8 + 10) bludgeoning damage.' }
    - { name: 'Fire Breath (Recharge 5-6)', desc: 'Pyrothar exhales fire in a 90-foot cone. Each creature in that area must make a DC 24 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one.' }
    - { name: 'Magma Breath (Recharge 5-6)', desc: 'Pyrothar exhales molten lava in a 60-foot line that is 5 feet wide. Each creature in that line must make a DC24 Dexterity saving throw, taking 63 (18d6) fire damage on a failed save, or half as much damage on a successful one. The ground in the line becomes difficult terrain until cleared. Each 5-foot-square portion of the area requires at least 1 minute to clear by hand.'}
legendary_actions:
    - { name: 'Pyrothar can take 3 legendary actions, choosing from the options below', desc: "Only one legendary action can be used at a time and only at the end of another creature's turn. He regains spent legendary actions at the start of his turn." }
    - { name: Detect, desc: 'Pyrothar makes a Wisdom (Perception) check.' }
    - { name: 'Tail Attack', desc: 'Pyrothar makes a tail attack.' }
    - { name: 'Wing Attack (Costs 2 Actions)', desc: 'Pyrothar beats his wings. Each creature within 15 feet of Pyrothar must succeed on a DC 24 Dexterity saving throw or take 17 (2d6 + 10) bludgeoning damage and be knocked prone. Pyrothar can then fly up to half his flying speed.' }
---
```statblock
monster: Pyrothar
```