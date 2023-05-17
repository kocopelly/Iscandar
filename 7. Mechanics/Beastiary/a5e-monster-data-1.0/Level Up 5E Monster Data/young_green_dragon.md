---
statblock: true
name: 'Young Green Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Dragon
cr: 10
ac: 17
hp: 161
hit_dice: '19d10 + 57'
speed: '40 ft., fly 80 ft., swim 40 ft.'
stats:
    - 18
    - 12
    - 16
    - 16
    - 12
    - 14
damage_immunities: poison
condition_immunities: poisoned
saves:
    - { dexterity: 5 }
    - { constitution: 7 }
    - { wisdom: 5 }
    - { charisma: 6 }
skillsaves:
    - { deception: 6 }
    - { insight: 5 }
    - { perception: 5 }
    - { persuasion: 6 }
    - { stealth: 5 }
senses: 'blindsight 30 ft., darkvision 120 ft., passive Perception 18'
languages: 'Common, Draconic, one more'
traits:
    0: { name: Amphibious, desc: 'The dragon can breathe air and water.' }
    1: { name: 'Woodland Stalker', desc: 'When in a forested area, the dragon has advantage on Stealth checks.' }
    2: { name: 'Innate Spellcasting', desc: "The dragon's spellcasting ability is Charisma (save DC 14). It can innately cast the following spells, requiring no material components." }
    traits: [' 3/day each:animal messenger, tongues']
actions:
    - { name: Multiattack, desc: 'The dragon attacks once with its bite and twice with its claws.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 20 (3d10 + 4) piercing damage plus 4 (1d8) poison damage.' }
    - { name: Claw, desc: 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage.' }
    - { name: 'Poison Breath (Recharge 56)', desc: 'The dragon exhales poisonous gas in a 30-foot cone. Each creature in that area makes a DC 15 Constitution saving throw, taking 42 (12d6) poison damage on a failed save or half damage on a success.' }
combat:
    - { name: 'While individual dragons have their own personalities and tactics, most rely heavily on their breath weapons', desc: 'They use them whenever they can, preferably from maximum distance and while flying above their enemies.' }
    - { name: 'When fighting in the open, dragons often circle above their enemies as they wait for their breath weapons to recharge', desc: "They only close to melee if their enemies deal significant damage with ranged attacks, or if they can savage an enemy cut off from its allies. Once bloodied, dragons become more aggressive, attacking with bite and claws when their breath weapons aren't available." }
    - { name: 'If a dragon is protecting its lair, it utilizes lair features, traps, allies, and architecture such as escape tunnels to keep up a hit-and-run fight, reappearing only when it has a fully-recharged breath weapon', desc: 'If the dragon is forced into melee combat, it uses its bite and claws against a single foe. If it has legendary actions like Roar and Wing Attack, it uses them to disperse its other enemies.' }
    - { name: 'If reduced to less than one-fourth its hit points while fighting in the open, a dragon flies away', desc: 'However, it fights to the death to defend its lair, unless it can regain the upper hand through tricks or bargains.' }

---
```statblock
monster: Young Green Dragon - A5E
```
