---
statblock: true
name: 'Young Red Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Dragon
cr: 11
ac: 18
hp: 178
hit_dice: '17d10 + 85'
speed: '40 ft., climb 40 ft., fly 80 ft.'
stats:
    - 22
    - 10
    - 20
    - 14
    - 12
    - 18
damage_immunities: fire
saves:
    - { dexterity: 4 }
    - { constitution: 9 }
    - { wisdom: 5 }
    - { charisma: 8 }
skillsaves:
    - { intimidation: 8 }
    - { perception: 5 }
    - { stealth: 4 }
senses: 'blindsight 30 ft., darkvision 120 ft., passive Perception 18'
languages: 'Common, Draconic'
traits:
    0: { name: 'Searing Heat', desc: 'A creature that starts its turn touching the dragon, or touches it or hits it with a melee attack for the first time on a turn, takes 3 (1d6) fire damage.' }
    1: { name: 'Volcanic Tyrant', desc: 'The dragon is immune to the effects of poisonous gases caused by volcanic environments. It also ignores difficult terrain caused by lava.' }
    2: { name: 'Innate Spellcasting', desc: "The dragon's spellcasting ability is Charisma (save DC 16). It can innately cast the following spells, requiring no material components." }
    traits: [' 3/day each:command, hold person']
actions:
    - { name: Multiattack, desc: 'The dragon attacks once with its bite and twice with its claws.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 22 (3d10 + 6) piercing damage plus 4 (1d8) fire damage.' }
    - { name: Claw, desc: 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 15 (2d8 + 6) slashing damage.' }
    - { name: 'Fire Breath (Recharge 56)', desc: 'The dragon exhales a blast of fire that fills a 30-foot cone. Each creature in that area makes a DC 17 Dexterity saving throw, taking 52 (15d6) fire damage on a failed save or half damage on a success. A creature that fails the saving throw also takes 5 (1d10) ongoing fire damage. While affected by this ongoing damage, it is frightened of the dragon. A creature can use an action to end the ongoing damage.' }
combat:
    - { name: 'While individual dragons have their own personalities and tactics, most rely heavily on their breath weapons', desc: 'They use them whenever they can, preferably from maximum distance and while flying above their enemies.' }
    - { name: 'When fighting in the open, dragons often circle above their enemies as they wait for their breath weapons to recharge', desc: "They only close to melee if their enemies deal significant damage with ranged attacks, or if they can savage an enemy cut off from its allies. Once bloodied, dragons become more aggressive, attacking with bite and claws when their breath weapons aren't available." }
    - { name: 'If a dragon is protecting its lair, it utilizes lair features, traps, allies, and architecture such as escape tunnels to keep up a hit-and-run fight, reappearing only when it has a fully-recharged breath weapon', desc: 'If the dragon is forced into melee combat, it uses its bite and claws against a single foe. If it has legendary actions like Roar and Wing Attack, it uses them to disperse its other enemies.' }
    - { name: 'If reduced to less than one-fourth its hit points while fighting in the open, a dragon flies away', desc: 'However, it fights to the death to defend its lair, unless it can regain the upper hand through tricks or bargains.' }

---
```statblock
monster: Young Red Dragon - A5E
```
