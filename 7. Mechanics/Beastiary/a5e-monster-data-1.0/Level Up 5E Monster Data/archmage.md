---
statblock: true
name: 'Archmage - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Humanoid
cr: 11
ac: 12
hp: 117
hit_dice: '18d8 + 36'
speed: '30 ft.'
stats:
    - 10
    - 14
    - 14
    - 20
    - 16
    - 14
damage_immunities: 'psychic (with mind blank)'
condition_immunities: 'charmed (with mind blank)'
saves:
    - { intelligence: 9 }
    - { wisdom: 7 }
skillsaves:
    - { arcana: 9 }
    - { insight: 7 }
    - { history: 9 }
    - { perception: 7 }
senses: 'passive Perception 17'
languages: 'any four'
traits:
    - { name: Foresight, desc: "When the foresight spell is active, the archmage can't be surprised and has advantage on ability checks, attack rolls, and saving throws. In addition, other creatures have disadvantage on attack rolls against the archmage." }
    - { name: 'Mind Blank', desc: 'When the mind blank spell is active, the archmage is immune to psychic damage, any effect that would read their emotions or thoughts, divination spells, and the charmed condition.' }
spells:
    spells: ['The archmage is an 18th level spellcaster. Their spellcasting ability is Intelligence (spell save DC 17, +9 to hit with spell attacks). The archmage can cast shield at level 1 and alter self at level 2 without expending a spell slot. They have the following wizard spells prepared:', 'Cantrips (at will): fire bolt, light, mage hand, message, prestidigitation', '1st-level (4 slots): detect magic, identify, mage armor, shield', '2nd-level (4 slots): alter self, detect thoughts, suggestion', '3rd-level (3 slots): counterspell, lightning bolt, sending', '4th-level (3 slots): confusion, hallucinatory terrain, locate creature', '5th-level (3 slots): cone of cold, mislead, scrying', '6th-level (1 slot): globe of invulnerability, true seeing', '7th-level (1 slot): teleport', '8th-level (1 slot): mind blank', '9th-level (1 slot): foresight']
actions:
    - { name: Dagger, desc: 'Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage.' }
    - { name: 'Fire Bolt (Cantrip; V, S)', desc: 'Ranged Spell Attack: +9 to hit, range 120 ft., one target. Hit: 22 (4d10) fire damage.' }
    - { name: 'Lightning Bolt (3rd-Level; V, S, M)', desc: 'A bolt of lightning 5 feet wide and 100 feet long arcs from the archmage. Each creature in the area makes a DC 17 Dexterity saving throw, taking 28 (8d6) lightning damage on a failure or half damage on a success.' }
    - { name: 'Confusion (4th-Level; V, S, M, Concentration)', desc: 'Each creature within 10 feet of a point the archmage can see within 120 feet makes a DC 17 Wisdom saving throw, becoming rattled until the end of its next turn on a success. On a failure, a creature is confused for 1 minute. The target repeats the saving throw at the end of each of its turns, ending the effect on itself on a success.' }
    - { name: 'Cone of Cold (5th-Level; V, S, M)', desc: 'Frost blasts from the archmage in a 60-foot cone. Each creature in the area makes a DC 17 Constitution saving throw, taking 36 (8d8) cold damage on a failure or half damage on a success.' }
    - { name: 'Mislead (5th-Level; S, Concentration)', desc: "The archmage becomes invisible for 1 hour. At the same time, an illusory copy of the archmage appears in their space. The archmage can use an action to move the copy up to 60 feet and have it speak or gesture. The copy is revealed as an illusion with any physical interaction, as solid objects and creatures pass through it. The archmage can use a bonus action to switch between their copy's senses or their own; while using their copy's senses, the archmage's body is blind and deaf. The invisibility, but not the duplicate, ends if the archmage casts another spell." }
    - { name: 'Globe of Invulnerability (6th-Level; V, S, M, Concentration)', desc: "A glimmering, 10-foot-radius sphere appears around the archmage. It remains for 1 minute and doesn't move with the archmage. Any 5th-level or lower spell cast from outside the sphere can't affect anything inside the sphere, even if cast with a higher level spell slot. Targeting something inside the sphere or including the sphere's space in an area has no effect on anything inside." }
    - { name: 'Teleport (7th-Level; V)', desc: 'The archmage teleports to a location they are familiar with on the same plane of existence.' }
reactions:
    - { name: 'Counterspell (3rd-Level; S)', desc: "When a creature the archmage can see within 60 feet casts a spell, the archmage attempts to interrupt it. If the creature is casting a 2nd-level spell or lower, the spell fails. If the creature is casting a 3rd-level or higher spell, the archmage makes an Intelligence check against a DC of 10 + the spell's level. On a success, the spell fails, and the spellcasting creature can use its reaction to try to cast a second spell with the same casting time so long as it uses a spell slot level equal to or less than half the original spell slot. If the archmage casts counterspell with a higher spell slot, the interrupted spell fails if its level is less than that of counterspell." }
    - { name: 'Shield (1st-Level; V, S)', desc: 'When the archmage is hit by an attack or targeted by magic missile, they gain a +5 bonus to AC (including against the triggering attack) and immunity to magic missile. These benefits last until the start of their next turn.' }

---
```statblock
monster: Archmage - A5E
```
