---
statblock: true
name: 'Flesh Guardian - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Construct
cr: 5
ac: 9
hp: 93
hit_dice: '11d8 + 44'
speed: '30 ft.'
stats:
    - 18
    - 8
    - 18
    - 6
    - 10
    - 5
damage_immunities: 'lightning, poison; damage from nonmagical, non-adamantine weapons'
condition_immunities: 'charmed, fatigue, frightened, paralyzed, petrified, poisoned'
senses: 'darkvision 60 ft., passive Perception 10'
languages: "understands the languages of its creator but can't speak"
traits:
    - { name: Berserk, desc: "When the guardian starts its turn while bloodied, roll a d6. On a 6, the guardian goes berserk. While berserk, the guardian attacks the nearest creature it can see. If it can't reach a creature, it attacks an object. The guardian stays berserk until it is destroyed or restored to full hit points." }
    - { name: 'If a berserk guardian can see and hear its creator, the creator can use an action to try to calm it by making a DC 15 Persuasion check', desc: 'On a success, the guardian is no longer berserk.' }
    - { name: 'Fire Fear', desc: 'When the guardian takes fire damage, it is rattled until the end of its next turn.' }
    - { name: 'Immutable Form', desc: 'The guardian is immune to any effect that would alter its form.' }
    - { name: 'Lightning Absorption', desc: 'When the guardian is subjected to lightning damage, it instead regains hit points equal to the lightning damage dealt.' }
    - { name: 'Magic Resistance', desc: 'The guardian has advantage on saving throws against spells and magical effects.' }
    - { name: 'Constructed Nature', desc: "Guardians don't require air, sustenance, or sleep." }
actions:
    - { name: Multiattack, desc: 'The guardian attacks twice with its slam.' }
    - { name: Slam, desc: 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage.' }
    - { name: 'Hurl Object', desc: 'Ranged Weapon Attack: +7 to hit, range 20/60 ft., one target. Hit: 18 (4d6 + 4) bludgeoning damage.' }
    - { name: 'Lightning Bolt (1/Day, While Bloodied)', desc: "An 80-foot-long, 5-foot-wide lightning bolt springs from the guardian's chest. Each creature in the area makes a DC 15 Dexterity saving throw, taking 28 (8d6) lightning damage on a failed save or half damage on a success." }
combat:
    - { name: 'A flesh guardian prefers to slam creatures in melee', desc: "When its Lightning Bolt is available, it uses it immediately, without much regard for catching multiple creatures in the blast. It tends to use its Lightning Bolt on distant and flying attackers. It throws objects only if it can't reach any foes. A flesh guardian possesses a greater sense of self-preservation than most guardians. It avoids fire when it can and may retreat from a battle to save itself." }

---
```statblock
monster: Flesh Guardian - A5E
```
