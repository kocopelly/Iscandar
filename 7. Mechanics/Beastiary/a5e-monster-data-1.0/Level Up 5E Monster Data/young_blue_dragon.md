---
statblock: true
name: 'Young Blue Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Dragon
cr: 10
ac: 18
hp: 152
hit_dice: '16d10 + 64'
speed: '40 ft., burrow 20 ft., fly 80 ft., swim 20 ft.'
stats:
    - 20
    - 10
    - 18
    - 14
    - 12
    - 16
damage_immunities: lightning
saves:
    - { dexterity: 4 }
    - { constitution: 8 }
    - { wisdom: 5 }
    - { charisma: 7 }
skillsaves:
    - { perception: 5 }
    - { stealth: 4 }
    - { survival: 5 }
senses: 'blindsight 30 ft., tremorsense 30 ft., darkvision 120 ft., passive Perception 18'
languages: 'Common, Draconic'
traits:
    0: { name: 'Desert Farer', desc: 'The dragon ignores difficult terrain or obscurement caused by sand or gravel, even while flying. Additionally, it ignores the effects of extreme heat.' }
    1: { name: 'Dune Splitter', desc: 'The dragon can remain submerged in sand and gravel for up to 4 hours. It has advantage on Stealth checks to hide in this way.' }
    2: { name: 'Innate Spellcasting', desc: "The dragon's spellcasting ability is Charisma (save DC 15). It can innately cast the following spells, requiring no material components." }
    traits: [' 3/day each:blur, silent image']
actions:
    - { name: Multiattack, desc: 'The dragon attacks once with its bite and twice with its claws.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 21 (3d10 + 5) piercing damage plus 4 (1d8) lightning damage.' }
    - { name: Claw, desc: 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) slashing damage.' }
    - { name: 'Lightning Breath (Recharge 56)', desc: "The dragon exhales a 60-foot-long, 5-foot-wide line of lightning. Each creature in that area makes a DC 16 Dexterity saving throw, taking 44 (8d10) lightning damage on a failed save or half damage on a success. A creature that fails the save can't take reactions until the end of its next turn." }
combat:
    - { name: 'While individual dragons have their own personalities and tactics, most rely heavily on their breath weapons', desc: 'They use them whenever they can, preferably from maximum distance and while flying above their enemies.' }
    - { name: 'When fighting in the open, dragons often circle above their enemies as they wait for their breath weapons to recharge', desc: "They only close to melee if their enemies deal significant damage with ranged attacks, or if they can savage an enemy cut off from its allies. Once bloodied, dragons become more aggressive, attacking with bite and claws when their breath weapons aren't available." }
    - { name: 'If a dragon is protecting its lair, it utilizes lair features, traps, allies, and architecture such as escape tunnels to keep up a hit-and-run fight, reappearing only when it has a fully-recharged breath weapon', desc: 'If the dragon is forced into melee combat, it uses its bite and claws against a single foe. If it has legendary actions like Roar and Wing Attack, it uses them to disperse its other enemies.' }
    - { name: 'If reduced to less than one-fourth its hit points while fighting in the open, a dragon flies away', desc: 'However, it fights to the death to defend its lair, unless it can regain the upper hand through tricks or bargains.' }

---
```statblock
monster: Young Blue Dragon - A5E
```
