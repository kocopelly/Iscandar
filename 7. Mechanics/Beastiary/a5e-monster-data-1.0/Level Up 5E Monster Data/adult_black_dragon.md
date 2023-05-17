---
statblock: true
name: 'Adult Black Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Dragon
cr: 17
ac: 19
hp: 253
hit_dice: '22d12 + 110'
speed: '40 ft., fly 80 ft., swim 40 ft.'
stats:
    - 22
    - 14
    - 20
    - 14
    - 12
    - 16
damage_immunities: acid
saves:
    - { dexterity: 8 }
    - { constitution: 11 }
    - { wisdom: 7 }
    - { charisma: 9 }
skillsaves:
    - { history: 8 }
    - { perception: 7 }
    - { stealth: 8 }
senses: 'blindsight 60 ft., darkvision 120 ft., passive Perception 20'
languages: 'Common, Draconic'
traits:
    0: { name: Ambusher, desc: "When submerged in water, the dragon has advantage on Stealth checks. If the dragon hits a creature that can't see it with its bite, it can deal piercing damage and grapple the target simultaneously." }
    1: { name: Amphibious, desc: 'The dragon can breathe air and water.' }
    2: { name: 'Legendary Resistance (3/Day)', desc: 'When the dragon fails a saving throw, it can choose to succeed instead. When it does, it sheds some of its scales, which turn to mud. If it has no more uses of this ability, its Armor Class is reduced to 17 until it finishes a long rest.' }
    3: { name: 'Ruthless (1/Round)', desc: 'After scoring a critical hit on its turn, the dragon can immediately make one claw attack.' }
    4: { name: 'Innate Spellcasting', desc: "The dragon's spellcasting ability is Charisma (save DC 17). It can innately cast the following spells, requiring no material components." }
    traits: [' 3/day each:fog cloud, pass without trace, legend lore, speak with dead']
actions:
    - { name: Multiattack, desc: 'The dragon attacks once with its bite and twice with its claws. In place of its bite attack, it can use Acid Spit.' }
    - { name: Bite, desc: "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 22 (3d10 + 6) piercing damage plus 4 (1d8) acid damage. Instead of dealing piercing damage, the dragon can grapple the target (escape DC 20), and a Large or smaller creature grappled in this way is restrained. While grappling a creature, the dragon can't bite or use Acid Spit against another target." }
    - { name: Claw, desc: 'Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) slashing damage.' }
    - { name: Tail, desc: 'Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage, and the dragon pushes the target 10 feet away.' }
    - { name: 'Acid Spit', desc: 'The dragon targets a creature within 60 feet, forcing it to make a DC 19 Dexterity saving throw. The creature takes 22 (4d10) acid damage on a failure or half damage on a success. A creature that fails the save also takes 5 (1d10) ongoing acid damage. A creature can use an action to end the ongoing damage.' }
    - { name: 'Acid Breath (Recharge 56)', desc: 'The dragon exhales sizzling acid in a 60-foot-long, 5-foot-wide line. Each creature in that area makes a DC 19 Dexterity saving throw, taking 63 (14d8) acid damage on a failed save or half damage on a success. A creature that fails the save is blinded until the end of its next turn.' }
reactions:
    - { name: 'Tail Attack', desc: 'When a creature the dragon can see within 10 feet hits the dragon with a melee attack, the dragon makes a tail attack against it.' }
legendary_actions:
    - { name: 'The dragon can take 3 legendary actions, choosing from the options below', desc: "Only one legendary action can be used at a time and only at the end of another creature's turn. It regains spent legendary actions at the start of its turn." }
    - { name: Darkness, desc: "The dragon creates a 20-foot-radius sphere of magical darkness originating from a point it can see within 120 feet. Darkvision can't penetrate this darkness. The darkness lasts for 1 minute or until the dragon uses this action again." }
    - { name: Roar, desc: "Each creature of the dragon's choice within 120 feet that can hear it makes a DC 17 Charisma saving throw. On a failure, it is frightened for 1 minute. A creature repeats the saving throw at the end of its turns, ending the effect on itself on a success. When it succeeds on a saving throw or the effect ends for it, it is immune to Roar for 24 hours." }
    - { name: 'Wing Attack', desc: 'The dragon beats its wings. Each creature within 15 feet makes a DC 20 Dexterity saving throw. On a failure, it is pushed 10 feet away and knocked prone. The dragon can then fly up to half its fly speed.' }
combat:
    - { name: 'While individual dragons have their own personalities and tactics, most rely heavily on their breath weapons', desc: 'They use them whenever they can, preferably from maximum distance and while flying above their enemies.' }
    - { name: 'When fighting in the open, dragons often circle above their enemies as they wait for their breath weapons to recharge', desc: "They only close to melee if their enemies deal significant damage with ranged attacks, or if they can savage an enemy cut off from its allies. Once bloodied, dragons become more aggressive, attacking with bite and claws when their breath weapons aren't available." }
    - { name: 'If a dragon is protecting its lair, it utilizes lair features, traps, allies, and architecture such as escape tunnels to keep up a hit-and-run fight, reappearing only when it has a fully-recharged breath weapon', desc: 'If the dragon is forced into melee combat, it uses its bite and claws against a single foe. If it has legendary actions like Roar and Wing Attack, it uses them to disperse its other enemies.' }
    - { name: 'If reduced to less than one-fourth its hit points while fighting in the open, a dragon flies away', desc: 'However, it fights to the death to defend its lair, unless it can regain the upper hand through tricks or bargains.' }

---
```statblock
monster: Adult Black Dragon - A5E
```
