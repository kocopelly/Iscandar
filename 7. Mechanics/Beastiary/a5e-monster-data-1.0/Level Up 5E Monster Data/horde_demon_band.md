---
statblock: true
name: 'Horde Demon Band - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Fiend
cr: 13
ac: 13
hp: 260
hit_dice: '40d8 + 80'
speed: '30 ft.'
stats:
    - 16
    - 12
    - 14
    - 8
    - 8
    - 8
damage_resistances: 'cold, fire, lightning; damage from nonmagical weapons'
damage_immunities: poison
condition_immunities: poisoned
senses: 'darkvision 120 ft., passive Perception 11'
languages: Abyssal
traits:
    - { name: 'Area Vulnerability', desc: 'The band takes double damage from any effect that targets an area.' }
    - { name: 'Chaotic Evil', desc: 'The band radiates a Chaotic and Evil aura.' }
    - { name: Band, desc: 'The band is composed of 5 or more horde demons. If it is subjected to a spell, attack, or other effect that affects only one target, it takes any damage but ignores other effects. It can share its space with Medium or smaller creatures or objects. The band can move through any opening large enough for one Medium creature without squeezing.' }
    - { name: 'Band Dispersal', desc: 'When the band is reduced to 0 hit points, it turns into 2 (1d4) horde demons with 26 hit points each.' }
actions:
    - { name: Multiattack, desc: 'The band attacks twice.' }
    - { name: 'Mob Attack', desc: 'Melee Weapon Attack: +8 to hit, reach 5 ft., one creature. Hit: 50 (10d6 + 15) slashing damage, or half damage if the band is bloodied.' }
combat:
    - { name: 'The horde demon uses whatever attacks it possesses', desc: 'It flees only if it suffers the frightened condition.' }

---
```statblock
monster: Horde Demon Band - A5E
```
