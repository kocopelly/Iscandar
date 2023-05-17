---
statblock: true
name: 'Storm Giant Monarch - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Giant
cr: 14
ac: 16
hp: 460
hit_dice: '40d12 + 200'
speed: '50 ft., swim 50 ft.'
stats:
    - 29
    - 14
    - 20
    - 16
    - 18
    - 18
damage_resistances: cold
damage_immunities: 'lightning, thunder'
saves:
    - { strength: 14 }
    - { constitution: 10 }
    - { wisdom: 9 }
    - { charisma: 9 }
skillsaves:
    - { arcana: 8 }
    - { athletics: 14 }
    - { history: 8 }
    - { insight: 9 }
    - { perception: 9 }
senses: 'passive Perception 19'
languages: 'Common, Giant'
traits:
    0: { name: Amphibious, desc: 'The giant can breathe air and water.' }
    1: { name: 'Innate Spellcasting', desc: "The giant's spellcasting ability is Charisma (spell save DC 17). It can innately cast the following spells, requiring no material components:" }
    traits: ['At will: detect magic, feather fall, levitate, light', '3/day each: control water, control weather, water breathing', '1/day: commune']
    2: { name: 'Magic Resistance', desc: 'The giant has advantage on saving throws against spells and magical effects.' }
actions:
    - { name: Multiattack, desc: 'The giant attacks twice with its greatsword.' }
    - { name: Greatsword, desc: 'Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 30 (6d6 + 9) slashing damage.' }
    - { name: Rock, desc: 'Ranged Weapon Attack: +12 to hit, range 60/240 ft., one target. Hit: 44 (10d6 + 9) bludgeoning damage. If the target is a Large or smaller creature, it makes a DC 22 Strength saving throw, falling prone on a failure.' }
    - { name: 'Lightning Strike (Recharge 56)', desc: 'The giant throws a lightning bolt at a point it can see within 500 feet. Each creature within 10 feet of that point makes a DC 18 Dexterity saving throw, taking 56 (16d6) lightning damage on a success or half the damage on a failure.' }
    - { name: 'Sword Sweep (While Bloodied)', desc: 'The giant makes a greatsword attack against each creature within 10 feet. Each creature hit with this attack makes a DC 22 Strength saving throw, falling prone on a failure.' }
'bonus actions':
    0: { name: Stomp, desc: 'Melee Weapon Attack: +14 to hit, reach 5 ft., one Medium or smaller prone target. Hit: 19 (3d6 + 9) bludgeoning damage.' }
    'bonus actions': ['The giant has the following bonus actions, which it can only use while bloodied:']
    1: { name: 'Elite Recovery', desc: 'The giant ends one negative effect currently affecting it. It can do so as long as it has at least 1 hit point, even while unconscious or incapacitated.' }
    2: { name: 'Lightning Sword', desc: 'The giant moves or swims up to its Speed without provoking opportunity attacks and makes a greatsword attack. On a hit, the target takes 28 (8d6) extra lightning damage.' }
    3: { name: 'Lightning Strikes (1/Day)', desc: 'The giant recharges and uses Lightning Strike.' }
    4: { name: 'Twister (1/Day)', desc: 'A Large or smaller creature the giant can see within 120 feet makes a DC 18 Strength saving throw. On a failure, it takes 42 (12d6) bludgeoning damage and is caught within a whirlwind or water funnel and restrained for 1 minute. On a success, it takes half damage. A creature can use an action to make a DC 18 Strength saving throw, freeing itself or a creature within its reach from the twister on a success.' }
combat:
    - { name: 'The storm giant attacks with Lightning Strike at every opportunity', desc: 'It is willing to fight at either close or long range. Storm giants are often too proud to surrender or flee but may offer a ceasefire if close to death.' }

---
```statblock
monster: Storm Giant Monarch - A5E
```
