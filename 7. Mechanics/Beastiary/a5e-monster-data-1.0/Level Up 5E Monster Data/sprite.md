---
statblock: true
name: 'Sprite - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Tiny
type: Fey
cr: 1
ac: 14
hp: 2
hit_dice: 1d4
speed: '10 ft., fly 40 ft.'
stats:
    - 2
    - 18
    - 10
    - 14
    - 12
    - 10
skillsaves:
    - { perception: 3 }
    - { stealth: 6 }
senses: 'passive Perception 13'
languages: 'Common, Elvish, Sylvan'
traits:
    - { name: 'Faerie Light', desc: 'As a bonus action, the sprite can cast dim light for 30 feet, or extinguish its glow.' }
actions:
    - { name: Rapier, desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 1 piercing damage plus 3 (1d6) poison damage. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even if it regains hit points, and it is asleep while poisoned in this way.' }
    - { name: Shortbow, desc: 'Ranged Weapon Attack: +6 to hit, range 40/160 ft., one target. Hit: 1 piercing damage plus 3 (1d6) poison damage. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even if it regains hit points, and it is asleep while poisoned in this way.' }
    - { name: Gust, desc: 'A 30-foot cone of strong wind issues from the sprite. Creatures in the area that fail a DC 10 Strength saving throw, and unsecured objects weighing 300 pounds or less, are pushed 10 feet away from the sprite. Unprotected flames in the area are extinguished and gas or vapor is dispersed. Using Gust does not cause the sprite to become visible.' }
    - { name: 'Heart Sight', desc: 'The sprite touches a creature. The creature makes a DC 10 Charisma saving throw. On a failure, the sprite magically reads its mental state and surface thoughts and learns its alignment (if any). Celestials, fiends, and undead automatically fail the saving throw.' }
'bonus actions':
    - { name: Invisibility, desc: 'The sprite and any equipment it wears or carries magically turns invisible until the sprite attacks, becomes incapacitated, or uses a bonus action to become visible.' }
combat:
    - { name: 'The sprite attacks with its shortbow, turns invisible, and moves to conceal its location', desc: 'It attacks with its rapier only if cornered. A group of sprites flee if half their number are defeated.' }

---
```statblock
monster: Sprite - A5E
```
