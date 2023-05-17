---
statblock: true
name: 'Ice Mephit - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Small
type: Elemental
cr: 1
ac: 12
hp: 21
hit_dice: 6d6
speed: '30 ft., fly 30 ft.'
stats:
    - 8
    - 14
    - 10
    - 8
    - 10
    - 10
damage_immunities: 'cold, poison'
condition_immunities: poisoned
'damage vulenrabilities': 'bludgeoning, fire'
skillsaves:
    - { perception: 2 }
    - { stealth: 4 }
senses: 'darkvision 60 ft., passive Perception 12'
languages: 'Aquan, Auran'
traits:
    - { name: 'Death Burst', desc: 'When the mephit dies, it explodes into ice shards. Each creature within 5 feet makes a DC 10 Constitution saving throw, taking 4 (1d8) slashing damage on a failed save or half damage on a success.' }
    - { name: 'False Appearance', desc: 'While motionless, the mephit is indistinguishable from a shard of ice.' }
    - { name: 'Elemental Nature', desc: "A mephit doesn't require air, sustenance, or sleep." }
actions:
    - { name: Claws, desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage plus 2 (1d4) cold damage.' }
    - { name: 'Fog (1/Day)', desc: 'The mephit exhales a cloud of fog, creating a 20-foot-radius sphere of fog centered on the mephit. The fog is heavily obscured to non-mephits. The fog cloud is immobile, spreads around corners, and remains for 10 minutes or until dispersed by a strong wind.' }
    - { name: 'Freezing Breath (1/Day)', desc: 'The mephit exhales a 15-foot cone of ice. Each creature in the area makes a DC 10 Constitution saving throw, taking 5 (2d4) cold damage on a failed save or half damage on a success.' }
combat:
    - { name: 'The mephit uses Freezing Breath and then uses Fog', desc: 'It attacks opponents at an advantage in the fog and uses the fog to help it flee if reduced to 7 hit points or fewer.' }

---
```statblock
monster: Ice Mephit - A5E
```
