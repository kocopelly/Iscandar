---
statblock: true
name: 'Cloud Giant Noble - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Giant
cr: 12
ac: 14
hp: 187
hit_dice: '15d12 + 90'
speed: '40 ft.'
stats:
    - 27
    - 10
    - 22
    - 12
    - 16
    - 16
damage_resistances: 'lightning, thunder'
saves:
    - { strength: 12 }
    - { constitution: 10 }
    - { wisdom: 7 }
    - { charisma: 7 }
skillsaves:
    - { insight: 7 }
    - { perception: 7 }
    - { persuasion: 7 }
senses: 'passive Perception 17'
languages: 'Common, Giant'
traits:
    0: { name: 'Cloud Sight', desc: "Clouds and fog do not impair the giant's vision." }
    1: { name: 'Innate Spellcasting', desc: "The giant's spellcasting ability is Charisma (spell save DC 15). It can innately cast the following spells, requiring no material components:" }
    traits: ['At will: detect magic, fog cloud, light', '3/day each: feather fall, fly, misty step, telekinesis', '1/day each: control weather, gaseous form']
    2: { name: 'Keen Smell', desc: 'The giant has advantage on Perception checks that rely on smell.' }
actions:
    - { name: Multiattack, desc: 'The giant attacks twice with its glaive.' }
    - { name: Glaive, desc: 'Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 24 (3d10 + 8) slashing damage. If the target is a Large or smaller creature, it makes a DC 20 Strength saving throw. On a failure, it is pushed up to 10 feet away from the giant and knocked prone.' }
    - { name: Rock, desc: 'Ranged Weapon Attack: +12 to hit, range 60/240 ft., one target. Hit: 39 (9d6 + 8) bludgeoning damage. If the target is a Large or smaller creature, it makes a DC 20 Strength saving throw, falling prone on a failure.' }
    - { name: 'Fog Cloud (1st-Level; V, S, Concentration)', desc: 'The giant creates a 20-foot-radius, heavily obscured sphere of fog centered on a point it can see within 120 feet. The fog spreads around corners and can be dispersed by a moderate wind (at least 10 miles per hour). It lasts for 1 hour.' }
    - { name: 'Arc Lightning (1/Day)', desc: 'Up to three creatures within 60 feet that the giant can see make DC 15 Dexterity saving throws, taking 42 (12d6) lightning damage on a failure or half damage on a success.' }
    - { name: 'Blinking Blades (1/Day)', desc: 'The giant magically teleports multiple times within a few seconds. The giant may make one glaive attack against each creature of its choice within 30 feet, up to a maximum of 6 attacks.' }
    - { name: 'Reverse Gravity (1/Day)', desc: "Each creature of the giant's choice within 30 feet is magically hurled 60 feet in the air. If a creature hits an obstacle, it takes 21 (6d6) bludgeoning damage. The creatures then fall, taking falling damage as normal." }
    - { name: 'Silver Tongue (1/Day)', desc: 'One creature that can hear the giant within 30 feet makes a DC 15 Wisdom saving throw. On a failure, it is magically charmed by the giant for 1 hour. This effect ends if the giant or its allies harm the creature.' }
'bonus actions':
    - { name: Gust, desc: 'One creature within 10 feet makes a DC 15 Strength saving throw. On a failure, it is pushed up to 30 feet away from the giant.' }
    - { name: 'Misty Step (2nd-Level; V)', desc: "The giant teleports to an unoccupied space it can see within 30 feet. The giant can't cast this spell and a 1st-level or higher spell on the same turn." }
combat:
    - { name: 'The cloud giant prefers to fight from within a fog cloud, in which it can attack a blinded creature and then cast misty step', desc: 'If bloodied while forced to fight in the open, it casts fly and retreats or tries to parley.' }

---
```statblock
monster: Cloud Giant Noble - A5E
```
