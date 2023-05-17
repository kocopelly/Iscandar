---
statblock: true
name: 'Stone Colossus - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Gargantuan
type: Construct
cr: 16
ac: 17
hp: 263
hit_dice: '17d20 + 85'
speed: '30 ft.'
stats:
    - 22
    - 10
    - 20
    - 3
    - 12
    - 1
damage_immunities: 'poison, psychic; damage from nonmagical, non-adamantine weapons'
condition_immunities: 'charmed, fatigue, frightened, paralyzed, petrified, poisoned'
senses: 'darkvision 120 ft., passive Perception 11'
languages: "understands the languages of its creator but can't speak"
traits:
    - { name: 'Immutable Form', desc: 'The guardian is immune to any effect that would alter its form.' }
    - { name: 'Magic Resistance', desc: 'The guardian has advantage on saving throws against spells and magical effects.' }
    - { name: 'Constructed Nature', desc: "Guardians don't require air, sustenance, or sleep." }
    - { name: 'Legendary Resistance (2/Day)', desc: 'If the colossus fails a saving throw, it can choose to succeed instead. When it does so, it crumbles and cracks, losing 20 hit points.' }
    - { name: 'Siege Monster', desc: 'The colossus deals double damage to objects and structures.' }
actions:
    - { name: Multiattack, desc: 'The guardian attacks twice with its slam.' }
    - { name: Slam, desc: 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage.' }
    - { name: Rock, desc: 'Ranged Weapon Attack: +10 to hit, range 60/240 ft., one target. Hit: 30 (7d6 + 6) bludgeoning damage. The target makes a DC 18 Strength saving throw, falling prone on a failure.' }
'bonus actions':
    - { name: 'Slow (Recharge 56)', desc: 'The guardian targets one or more creatures within 30 feet. Each target makes a DC 17 Wisdom saving throw. On a failure, the target is slowed for 1 minute. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.' }
legendary_actions:
    - { name: 'The colossus can take 2 legendary actions, choosing from the options below', desc: "Only one legendary action can be used at a time and only at the end of another creature's turn. It regains spent legendary actions at the start of its turn." }
    - { name: Seize, desc: "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 16 (4d4 + 6) bludgeoning damage, and the target is grappled (escape DC 18). Until this grapple ends, the target is restrained, and the colossus can't seize a different creature." }
    - { name: Fling, desc: 'The colossus throws one Large or smaller object or creature it is grappling up to 60 feet. The target lands prone and takes 21 (6d6) bludgeoning damage. If the colossus throws the target at another creature, that creature makes a DC 18 Dexterity saving throw, taking the same damage on a failure.' }
    - { name: Stomp, desc: 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 20 (4d6 + 6) bludgeoning damage. If the target is a Large or smaller creature, it makes a DC 18 Strength check, falling prone on a failure.' }
    - { name: 'Bolt from the Blue (Costs 2 Actions)', desc: 'If the colossus is outside, it calls a bolt of energy down from the sky, hitting a point on the ground or water within 120 feet. Each creature in a 10-foot-radius, sky-high cylinder centered on that point makes a DC 17 Dexterity saving throw, taking 28 (8d6) lightning damage on a failed save or half damage on a success. The colossus can choose to make the bolt deal fire or radiant damage instead of lightning.' }
combat:
    - { name: "The stone guardian's strategy is determined by its programming", desc: "Most commonly, it attacks the closest enemy first. It moves to include at least two creatures within range before using Slow. It throws a rock or other object if it can't reach an enemy on its turn." }

---
```statblock
monster: Stone Colossus - A5E
```
