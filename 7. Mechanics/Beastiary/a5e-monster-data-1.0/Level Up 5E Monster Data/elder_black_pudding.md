---
statblock: true
name: 'Elder Black Pudding - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Ooze
cr: 8
ac: 7
hp: 171
hit_dice: '18d12 + 54'
speed: '20 ft., climb 20 ft., swim 20 ft.'
stats:
    - 16
    - 4
    - 16
    - 1
    - 6
    - 1
damage_immunities: 'acid, cold, lightning, slashing'
condition_immunities: 'blinded, charmed, deafened, fatigue, frightened, prone'
senses: 'blindsight 60 ft. (blind beyond this radius), passive Perception 8'
traits:
    - { name: Amorphous, desc: 'The pudding can pass through an opening as narrow as 1 inch wide without squeezing.' }
    - { name: 'Corrosive Body', desc: 'A creature that touches the pudding or hits it with a melee attack while within 5 feet takes 9 (2d8) acid damage. A nonmagical weapon made of metal or wood that hits the black pudding corrodes after dealing damage, taking a permanent -1 penalty to damage rolls per hit. If this penalty reaches -5, the weapon is destroyed. Wooden or metal nonmagical ammunition is destroyed after dealing damage. Any other metal or organic object that touches it takes 9 (2d8) acid damage.' }
    - { name: 'Spider Climb', desc: 'The pudding can use its climb speed even on difficult surfaces and upside down on ceilings.' }
    - { name: 'Sunlight Sensitivity', desc: 'While in sunlight, the pudding has disadvantage on attack rolls.' }
    - { name: 'Ooze Nature', desc: "An ooze doesn't require air or sleep." }
actions:
    - { name: Pseudopod, desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage plus 9 (2d8) acid damage. Nonmagical armor worn by the target corrodes, taking a permanent -1 penalty to its AC protection per hit. If the penalty reduces the armor's AC protection to 10, the armor is destroyed." }
    - { name: Multiattack, desc: "The pudding makes two pseudopod attacks. The pudding can't use Multiattack after it splits for the first time." }
reactions:
    - { name: Split, desc: "When a Medium or larger pudding with at least 10 hit points is subjected to lightning or slashing damage, it splits into two puddings that are each one size smaller. Each new pudding has half the original's hit points (rounded down)." }
combat:
    - { name: 'The pudding lurks on walls or ceilings or conceals itself in shadows', desc: 'It attacks creatures who venture into range and pursues the closest creature. It retreats only if exposed to sunlight, in which case it tries to climb away or squeeze into a crack.' }

---
```statblock
monster: Elder Black Pudding - A5E
```
