---
statblock: true
name: 'Ancient Green Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Gargantuan
type: Dragon
cr: 24
ac: 21
hp: 420
hit_dice: '24d20 + 168'
speed: '40 ft., fly 80 ft., swim 40 ft.'
stats:
    - 26
    - 12
    - 24
    - 20
    - 16
    - 28
damage_immunities: poison
condition_immunities: poisoned
saves:
    - { dexterity: 8 }
    - { constitution: 14 }
    - { wisdom: 10 }
    - { charisma: 11 }
skillsaves:
    - { deception: 11 }
    - { insight: 10 }
    - { perception: 10 }
    - { persuasion: 11 }
    - { stealth: 8 }
senses: 'blindsight 60 ft., darkvision 120 ft., passive Perception 23'
languages: 'Common, Draconic, three more'
traits:
    0: { name: Amphibious, desc: 'The dragon can breathe air and water.' }
    1: { name: 'Legendary Resistance (3/Day)', desc: 'When the dragon fails a saving throw, it can choose to succeed instead. When it does, it sheds some of its scales, which turn into dry leaves and blow away. If it has no more uses of this ability, its Armor Class is reduced to 19 until it finishes a long rest.' }
    2: { name: 'Woodland Stalker', desc: 'When in a forested area, the dragon has advantage on Stealth checks. Additionally, when it speaks in such a place, it can project its voice such that it seems to come from all around, allowing it to remain hidden while speaking.' }
    3: { name: 'Blood Toxicity (While Bloodied)', desc: 'The first time each turn a creature hits the dragon with a melee attack while within 10 feet of it, that creature makes a DC 22 Dexterity saving throw, taking 10 (3d6) poison damage on a failure.' }
    4: { name: 'Innate Spellcasting', desc: "The dragon's spellcasting ability is Charisma (save DC 19). It can innately cast the following spells, requiring no material components." }
    traits: [' 3/day each:animal messenger, tongues, modify memory, scrying', ' 1/day:mass suggestion, telepathic bond']
actions:
    - { name: Multiattack, desc: 'The dragon attacks once with its bite and twice with its claws. In place of its bite attack, it can Spit Poison.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +15 to hit, reach 15 ft., one target. Hit: 30 (4d10 + 8) piercing damage plus 9 (2d8) poison damage.' }
    - { name: Claw, desc: 'Melee Weapon Attack: +15 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) slashing damage.' }
    - { name: Tail, desc: 'Melee Weapon Attack: +15 to hit, reach 20 ft., one target. Hit: 21 (3d8 + 8) bludgeoning damage, and the dragon pushes the target 10 feet away.' }
    - { name: 'Spit Poison', desc: 'The dragon targets a creature within 60 feet, forcing it to make a DC 22 Dexterity saving throw. The creature takes 22 (4d10) poison damage on a failure or half damage on a success. A creature that fails the save is also poisoned for 1 minute. The creature repeats the saving throw at the end of each of its turns, taking 11 (2d10) poison damage on a failure and ending the effect on a success.' }
    - { name: 'Poison Breath (Recharge 56)', desc: 'The dragon exhales poisonous gas in a 90-foot cone. Each creature in that area makes a DC 22 Constitution saving throw, taking 80 (23d6) poison damage on a failed save or half damage on a success. A creature with immunity to poison damage that fails the save takes no damage, but its poison immunity is reduced to resistance for the next hour.' }
    - { name: 'Honeyed Words', desc: "The dragon's words sow doubt in the minds of those who hear them. One creature within 60 feet who can hear and understand the dragon makes a DC 19 Wisdom saving throw. On a failure, the creature must use its reaction, if available, to make one attack against a creature of the dragon's choice with whatever weapon it has to do so, moving up to its speed as part of the reaction if necessary. It need not use any special class features (such as Sneak Attack or Divine Smite) when making this attack. If it can't get in a position to attack the creature, it moves as far as it can toward the target before regaining its senses. A creature immune to being charmed is immune to this ability." }
reactions:
    - { name: 'Tail Attack', desc: 'When a creature the dragon can see within 10 feet hits the dragon with a melee attack, the dragon makes a tail attack against it.' }
legendary_actions:
    - { name: 'The dragon can take 3 legendary actions, choosing from the options below', desc: "Only one legendary action can be used at a time and only at the end of another creature's turn. It regains spent legendary actions at the start of its turn." }
    - { name: 'Honeyed Words', desc: 'The dragon uses Honeyed Words.' }
    - { name: Roar, desc: "Each creature of the dragon's choice within 120 feet that can hear it makes a DC 19 Charisma saving throw. On a failure, it is frightened for 1 minute. A creature repeats the saving throw at the end of its turns, ending the effect on itself on a success. When it succeeds on a saving throw or the effect ends for it, it is immune to Roar for 24 hours." }
    - { name: 'Wing Attack', desc: 'The dragon beats its wings. Each creature within 15 feet makes a DC 22 Dexterity saving throw. On a failure, it is pushed 10 feet away and knocked prone. The dragon can then fly up to half its fly speed.' }
combat:
    - { name: 'While individual dragons have their own personalities and tactics, most rely heavily on their breath weapons', desc: 'They use them whenever they can, preferably from maximum distance and while flying above their enemies.' }
    - { name: 'When fighting in the open, dragons often circle above their enemies as they wait for their breath weapons to recharge', desc: "They only close to melee if their enemies deal significant damage with ranged attacks, or if they can savage an enemy cut off from its allies. Once bloodied, dragons become more aggressive, attacking with bite and claws when their breath weapons aren't available." }
    - { name: 'If a dragon is protecting its lair, it utilizes lair features, traps, allies, and architecture such as escape tunnels to keep up a hit-and-run fight, reappearing only when it has a fully-recharged breath weapon', desc: 'If the dragon is forced into melee combat, it uses its bite and claws against a single foe. If it has legendary actions like Roar and Wing Attack, it uses them to disperse its other enemies.' }
    - { name: 'If reduced to less than one-fourth its hit points while fighting in the open, a dragon flies away', desc: 'However, it fights to the death to defend its lair, unless it can regain the upper hand through tricks or bargains.' }

---
```statblock
monster: Ancient Green Dragon - A5E
```
