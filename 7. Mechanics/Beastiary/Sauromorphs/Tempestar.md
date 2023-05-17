---
statblock: true
name: 'Tempestar'
image: ![[Tempestar_Portrait.jpg]]
size: Gargantuan
type: Dragon
alignment: Lawful Neutral
cr: 20
ac: 22
hp: 362
hit_dice: '25d20 + 150'
speed: '40 ft., fly 80 ft.'
stats:
    - 26
    - 14
    - 22
    - 22
    - 18
    - 20
damage_immunities: lightning, thunder
saves:
    - { dexterity: 9 }
    - { constitution: 13 }
    - { wisdom: 11 }
    - { charisma: 12 }
skillsaves:
    - { perception: 16 }
    - { insight: 11 }
    - { nature: 12 }
senses: 'blindsight 120 ft., darkvision 240 ft., passive Perception 26'
languages: 'Auran, Common, Draconic'
straits:
    - { name: 'Legendary Resistance (3/Day)', desc: 'If Tempestar fails a saving throw, it can choose to succeed insteadsucceed instead.' }
    - { name: 'Magical Nature', desc: 'Tempestar’s innate spellcasting ability is Wisdom (spell save DC 19, +11 to hit with spell attacks). Tempestar can innately cast the following spells, requiring no material components: At will: detect magic, gust of wind, wind wall 3/day each: call lightning, control weather, wind walk' }
actions:
    - { name: 'Multiattack', desc: 'Tempestar can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.' }
    - { name: 'Bite', desc: 'Melee Weapon Attack: +14 to hit, reach 15 ft., one target. Hit: 19 (2d10 + 8) piercing damage plus 4 (1d8) lightning damage.' }
    - { name: 'Claw', desc: 'Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 15 (2d6 + 8) slashing damage.' }
    - { name: 'Tail', desc: 'Melee Weapon Attack: +14 to hit, reach 20 ft., one target. Hit: 17 (2d8 + 8) bludgeoning damage.' }
    - { name: 'Frightful Presence', desc: 'Each creature of Tempestar’s choice that is within 120 feet of Tempestar and aware of it must succeed on a DC 17 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature’s saving throw is successful or the effect ends for it, the creature is immune to Tempestar’s Frightful Presence for the next 24 hours.' }
    - { name: 'Lightning Breath (Recharge 5-6)', desc: 'Tempestar exhales lightning in a 90-foot line that is 5 feet wide. Each creature in that line must make a DC 21 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one.' }
    - { name: 'Storm Breath (Recharge 5-6)', desc: 'Tempestar exhales energy in a 60-foot cone. Each creature in that area must make a DC 21 Constitution saving throw, taking 72 (16d8) thunder damage on a failed save, or half as much damage on a successful one.' }
legendary_actions:
    - { name: 'Detect', desc: 'Tempestar makes a Wisdom (Perception) check.' }
    - { name: 'Tail Attack', desc: 'Tempestar makes a tail attack.' }
    - { name: 'Wing Attack (Costs 2 Actions)', desc: 'Tempestar beats its wings. Each creature within 15 feet of Tempestar must succeed on a DC 22 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Tempestar can then fly up to half its flying speed.' }
---
```statblock
monster: Tempestar
```