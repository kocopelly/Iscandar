---
statblock: true
name: 'Spark Mephit - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Small
type: Elemental
cr: 1
ac: 12
hp: 17
hit_dice: 5d6
speed: '30 ft., fly 30 ft.'
stats:
    - 8
    - 14
    - 10
    - 8
    - 10
    - 12
damage_immunities: 'lightning, poison'
condition_immunities: poisoned
senses: 'darkvision 60 ft., passive Perception 10'
languages: 'Auran, Ignan'
traits:
    - { name: 'Death Burst', desc: 'When the mephit dies, its Spark Form recharges, and the mephit uses it before it dies.' }
    - { name: 'Elemental Nature', desc: "A mephit doesn't require air, sustenance, or sleep." }
actions:
    - { name: Claws, desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage plus 2 (1d4) lightning damage.' }
    - { name: 'Spark Form (Recharge 6)', desc: "The mephit transforms into an arc of lightning and flies up to 20 feet without provoking opportunity attacks. During this movement, the mephit can pass through other creatures' spaces. Whenever it moves through another creature's space for the first time during this movement, that creature makes a DC 12 Dexterity saving throw, taking 5 (2d4) lightning damage on a failed save or half damage on a success. The mephit then reverts to its original form." }
    - { name: 'Faerie Flame (1/Day)', desc: 'Each creature within 10 feet of the mephit makes a DC 11 Dexterity saving throw. On a failure, the creature is magically outlined in blue light for 1 minute. While outlined, the creature gains no benefit from being invisible and attack rolls against it are made with advantage.' }
combat:
    - { name: 'The mephit uses Spark Form and then attacks with its claws', desc: 'If multiple spark mephits are present, one uses Faerie Flame. It fights to the death.' }

---
```statblock
monster: Spark Mephit - A5E
```
