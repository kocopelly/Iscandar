---
statblock: true
name: 'Accursed Spirit Naga - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Monstrosity
cr: 8
ac: 16
hp: 85
hit_dice: '10d10 + 30'
speed: '40 ft., swim 40 ft.'
stats:
    - 16
    - 16
    - 16
    - 16
    - 14
    - 16
damage_immunities: poison
condition_immunities: 'charmed, poisoned'
saves:
    - { dexterity: 6 }
    - { constitution: 6 }
    - { wisdom: 5 }
    - { charisma: 6 }
senses: 'darkvision 60 ft., passive Perception 12'
languages: 'Abyssal, Celestial, Common'
traits:
    - { name: Amphibious, desc: 'The naga can breathe air and water.' }
    - { name: 'Magic Resistance', desc: 'The naga has advantage on saving throws against spells and magical effects.' }
actions:
    - { name: Bite, desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage. The target makes a DC 15 Constitution saving throw, taking 28 (8d6) poison damage on a failure or half damage on a success.' }
    - { name: 'Hypnotic Pattern (3rd-Level; V, Concentration)', desc: 'A swirling pattern of light appears at a point within 120 feet of the naga. Each creature within 10 feet of the pattern that can see it makes a DC 14 Wisdom saving throw. On a failure, the creature is charmed for 1 minute. While charmed, the creature is incapacitated and its Speed is 0. The effect ends on a creature if it takes damage or if another creature uses an action to shake it out of its daze.' }
    - { name: 'Lightning Bolt (3rd-Level; V)', desc: 'A bolt of lightning 5 feet wide and 100 feet long arcs from the naga. Each creature in the area makes a DC 14 Dexterity saving throw, taking 28 (8d6) lightning damage on a failure or half damage on a success.' }
    - { name: 'Blight (4th-Level; V, Concentration)', desc: 'The naga targets a living creature or plant within 30 feet, draining moisture and vitality from it. The target makes a DC 14 Constitution saving throw, taking 36 (8d8) necrotic damage on a failure or half damage on a success. Plant creatures have disadvantage on their saving throw and take maximum damage. A nonmagical plant dies.' }
    - { name: Multiattack, desc: 'The naga casts a spell and uses its vampiric bite.' }
    - { name: 'Vampiric Bite', desc: 'The naga attacks with its bite. If it hits and the target fails its saving throw against poison, the naga magically gains temporary hit points equal to the poison damage dealt.' }
reactions:
    - { name: 'Shield (1st-Level; V)', desc: 'When the naga is hit by an attack or targeted by magic missile, it gains a +5 bonus to AC (including against the triggering attack) and immunity to magic missile. These benefits last until the beginning of its next turn.' }
combat:
    - { name: 'The spirit naga tries to cast charm person and dominate person before combat starts', desc: 'In combat, it casts hypnotic pattern or lightning bolt if it can target two or more opponents. Otherwise, it bites in melee or casts blight from a distance. It casts shield whenever necessary. It fights to the death.' }

---
```statblock
monster: Accursed Spirit Naga - A5E
```
