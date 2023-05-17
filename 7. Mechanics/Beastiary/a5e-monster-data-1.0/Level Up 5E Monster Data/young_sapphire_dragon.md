---
statblock: true
name: 'Young Sapphire Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Dragon
cr: 10
ac: 18
hp: 161
hit_dice: '19d10 + 57'
speed: '40 ft., burrow 20 ft., fly 80 ft.'
stats:
    - 18
    - 18
    - 16
    - 18
    - 16
    - 14
damage_immunities: psychic
condition_immunities: fatigue
saves:
    - { constitution: 7 }
    - { intelligence: 8 }
    - { wisdom: 7 }
    - { charisma: 6 }
skillsaves:
    - { arcana: 8 }
    - { deception: 6 }
    - { history: 8 }
    - { insight: 7 }
    - { perception: 7 }
    - { persuasion: 6 }
senses: 'darkvision 120 ft., passive Perception 20'
languages: 'Common, Deep Speech, Draconic, Undercommon, telepathy 120 ft.'
traits:
    0: { name: 'Far Thoughts', desc: 'The dragon is aware of any creature that uses a psionic ability or communicates telepathically within 100 miles of it. As an action, the dragon can psionically observe a creature, object, or location it is familiar with within 100 miles. While observing a subject in this way, the dragon can see, hear, and communicate telepathically, but it is blind and deaf in regard to its physical senses and does not require food or water. The dragon can psionically observe a subject indefinitely and can end this effect and return to its own senses as an action.' }
    1: { name: 'Innate Spellcasting', desc: "The dragon's spellcasting ability is Charisma (save DC 15). It can innately cast the following spells, requiring no material components." }
    traits: [' 3/day each:comprehend languages, detect thoughts']
actions:
    - { name: Multiattack, desc: 'The dragon attacks once with its bite and twice with its claws.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 20 (3d10 + 4) piercing damage plus 4 (1d8) psychic damage.' }
    - { name: Claws, desc: 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage.' }
    - { name: 'Discognitive Breath (Recharge 56)', desc: 'The dragon unleashes psychic energy in a 30-foot cone. Each creature in that area makes a DC 15 Intelligence saving throw, taking 49 (9d10) psychic damage on a failed save or half damage on a success.' }
combat:
    - { name: 'While individual dragons have their own personalities and tactics, most rely heavily on their breath weapons', desc: 'They use them whenever they can, preferably from maximum distance and while flying above their enemies.' }
    - { name: 'When fighting in the open, dragons often circle above their enemies as they wait for their breath weapons to recharge', desc: "They only close to melee if their enemies deal significant damage with ranged attacks, or if they can savage an enemy cut off from its allies. Once bloodied, dragons become more aggressive, attacking with bite and claws when their breath weapons aren't available." }
    - { name: 'If a dragon is protecting its lair, it utilizes lair features, traps, allies, and architecture such as escape tunnels to keep up a hit-and-run fight, reappearing only when it has a fully-recharged breath weapon', desc: 'If the dragon is forced into melee combat, it uses its bite and claws against a single foe. If it has legendary actions like Roar and Wing Attack, it uses them to disperse its other enemies.' }
    - { name: 'If reduced to less than one-fourth its hit points while fighting in the open, a dragon flies away', desc: 'However, it fights to the death to defend its lair, unless it can regain the upper hand through tricks or bargains.' }

---
```statblock
monster: Young Sapphire Dragon - A5E
```
