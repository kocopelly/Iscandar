---
statblock: true
name: 'Adult Emerald Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Dragon
cr: 17
ac: 18
hp: 241
hit_dice: '23d12 + 92'
speed: '40 ft., burrow 30 ft., fly 60 ft.'
stats:
    - 22
    - 22
    - 18
    - 22
    - 12
    - 18
damage_resistances: 'psychic, thunder'
condition_immunities: fatigue
saves:
    - { constitution: 10 }
    - { intelligence: 12 }
    - { wisdom: 7 }
    - { charisma: 10 }
skillsaves:
    - { deception: 10 }
    - { history: 12 }
    - { perception: 7 }
    - { stealth: 12 }
senses: 'darkvision 120 ft., passive Perception 17'
languages: 'Common, Deep Speech, Draconic, Undercommon, telepathy 120 ft.'
traits:
    0: { name: 'Legendary Resistance (3/Day)', desc: 'When the dragon fails a saving throw, it can choose to succeed instead. When it does, its eyes flash red as it goes into a fit of rage. Until the end of its next turn, it makes melee attacks against the creature that triggered the saving throw with advantage and with disadvantage against all other creatures.' }
    1: { name: 'Psionic Powers', desc: "The dragon's psionic abilities are considered both magical and psionic." }
    2: { name: 'Far Thoughts', desc: 'The dragon is aware of any creature that uses a psionic ability or communicates telepathically within 100 miles of it. As an action, the dragon can psionically observe a creature, object, or location it is familiar with within 100 miles. While observing a subject in this way, the dragon can see, hear, and communicate telepathically, but it is blind and deaf in regard to its physical senses and does not require food or water. The dragon can psionically observe a subject indefinitely and can end this effect and return to its own senses as an action.' }
    3: { name: 'Innate Spellcasting', desc: "The dragon's spellcasting ability is Charisma (save DC 18). It can innately cast the following spells, requiring no material components." }
    traits: [' 3/day each:confusion, dominate person, hideous laughter, suggestion']
actions:
    - { name: Multiattack, desc: 'The dragon attacks once with its bite and twice with its claws. In place of its bite, it can use Psionic Wave.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 22 (3d10 + 6) piercing damage plus 4 (1d8) thunder damage.' }
    - { name: Claws, desc: 'Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) slashing damage.' }
    - { name: 'Psionic Wave', desc: 'The dragon psionically emits a wave of crushing mental pressure. Each creature within 20 feet makes a DC 18 Wisdom saving throw, taking 16 (3d10) psychic damage on a failed save or half damage on a success. Confused creatures make this saving throw with disadvantage.' }
    - { name: 'Maddening Breath (Recharge 56)', desc: 'The dragon screams, stripping flesh from bones and reason from minds in a 60-foot cone. Each creature in that area makes a DC 18 Constitution saving throw, taking 71 (13d10) thunder damage on a failed save or half damage on a success. Creatures that fail this saving throw by 10 or more are also psionically confused until the end of their next turn.' }
reactions:
    - { name: 'Spiteful Retort (While Bloodied)', desc: 'When a creature the dragon can see damages the dragon, the dragon lashes out with a psionic screech. The attacker makes a DC 15 Wisdom saving throw, taking 18 (4d8) thunder damage on a failed save or half damage on a success. Confused creatures make this saving throw with disadvantage.' }
legendary_actions:
    - { name: 'The dragon can take 3 legendary actions, choosing from the options below', desc: "Only one legendary action can be used at a time and only at the end of another creature's turn. It regains spent legendary actions at the start of its turn." }
    - { name: 'Paranoid Ranting', desc: 'The dragon psionically rants nonsense at a creature that can hear it within 60 feet. The target makes a DC 15 Wisdom saving throw. On a failed save, the creature gains a randomly determined short-term mental stress effect or madness.' }
    - { name: 'Pandorum (Costs 2 Actions)', desc: 'The dragon psionically targets one creature within 60 feet. The target makes a DC 15 Wisdom saving throw, becoming confused on a failure. While confused in this way, the target regards their allies as traitorous enemies. When rolling to determine its actions, treat a roll of 1 to 4 as a result of 8. The target repeats the saving throw at the end of each of its turns, ending the effect on a success.' }
    - { name: 'Psionic Wave (Costs 2 Actions)', desc: 'The dragon makes a psionic wave attack.' }
    - { name: 'Maddening Harmonics (1/Day)', desc: "Each creature of the dragon's choice that can hear within 90 feet makes a DC 15 Wisdom saving throw. On a failure, a creature becomes psionically confused for 1 minute. A creature repeats the saving throw at the end of each of its turns, ending the effect on itself on a success." }
combat:
    - { name: 'While individual dragons have their own personalities and tactics, most rely heavily on their breath weapons', desc: 'They use them whenever they can, preferably from maximum distance and while flying above their enemies.' }
    - { name: 'When fighting in the open, dragons often circle above their enemies as they wait for their breath weapons to recharge', desc: "They only close to melee if their enemies deal significant damage with ranged attacks, or if they can savage an enemy cut off from its allies. Once bloodied, dragons become more aggressive, attacking with bite and claws when their breath weapons aren't available." }
    - { name: 'If a dragon is protecting its lair, it utilizes lair features, traps, allies, and architecture such as escape tunnels to keep up a hit-and-run fight, reappearing only when it has a fully-recharged breath weapon', desc: 'If the dragon is forced into melee combat, it uses its bite and claws against a single foe. If it has legendary actions like Roar and Wing Attack, it uses them to disperse its other enemies.' }
    - { name: 'If reduced to less than one-fourth its hit points while fighting in the open, a dragon flies away', desc: 'However, it fights to the death to defend its lair, unless it can regain the upper hand through tricks or bargains.' }

---
```statblock
monster: Adult Emerald Dragon - A5E
```
