---
statblock: true
name: 'Young Silver Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Dragon
cr: 10
ac: 18
hp: 157
hit_dice: '15d10 + 75'
speed: '40 ft., fly 80 ft.'
stats:
    - 22
    - 14
    - 20
    - 14
    - 10
    - 18
damage_immunities: cold
saves:
    - { dexterity: 6 }
    - { constitution: 9 }
    - { wisdom: 4 }
    - { charisma: 8 }
skillsaves:
    - { arcana: 6 }
    - { history: 6 }
    - { perception: 4 }
    - { stealth: 6 }
senses: 'blindsight 30 ft., darkvision 120 ft., passive Perception 17'
languages: 'Common, Draconic'
traits:
    0: { name: 'Cloud Strider', desc: 'The dragon suffers no harmful effects from high altitudes.' }
    1: { name: 'Innate Spellcasting', desc: "The dragon's spellcasting ability is Charisma (save DC 17). It can innately cast the following spells, requiring no material components." }
    traits: [' 3/day each:charm person, faerie fire']
actions:
    - { name: Multiattack, desc: 'The dragon attacks with its bite and twice with its claws.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 22 (3d10 + 6) piercing damage plus 4 (1d8) cold damage.' }
    - { name: Claws, desc: 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 15 (2d8 + 6) slashing damage.' }
    - { name: 'Breath Weapons (Recharge 56)', desc: 'The dragon uses one of the following breath weapons:' }
    - { name: 'Frost Breath', desc: 'The dragon exhales freezing wind in a 30-foot cone. Each creature in the area makes a DC 17 Constitution saving throw, taking 40 (9d8) cold damage on a failed save or half damage on a success.' }
    - { name: 'Paralyzing Breath', desc: 'The dragon exhales paralytic gas in a 30-foot cone. Each creature in the area must succeed on a DC 17 Constitution saving throw or be paralyzed until the end of its next turn.' }
combat:
    - { name: 'While individual dragons have their own personalities and tactics, most rely heavily on their breath weapons', desc: 'They use them whenever they can, preferably from maximum distance and while flying above their enemies.' }
    - { name: 'When fighting in the open, dragons often circle above their enemies as they wait for their breath weapons to recharge', desc: "They only close to melee if their enemies deal significant damage with ranged attacks, or if they can savage an enemy cut off from its allies. Once bloodied, dragons become more aggressive, attacking with bite and claws when their breath weapons aren't available." }
    - { name: 'If a dragon is protecting its lair, it utilizes lair features, traps, allies, and architecture such as escape tunnels to keep up a hit-and-run fight, reappearing only when it has a fully-recharged breath weapon', desc: 'If the dragon is forced into melee combat, it uses its bite and claws against a single foe. If it has legendary actions like Roar and Wing Attack, it uses them to disperse its other enemies.' }
    - { name: 'If reduced to less than one-fourth its hit points while fighting in the open, a dragon flies away', desc: 'However, it fights to the death to defend its lair, unless it can regain the upper hand through tricks or bargains.' }

---
```statblock
monster: Young Silver Dragon - A5E
```
