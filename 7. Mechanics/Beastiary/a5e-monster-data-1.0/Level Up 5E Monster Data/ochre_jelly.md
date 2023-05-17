---
statblock: true
name: 'Ochre Jelly - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Ooze
cr: 2
ac: 8
hp: 45
hit_dice: '6d10 + 12'
speed: '15 ft., climb 15 ft., swim 15 ft.'
stats:
    - 14
    - 6
    - 14
    - 1
    - 6
    - 1
damage_immunities: 'acid, lightning, slashing'
condition_immunities: 'blinded, charmed, deafened, fatigue, frightened, prone'
senses: 'blindsight 60 ft. (blind beyond this radius), passive Perception 8'
traits:
    - { name: Amorphous, desc: 'The jelly can pass through an opening as narrow as 1 inch wide without squeezing.' }
    - { name: 'Spider Climb', desc: 'The jelly can use its climb speed even on difficult surfaces and upside down on ceilings.' }
    - { name: 'Sunlight Sensitivity', desc: 'While in sunlight, the jelly has disadvantage on attack rolls.' }
    - { name: 'Ooze Nature', desc: "An ooze doesn't require air or sleep." }
actions:
    - { name: Pseudopod, desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage plus 3 (1d6) acid damage, and the target is grappled (escape DC 12). A grappled target takes 3 (1d6) acid damage at the start of each of the jelly's turns." }
reactions:
    - { name: Split, desc: "When a Medium or larger jelly with at least 10 hit points is subjected to lightning or slashing damage, it splits into two jellies that are each one size smaller, freeing any grappled targets. Each new jelly has half the original's hit points (rounded down)." }
combat:
    - { name: 'The ochre jelly grapples passing creatures with its pseudopods', desc: 'Given time, it will grab as many creatures as approach within 5 feet of it. It flees from sunlight.' }

---
```statblock
monster: Ochre Jelly - A5E
```
