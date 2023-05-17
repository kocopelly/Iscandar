---
statblock: true
name: 'Manticore - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Monstrosity
cr: 3
ac: 14
hp: 68
hit_dice: '8d10 + 24'
speed: '30 ft., fly 50 ft.'
stats:
    - 16
    - 14
    - 16
    - 8
    - 12
    - 8
senses: 'darkvision 60 ft., passive Perception 11'
languages: Common
actions:
    - { name: Multiattack, desc: 'The manticore attacks with its bite and its claws.' }
    - { name: Bite, desc: 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage.' }
    - { name: Claws, desc: 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) slashing damage. If the manticore moves at least 20 feet straight towards the target before the attack, the target makes a DC 13 Strength saving throw, falling prone on a failure.' }
    - { name: Tail, desc: 'Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 7 (1d8 + 3) piercing damage.' }
    - { name: 'Tail Spike Volley (4/Day)', desc: 'The manticore fires tail spikes in a 5-foot-wide, 60-foot-long line. Each creature in the area makes a DC 12 Dexterity saving throw, taking 14 (4d6) piercing damage on a failure or half damage on a success.' }
reactions:
    - { name: 'Tail Whip', desc: 'If a creature the manticore can see hits it with a melee attack, the manticore attacks the attacker with its tail. If it hits, it can fly up to half its fly speed without provoking opportunity attacks from the attacker.' }
combat:
    - { name: 'The manticore fires a tail spike volley from a distance, preferably from the air', desc: 'It then flies past an opponent, attacking with its tail from 10 feet away to avoid opportunity attacks. Finally, it charges at least 20 feet and attacks with its claws and bite. If bloodied, it falls back and uses the rest of its tail spikes. It flees only if its tail spike volleys have been depleted.' }

---
```statblock
monster: Manticore - A5E
```
