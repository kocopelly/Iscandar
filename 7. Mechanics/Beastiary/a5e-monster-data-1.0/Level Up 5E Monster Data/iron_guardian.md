---
statblock: true
name: 'Iron Guardian - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Construct
cr: 14
ac: 20
hp: 210
hit_dice: '20d10 + 100'
speed: '30 ft.'
stats:
    - 24
    - 12
    - 20
    - 3
    - 12
    - 1
damage_immunities: 'fire, poison, psychic; damage from nonmagical, non-adamantine weapons'
condition_immunities: 'charmed, fatigue, frightened, paralyzed, petrified, poisoned'
senses: 'darkvision 120 ft., passive Perception 11'
languages: "understands the languages of its creator but can't speak"
traits:
    - { name: 'Fire Absorption', desc: 'When the guardian is subjected to fire damage, it instead regains hit points equal to the fire damage dealt.' }
    - { name: 'Immutable Form', desc: 'The guardian is immune to any effect that would alter its form.' }
    - { name: 'Magic Resistance', desc: 'The guardian has advantage on saving throws against spells and magical effects.' }
    - { name: 'Constructed Nature', desc: "Guardians don't require air, sustenance, or sleep." }
actions:
    - { name: Multiattack, desc: 'The guardian makes two sword attacks.' }
    - { name: Sword, desc: 'Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 29 (4d10 + 7) slashing damage.' }
    - { name: 'Poison Breath (Recharge 56)', desc: 'The guardian exhales poisonous gas in a 15-foot cone. Each creature in the area makes a DC 18 Constitution saving throw, taking 45 (10d8) poison damage on a failure or half damage on a success.' }
reactions:
    - { name: Deflection, desc: 'When missed by a ranged attack by a creature the guardian can see, the guardian redirects the attack against a creature within 60 feet that it can see. The original attacker must reroll the attack against the new target.' }
combat:
    - { name: "The iron guardian's strategy is determined by its programming", desc: 'It may attack the closest enemy, or it may be instructed to attack only certain targets, such as the first one to touch an item it was protecting. It uses its poison breath whenever it can include two or more creatures in the blast. It uses its Deflection reaction to target either the least-armored creature within range or its preferred target.' }

---
```statblock
monster: Iron Guardian - A5E
```
