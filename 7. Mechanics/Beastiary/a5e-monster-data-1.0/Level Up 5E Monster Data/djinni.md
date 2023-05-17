---
statblock: true
name: 'Djinni - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Elemental
cr: 11
ac: 16
hp: 172
hit_dice: '15d10 + 90'
speed: '30 ft., fly 90 ft (hover).'
stats:
    - 18
    - 22
    - 22
    - 14
    - 16
    - 20
damage_resistances: 'lightning, thunder'
saves:
    - { dexterity: 10 }
    - { intelligence: 6 }
    - { wisdom: 7 }
    - { charisma: 9 }
skillsaves:
    - { acrobatics: 10 }
    - { insight: 7 }
    - { perception: 7 }
senses: 'darkvision 120 ft., passive Perception 17'
languages: Auran
traits:
    0: { name: 'Innate Spellcasting', desc: "The djinni's innate spellcasting ability is Charisma (spell save DC 17). It can innately cast the following spells, requiring no material components:" }
    traits: ['At will: alter self (can assume Medium or Large form), detect magic, wind wall', '3/day each: creation, major image, tongues, wind walk', '1/day each: conjure elemental (air elemental only), control weather, create food and water (10 supply), plane shift (to Elemental Plane of Air only)']
    1: { name: 'Elemental Demise', desc: 'When a genie dies, its body becomes a mote of elemental energy. This mote might take the form of a glowing chunk of earth, a shard of crystallized air, or an ever-burning ember.' }
actions:
    - { name: Multiattack, desc: 'The djinni makes three scimitar attacks.' }
    - { name: Scimitar, desc: 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage plus 5 (1d10) lightning damage.' }
    - { name: 'Lightning Blast', desc: 'Ranged Spell Attack: +9 to hit, range 90 ft., one target. Hit: 35 (10d6) lightning damage.' }
    - { name: 'Scimitar Sweep (1/Day, Giant Form Only)', desc: 'The djinn makes a scimitar attack against each creature of its choice within its reach.' }
'bonus actions':
    - { name: 'Giant Form (1/Day, While Not Bloodied)', desc: 'The djinni magically becomes a Huge, semi-substantial creature of billowing cloud. In this form, it gains resistance to nonmagical damage, and its scimitar attacks gain a reach of 10 feet. The effect ends after 1 minute, when the djinni is incapacitated, or if the djinn becomes bloodied.' }
    - { name: 'Whirlwind (1/Day)', desc: "A magical, 5-foot-wide, 30-foot-tall whirlwind appears in a space the djinni can see within 60 feet. The whirlwind may appear in another creature's space. If the whirlwind appears in another creature's space, or when it enters a creature's space for the first time on a turn, the creature makes a DC 18 Strength check, becoming restrained by the whirlwind on a failure. The whirlwind may restrain one creature at a time. A creature within 5 feet of the whirlwind (including the restrained creature) can use an action to make a DC 18 Strength check, freeing the restrained creature on a success. A freed creature can move to an unoccupied space within 5 feet of the whirlwind." }
    - { name: 'As a bonus action, the djinni can move the whirlwind up to 30 feet, moving a restrained creature with it', desc: 'The whirlwind disappears if the djinni loses sight of it, if the djinni dies or is incapacitated, or if the djinni dismisses it as an action.' }
combat:
    - { name: 'The djinni begins combat by taking Giant Form, then using Scimitar Sweep if it can target four or more foes', desc: 'Otherwise, it uses Whirlwind to move a melee attacker far away or draw a ranged attacker close.' }
    - { name: "Once the djinn is bloodied and can't use its Giant Form, it flies away unless it can complete some important objective by remaining", desc: '' }

---
```statblock
monster: Djinni - A5E
```
