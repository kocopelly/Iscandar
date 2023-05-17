---
statblock: true
name: 'Adult Sapphire Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Dragon
cr: 19
ac: 19
hp: 304
hit_dice: '29d12 + 116'
speed: '40 ft., burrow 30 ft., fly 80 ft.'
stats:
    - 22
    - 22
    - 18
    - 22
    - 20
    - 16
damage_immunities: psychic
condition_immunities: fatigue
saves:
    - { constitution: 10 }
    - { intelligence: 12 }
    - { wisdom: 11 }
    - { charisma: 10 }
skillsaves:
    - { arcana: 12 }
    - { deception: 10 }
    - { history: 12 }
    - { insight: 11 }
    - { perception: 11 }
    - { persuasion: 10 }
senses: 'darkvision 120 ft., passive Perception 24'
languages: 'Common, Deep Speech, Draconic, Undercommon, telepathy 120 ft.'
traits:
    0: { name: 'Legendary Resistance (3/Day)', desc: "When the dragon fails a saving throw, it can choose to succeed instead. When it does, its eyes dull as it briefly loses its connection to the future. Until the end of its next turn, it can't use Foretell, Prognosticate, or Prophesy Doom, and it loses its Predictive Harmonics trait." }
    1: { name: 'Predictive Harmonics', desc: 'The dragon is psionically aware of its own immediate future. The dragon cannot be surprised, and any time the dragon would make a roll with disadvantage, it makes that roll normally instead.' }
    2: { name: 'Psionic Powers', desc: "The dragon's psionic abilities are considered both magical and psionic." }
    3: { name: 'Far Thoughts', desc: 'The dragon is aware of any creature that uses a psionic ability or communicates telepathically within 100 miles of it. As an action, the dragon can psionically observe a creature, object, or location it is familiar with within 100 miles. While observing a subject in this way, the dragon can see, hear, and communicate telepathically, but it is blind and deaf in regard to its physical senses and does not require food or water. The dragon can psionically observe a subject indefinitely and can end this effect and return to its own senses as an action.' }
    4: { name: 'Innate Spellcasting', desc: "The dragon's spellcasting ability is Charisma (save DC 18). It can innately cast the following spells, requiring no material components." }
    traits: [' 3/day each:comprehend languages, detect thoughts, telekinesis, wall of force']
actions:
    - { name: Multiattack, desc: 'The dragon attacks once with its bite and twice with its claws. In place of its bite, it can use Psionic Wave.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 22 (3d10 + 6) piercing damage plus 4 (1d8) psychic damage.' }
    - { name: Claws, desc: 'Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) slashing damage.' }
    - { name: 'Psionic Wave', desc: 'The dragon psionically emits a wave of crushing mental pressure. Each creature within 20 feet makes a DC 18 Wisdom saving throw, taking 16 (3d10) psychic damage on a failed save or half damage on a success. Creatures suffering ongoing psychic damage make this saving throw with disadvantage.' }
    - { name: 'Discognitive Breath (Recharge 56)', desc: 'The dragon unleashes psychic energy in a 60-foot cone. Each creature in that area makes a DC 18 Intelligence saving throw, taking 60 (11d10) psychic damage and 11 (2d10) ongoing psychic damage on a failed save or half as much psychic damage and no ongoing psychic damage on a success. The ongoing damage ends if a creature falls unconscious. A creature can also use an action to ground itself in reality, ending the ongoing damage.' }
    - { name: 'Prognosticate (3/Day)', desc: 'The dragon psionically makes a prediction of an event up to 100 years in the future. This prediction has a 67 percent chance of being perfectly accurate and a 33 percent chance of being partially or wholly wrong. Alternatively, the dragon can choose to gain truesight to a range of 90 feet for 1 minute.' }
legendary_actions:
    - { name: 'The dragon can take 3 legendary actions, choosing from the options below', desc: "Only one legendary action can be used at a time and only at the end of another creature's turn. It regains spent legendary actions at the start of its turn." }
    - { name: Foretell, desc: "The dragon psionically catches a glimpse of a fast-approaching moment and plans accordingly. The dragon rolls a d20 and records the number rolled. Until the end of the dragon's next turn, the dragon can replace the result of any d20 rolled by it or a creature within 120 feet with the foretold number. Each foretold roll can be used only once." }
    - { name: 'Psionic Wave (Costs 2 Actions)', desc: 'The dragon uses Psionic Wave.' }
    - { name: 'Shatter Mind (Costs 2 Actions)', desc: 'The dragon targets a creature within 60 feet, forcing it to make a DC 23 Intelligence saving throw. On a failure, the creature takes 22 (4d10) ongoing psychic damage. An affected creature repeats the saving throw at the end of each of its turns, ending the ongoing psychic damage on a success. A creature can also use an action to ground itself in reality, ending the ongoing damage.' }
combat:
    - { name: 'While individual dragons have their own personalities and tactics, most rely heavily on their breath weapons', desc: 'They use them whenever they can, preferably from maximum distance and while flying above their enemies.' }
    - { name: 'When fighting in the open, dragons often circle above their enemies as they wait for their breath weapons to recharge', desc: "They only close to melee if their enemies deal significant damage with ranged attacks, or if they can savage an enemy cut off from its allies. Once bloodied, dragons become more aggressive, attacking with bite and claws when their breath weapons aren't available." }
    - { name: 'If a dragon is protecting its lair, it utilizes lair features, traps, allies, and architecture such as escape tunnels to keep up a hit-and-run fight, reappearing only when it has a fully-recharged breath weapon', desc: 'If the dragon is forced into melee combat, it uses its bite and claws against a single foe. If it has legendary actions like Roar and Wing Attack, it uses them to disperse its other enemies.' }
    - { name: 'If reduced to less than one-fourth its hit points while fighting in the open, a dragon flies away', desc: 'However, it fights to the death to defend its lair, unless it can regain the upper hand through tricks or bargains.' }

---
```statblock
monster: Adult Sapphire Dragon - A5E
```
