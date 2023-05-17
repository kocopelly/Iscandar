---
statblock: true
name: 'Ancient Brass Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Gargantuan
type: Dragon
cr: 22
ac: 20
hp: 367
hit_dice: '21d20 + 147'
speed: '40 ft., burrow 40 ft., fly 80 ft.'
stats:
    - 26
    - 10
    - 24
    - 20
    - 16
    - 18
damage_immunities: fire
saves:
    - { dexterity: 7 }
    - { constitution: 14 }
    - { wisdom: 10 }
    - { charisma: 11 }
skillsaves:
    - { arcana: 12 }
    - { history: 12 }
    - { nature: 12 }
    - { perception: 10 }
    - { persuasion: 11 }
    - { religion: 12 }
    - { stealth: 7 }
senses: 'blindsight 60 ft., darkvision 120 ft., passive Perception 23'
languages: 'Common, Draconic, three more'
traits:
    0: { name: 'Legendary Resistance (3/Day)', desc: 'When the dragon fails a saving throw, it can choose to succeed instead. When it does, some of its scales fall away and turn to sand. If it has no more uses of this ability, its Armor Class is reduced to 18 until it finishes a long rest.' }
    1: { name: Self-Sufficient, desc: 'The brass dragon can subsist on only a quart of water and a pound of food per day.' }
    2: { name: 'Scholar of the Ages', desc: 'The brass dragon gains a d4 expertise die on Intelligence checks made to recall lore. If it fails such a roll, it can expend one use of its Legendary Resistance trait to treat the roll as a 20.' }
    3: { name: 'Innate Spellcasting', desc: "The dragon's spellcasting ability is Charisma (save DC 19). It can innately cast the following spells, requiring no material components." }
    traits: [' 3/day each:comprehend languages, identify, commune, legend lore', ' 1/day:teleport, true seeing']
actions:
    - { name: Multiattack, desc: 'The dragon attacks once with its bite and twice with its claws. In place of its bite, it can use Molten Spit.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +15 to hit, reach 15 ft., one target. Hit: 30 (4d10 + 8) piercing damage plus 9 (2d8) fire damage.' }
    - { name: Claws, desc: 'Melee Weapon Attack: +15 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) slashing damage.' }
    - { name: Tail, desc: 'Melee Weapon Attack: +15 to hit, reach 20 ft., one target. Hit: 21 (3d8 + 8) bludgeoning damage, and the dragon pushes the target 10 feet away.' }
    - { name: 'Staff (Humanoid Form Only)', desc: 'Melee Weapon Attack: +15 to hit, reach 5 ft., one target. Hit: 12 (1d8 + 8) bludgeoning damage.' }
    - { name: 'Molten Spit', desc: 'The dragon targets a creature within 60 feet, forcing it to make a DC 22 Dexterity saving throw. The creature takes 22 (4d10) fire damage on a failure or half damage on a success. A creature that fails the saving throw also takes 11 (2d10) ongoing fire damage. A creature can use an action to end the ongoing damage.' }
    - { name: 'Breath Weapons (Recharge 56)', desc: 'The dragon uses one of the following breath weapons:' }
    - { name: 'Molten Breath', desc: 'The dragon exhales molten glass in a 90-foot-long, 10-foot-wide line. Each creature in the area makes a DC 22 Dexterity saving throw, taking 70 (20d6) fire damage on a failed save or half damage on a success. A creature that fails the save is also blinded until the end of its next turn.' }
    - { name: 'Sleep Breath', desc: 'The dragon exhales sleep gas in a 90-foot cone. Each creature in the area makes a DC 22 Constitution saving throw. On a failure, a creature falls unconscious for 10 minutes or until it takes damage or someone uses an action to wake it.' }
    - { name: 'Change Shape', desc: "The dragon magically takes the shape of a humanoid or beast or changes back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (dragon's choice). In the new form, the dragon's stats are unchanged except for its size. It can't use Molten Spit, Breath Weapons, Tail Attack, or Wing Attack except in dragon form. In beast form, it can attack only with its bite and claws, if appropriate to its form. If the beast form is Large or smaller, the reach of these attacks is reduced to 5 feet. In humanoid form, it can attack only with its staff." }
reactions:
    - { name: 'Tail Attack', desc: 'When a creature the dragon can see within 10 feet hits the dragon with a melee attack, the dragon makes a tail attack against it.' }
legendary_actions:
    - { name: 'The dragon can take 3 legendary actions, choosing from the options below', desc: "Only one legendary action can be used at a time and only at the end of another creature's turn. It regains spent legendary actions at the start of its turn." }
    - { name: Analyze, desc: "The dragon evaluates one creature it can see within 60 feet. It learns the creature's resistances, immunities, vulnerabilities, and current and maximum hit points. That creature's next attack roll against the dragon before the start of the dragon's next turn is made with disadvantage." }
    - { name: Roar, desc: "Each creature of the dragon's choice within 120 feet that can hear it makes a DC 19 Charisma saving throw. On a failure, it is frightened for 1 minute. A creature repeats the saving throw at the end of its turns, ending the effect on itself on a success. When it succeeds on a saving throw or the effect ends for it, it is immune to Roar for 24 hours." }
    - { name: 'Wing Attack', desc: 'The dragon beats its wings. Each creature within 15 feet makes a DC 23 Dexterity saving throw. On a failure, it is pushed 10 feet away and knocked prone. The dragon can then fly up to half its fly speed.' }
combat:
    - { name: 'While individual dragons have their own personalities and tactics, most rely heavily on their breath weapons', desc: 'They use them whenever they can, preferably from maximum distance and while flying above their enemies.' }
    - { name: 'When fighting in the open, dragons often circle above their enemies as they wait for their breath weapons to recharge', desc: "They only close to melee if their enemies deal significant damage with ranged attacks, or if they can savage an enemy cut off from its allies. Once bloodied, dragons become more aggressive, attacking with bite and claws when their breath weapons aren't available." }
    - { name: 'If a dragon is protecting its lair, it utilizes lair features, traps, allies, and architecture such as escape tunnels to keep up a hit-and-run fight, reappearing only when it has a fully-recharged breath weapon', desc: 'If the dragon is forced into melee combat, it uses its bite and claws against a single foe. If it has legendary actions like Roar and Wing Attack, it uses them to disperse its other enemies.' }
    - { name: 'If reduced to less than one-fourth its hit points while fighting in the open, a dragon flies away', desc: 'However, it fights to the death to defend its lair, unless it can regain the upper hand through tricks or bargains.' }

---
```statblock
monster: Ancient Brass Dragon - A5E
```
