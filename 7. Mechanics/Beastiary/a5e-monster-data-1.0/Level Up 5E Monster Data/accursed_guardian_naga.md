---
statblock: true
name: 'Accursed Guardian Naga - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Monstrosity
cr: 12
ac: 18
hp: 136
hit_dice: '16d10 + 48'
speed: '40 ft., swim 40 ft.'
stats:
    - 16
    - 18
    - 16
    - 16
    - 18
    - 18
damage_immunities: poison
condition_immunities: 'charmed, poisoned'
saves:
    - { dexterity: 8 }
    - { constitution: 7 }
    - { intelligence: 7 }
    - { wisdom: 8 }
    - { charisma: 8 }
senses: 'darkvision 60 ft., passive Perception 14'
languages: 'Abyssal, Celestial, Common'
traits:
    - { name: Amphibious, desc: 'The naga can breathe air and water.' }
    - { name: Forbiddance, desc: "The naga's lair is under the forbiddance spell. Until it is dispelled, creatures in the lair can't teleport or use planar travel. Fiends and undead that are not the naga's allies take 27 (5d10) radiant damage when they enter or start their turn in the lair." }
    - { name: 'Magic Resistance', desc: 'The naga has advantage on saving throws against spells and magical effects.' }
spells:
    spells: ['The naga is an 11th level spellcaster. Its spellcasting ability is Wisdom (spell save DC 16). The naga has the following cleric spells prepared, which it can cast with only vocalized components:', 'Cantrips (at will): mending, thaumaturgy', '1st-level (4 slots): command, cure wounds, false life', '2nd-level (3 slots): calm emotions, hold person, locate object', '3rd-level (3 slots) clairvoyance, create food and water', '4th-level (3 slots): divination, freedom of movement', '5th-level (2 slots): flame strike, geas, scrying', '6th-level (1 slot): forbiddance']
actions:
    - { name: Bite, desc: 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage. The target makes a DC 15 Constitution saving throw, taking 35 (10d6) poison damage on a failure or half damage on a success.' }
    - { name: 'Spit Poison', desc: 'Melee Weapon Attack: +8 to hit, range 20/60 ft., one creature. Hit: The target makes a DC 15 Constitution saving throw, taking 35 (10d6) poison damage on a failure or half damage on a success.' }
    - { name: 'Command (1st-Level; V)', desc: 'One living creature within 60 feet that the naga can see and that can hear and understand it makes a DC 16 Wisdom saving throw. On a failure, the target uses its next turn to move as far from the naga as possible, avoiding hazardous terrain.' }
    - { name: 'Hold Person (2nd-Level; V, Concentration)', desc: 'One humanoid the naga can see within 60 feet makes a DC 16 Wisdom saving throw. On a failure, the target is paralyzed for 1 minute. It repeats the saving throw at the end of each of its turns, ending the effect on a success.' }
    - { name: 'Flame Strike (5th-Level; V)', desc: 'A column of divine flame fills a 10-foot-radius, 40-foot-high cylinder within 60 feet. Creatures in the area make a DC 16 Dexterity saving throw, taking 14 (4d6) fire damage and 14 (4d6) radiant damage on a failure or half damage on a success.' }
    - { name: Multiattack, desc: 'The naga casts a spell and uses its vampiric bite.' }
    - { name: 'Vampiric Bite', desc: 'The naga attacks with its bite. If it hits and the target fails its saving throw against poison, the naga magically gains temporary hit points equal to the poison damage dealt.' }
'bonus actions':
    - { name: Shapeshift, desc: 'The naga changes its form to that of a specific Medium humanoid, a Medium snake-human hybrid with the lower body of a snake, or its true form, which is a Large snake. While shapeshifted, its statistics are unchanged except for its size. It reverts to its true form if it dies.' }
combat:
    - { name: 'The guardian naga casts flame strike on groups of enemies', desc: 'Otherwise it either bites or spits poison. It might cast hold person against a creature immune to poison or one it believes has a low Wisdom. The guardian naga dies in defense of its lair.' }

---
```statblock
monster: Accursed Guardian Naga - A5E
```
