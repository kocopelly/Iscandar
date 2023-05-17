---
statblock: true
name: 'Young Earth Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Dragon
cr: 10
ac: 18
hp: 161
hit_dice: '17d10 + 68'
speed: '40 ft., fly 40 ft., burrow 60 ft.'
stats:
    - 18
    - 12
    - 18
    - 12
    - 16
    - 10
damage_resistances: 'damage from nonmagical weapons'
condition_immunities: petrified
saves:
    - { strength: 8 }
    - { constitution: 8 }
    - { intelligence: 5 }
    - { wisdom: 7 }
    - { charisma: 4 }
skillsaves:
    - { athletics: 8 }
    - { insight: 7 }
    - { nature: 5 }
    - { perception: 7 }
senses: 'darkvision 120 ft., tremorsense 60 ft., passive Perception 20'
languages: 'Common, Draconic, Terran'
traits:
    0: { name: 'Earth Glide', desc: 'The dragon can burrow through nonmagical, unworked earth and stone without disturbing it.' }
    1: { name: 'False Appearance', desc: 'While the dragon remains motionless within its linked area, it is indistinguishable from a natural rocky outcropping.' }
    2: { name: 'Essence Link', desc: 'The essence dragon is spiritually linked to a specific area or landmark. The dragon gains no benefit from a long rest when more than 1 mile away from its linked area. If the dragon dies, the area it is linked to loses its vital essence until it forms a new essence dragon, which can take centuries. When a creature first enters an area that has lost its vital essence in this way, they gain a level of fatigue and a level of strife. This fatigue and strife can be removed only by completing a long rest outside the area.' }
    3: { name: 'Innate Spellcasting', desc: "The dragon's spellcasting ability is Charisma (save DC 12). It can innately cast the following spells, requiring no material components." }
    traits: [' 3/day each:locate animals or plants, spike growth']
actions:
    - { name: Multiattack, desc: 'The dragon attacks once with its bite and twice with its slam.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 22 (4d10 + 4) piercing damage.' }
    - { name: Slam, desc: 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage.' }
    - { name: 'Scouring Breath (Recharge 56)', desc: 'The dragon exhales scouring sand and stones in a 30-foot cone. Each creature in that area makes a DC 16 Dexterity saving throw, taking 38 (11d6) slashing damage on a failed save or half damage on a success.' }
combat:
    - { name: 'While individual dragons have their own personalities and tactics, most rely heavily on their breath weapons', desc: 'They use them whenever they can, preferably from maximum distance and while flying above their enemies.' }
    - { name: 'When fighting in the open, dragons often circle above their enemies as they wait for their breath weapons to recharge', desc: "They only close to melee if their enemies deal significant damage with ranged attacks, or if they can savage an enemy cut off from its allies. Once bloodied, dragons become more aggressive, attacking with bite and claws when their breath weapons aren't available." }
    - { name: 'If a dragon is protecting its lair, it utilizes lair features, traps, allies, and architecture such as escape tunnels to keep up a hit-and-run fight, reappearing only when it has a fully-recharged breath weapon', desc: 'If the dragon is forced into melee combat, it uses its bite and claws against a single foe. If it has legendary actions like Roar and Wing Attack, it uses them to disperse its other enemies.' }
    - { name: 'If reduced to less than one-fourth its hit points while fighting in the open, a dragon flies away', desc: 'However, it fights to the death to defend its lair, unless it can regain the upper hand through tricks or bargains.' }

---
```statblock
monster: Young Earth Dragon - A5E
```
