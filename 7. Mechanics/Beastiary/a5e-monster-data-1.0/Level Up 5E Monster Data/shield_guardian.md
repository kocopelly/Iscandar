---
statblock: true
name: 'Shield Guardian - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Construct
cr: 7
ac: 17
hp: 133
hit_dice: '14d10 + 56'
speed: '30 ft.'
stats:
    - 18
    - 10
    - 18
    - 6
    - 10
    - 3
damage_immunities: poison
condition_immunities: 'charmed, fatigue, frightened, paralyzed, petrified, poisoned'
senses: 'darkvision 60 ft., passive Perception 10'
languages: "understands all languages but can't speak"
traits:
    - { name: Amulet, desc: "The guardian is magically bound to an amulet. It knows the distance and direction to the amulet while it is on the same plane of existence. Whoever wears the amulet becomes the guardian's master and can magically command the guardian to travel to it." }
    - { name: 'Immutable Form', desc: 'The guardian is immune to any effect that would alter its form.' }
    - { name: 'Magic Resistance', desc: 'The guardian has advantage on saving throws against spells and magical effects.' }
    - { name: 'Spell Storing', desc: "A spellcaster wearing the guardian's amulet can use the guardian to store a spell. The spellcaster casts a spell using a 4th-level or lower spell slot on the guardian, choosing any spell parameters. The spell has no effect when thus cast. The guardian can cast this spell once, using no components, when ordered to do so by its master or under other predefined circumstances. When a spell is stored in the guardian, any previously stored spell is lost." }
    - { name: 'Constructed Nature', desc: "Guardians don't require air, sustenance, or sleep." }
actions:
    - { name: Multiattack, desc: 'The guardian attacks twice with its fist.' }
    - { name: Fist, desc: 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage.' }
    - { name: Self-Repair, desc: 'The guardian regains 15 hit points.' }
reactions:
    - { name: 'Absorb Damage', desc: 'If the guardian is within 60 feet of its master when the master takes damage, half the damage (rounded up) is transferred to the guardian.' }
    - { name: Shield, desc: "If the guardian is within 5 feet of its master when the master is attacked, the guardian grants a +3 bonus to its master's AC." }
combat:
    - { name: "The shield guardian follows its master's orders", desc: 'If not given orders, it moves to stay within 60 feet of its master and attacks anyone who attacks its master or itself (in that order). If no one is wearing its amulet, it defends itself and performs self-repair but takes no other actions.' }

---
```statblock
monster: Shield Guardian - A5E
```
