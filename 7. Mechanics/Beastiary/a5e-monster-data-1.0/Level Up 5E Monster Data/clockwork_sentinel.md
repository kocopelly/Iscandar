---
statblock: true
name: 'Clockwork Sentinel - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Construct
cr: 4
ac: 18
hp: 60
hit_dice: '8d8 + 24'
speed: '35 ft.'
stats:
    - 16
    - 12
    - 16
    - 1
    - 6
    - 1
damage_immunities: 'poison, psychic'
condition_immunities: 'blinded, charmed, deafened, exhaustion, frightened, paralyzed, petrified, poisoned'
skillsaves:
    - { athletics: 5 }
    - { perception: 0 }
    - { survival: 0 }
senses: 'blindsight 120 ft. (blind beyond that range), passive Perception 12'
traits:
    - { name: 'False Appearance', desc: 'While motionless, the sentinel is indistinguishable from normal armor.' }
    - { name: 'Clockwork Nature', desc: "A clockwork doesn't require air, nourishment, or rest, and is immune to disease." }
    - { name: 'Immutable Form', desc: 'The clockwork is immune to any effect that would alter its form.' }
actions:
    - { name: Multiattack, desc: 'The sentinel attacks three times.' }
    - { name: Halberd, desc: 'Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 8 (1d10 + 3) slashing damage.' }
    - { name: 'Calculated Sweep', desc: 'The sentinel makes a melee attack against each creature of its choice within 10 feet. On a critical hit, the target makes a DC 13 Strength saving throw, falling prone on a failure.' }
reactions:
    - { name: Parry, desc: 'The sentinel adds 2 to its AC against one melee attack that would hit it.' }
'bonus actions':
    - { name: 'Overclock (Recharge 56)', desc: 'The sentinel takes the Dash action.' }
combat:
    - { name: 'The clockwork sentinel attacks unauthorized creatures, pursuing them for up to 1 mile if they flee the area the sentinel has been programmed to guard', desc: '' }

---
```statblock
monster: Clockwork Sentinel - A5E
```
