---
statblock: true
name: 'Trickster Priest - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Humanoid
cr: 2
ac: 12
hp: 32
hit_dice: '5d8 + 10'
speed: '30 ft.'
stats:
    - 12
    - 10
    - 14
    - 12
    - 16
    - 12
saves:
    - { wisdom: 5 }
    - { charisma: 3 }
skillsaves:
    - { medicine: 5 }
    - { insight: 5 }
    - { persuasion: 3 }
    - { religion: 3 }
    - { deception: 3 }
    - { stealth: 2 }
senses: 'passive Perception 13'
languages: 'any two'
traits: {  }
spells:
    spells: ['The priest is a 5th level spellcaster. Their spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). They have the following cleric spells prepared:', 'Cantrips (at will): sacred flame, thaumaturgy, minor illusion', '1st-level (4 slots): ceremony, detect evil and good, healing word, disguise self', '2nd-level (3 slots): lesser restoration, invisibility', '3rd-level (2 slots): spirit guardians, major image']
actions:
    - { name: Mace, desc: 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage. On a hit, the priest can expend a spell slot to deal 7 (2d6) radiant damage, plus an extra 3 (1d6) radiant damage for each level of the spell slot expended above 1st.' }
    - { name: 'Sacred Flame (Cantrip; V, S)', desc: 'One creature the priest can see within 60 feet makes a DC 13 Dexterity saving throw, taking 9 (2d8) radiant damage on a failure. This spell ignores cover.' }
    - { name: 'Invisibility (2nd-Level; V, S, M, Concentration)', desc: 'The priest or a creature they touch is invisible for 1 hour. The spell ends if the invisible creature attacks or casts a spell.' }
    - { name: 'Spirit Guardians (3rd-Level; V, S, M, Concentration)', desc: "Spectral forms surround the priest in a 10-foot radius for 10 minutes. The priest can choose creatures they can see to be unaffected by the spell. Other creatures treat the area as difficult terrain, and when a creature enters the area for the first time on a turn or starts its turn there, it makes a DC 13 Wisdom saving throw, taking 10 (3d6) radiant or necrotic damage (priest's choice) on a failure or half damage on a success." }
'bonus actions':
    - { name: 'Healing Word (1st-Level; V)', desc: "The priest or a living creature within 60 feet regains 5 (1d4 + 3) hit points. The priest can't cast this spell and a 1st-level or higher spell on the same turn." }
    - { name: 'Priests devoted to trickster gods cast spells of deception that make them more akin to rogues than other priests', desc: '' }

---
```statblock
monster: Trickster Priest - A5E
```
