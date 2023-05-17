---
statblock: true
name: 'Azer Forgemaster - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Elemental
cr: 4
ac: 16
hp: 78
hit_dice: '12d8 + 24'
speed: '30 ft.'
stats:
    - 18
    - 14
    - 14
    - 12
    - 16
    - 16
damage_immunities: 'fire, poison'
condition_immunities: poisoned
'damage vulenrabilities': cold
senses: 'passive Perception 13'
languages: 'Common, Ignan'
traits:
    - { name: 'Fiery Aura', desc: 'A creature that ends its turn within 5 feet of one or more azers takes 5 (1d10) fire damage. The azer sheds bright light in a 10-foot radius and dim light for an additional 10 feet.' }
actions:
    - { name: Multiattack, desc: 'The azer attacks with its returning hammer and uses Bonfire if available.' }
    - { name: 'Returning Hammer', desc: "Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 feet, one target. Hit: 8 (1d8 + 4) bludgeoning damage plus 7 (2d6) fire damage. The azer's hammer returns to its hand after it's thrown." }
    - { name: 'Bonfire (3/Day)', desc: 'A 5-foot-square space within 60 feet catches fire. A creature takes 10 (3d6) fire damage when it enters this area for the first time on a turn or starts its turn there. A creature can use an action to extinguish this fire.' }
'bonus actions':
    - { name: 'Fire Step', desc: 'While standing in fire, the azer can magically teleport up to 90 feet to a space within fire.' }
combat:
    - { name: 'The azer forgemaster uses its Bonfire ability not only to damage enemies but also to provide tactical movement options for itself and its minions', desc: 'It remains in or near a bonfire. It starts combat by throwing hammers from the back lines if it can, but advances to fight in melee after several allies are killed. When close to death, it uses Fire Step to escape.' }

---
```statblock
monster: Azer Forgemaster - A5E
```
