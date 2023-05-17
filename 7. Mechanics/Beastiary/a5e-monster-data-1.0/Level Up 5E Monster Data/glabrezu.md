---
statblock: true
name: 'Glabrezu - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Fiend
cr: 10
ac: 17
hp: 157
hit_dice: '15d10 + 75'
speed: '40 ft.'
stats:
    - 20
    - 16
    - 20
    - 18
    - 18
    - 18
damage_resistances: 'cold, fire, lightning; damage from nonmagical weapons'
damage_immunities: poison
condition_immunities: poisoned
saves:
    - { strength: 9 }
    - { constitution: 9 }
    - { wisdom: 8 }
    - { charisma: 8 }
skillsaves:
    - { deception: 8 }
    - { stealth: 7 }
senses: 'truesight 120 ft., passive Perception 14'
languages: 'Abyssal, telepathy 120 ft.'
traits:
    - { name: 'Chaotic Evil', desc: 'The glabrezu radiates a Chaotic and Evil aura.' }
    - { name: 'Magic Resistance', desc: 'The glabrezu has advantage on saving throws against spells and magical effects.' }
actions:
    - { name: Multiattack, desc: 'The glabrezu makes two pincer attacks.' }
    - { name: Pincer, desc: "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 16 (2d10 + 5) bludgeoning damage. If the target is a Medium or smaller creature, it is grappled (escape DC 17). The glabrezu has two pincers, each of which can grapple one target. While grappling a target, a pincer can't attack a different target. If the same creature is grappled by both of the glabrezu's pincers, it must escape from each of them separately." }
    - { name: Wish, desc: 'Once per 30 days, the glabrezu can cast wish for a mortal, using no material components. Before doing so, it will demand that the mortal commit a terribly evil act or make a painful sacrifice.' }
'bonus actions':
    - { name: Fists, desc: 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 10 (2d4 + 5) bludgeoning damage.' }
    - { name: Rend, desc: 'If grappling the same target with both pincers, the glabrezu rips at the target, ending both grapples and dealing 27 (4d10 + 5) slashing damage. If this damage reduces a creature to 0 hit points, it dies and is torn in half.' }
    - { name: Darkness, desc: "Magical darkness spreads from a point within 30 feet, filling a 15-foot-radius sphere and spreading around corners. It remains for 1 minute, until the glabrezu dismisses it, or until the glabrezu uses this ability again. A creature with darkvision can't see through this darkness, and nonmagical light can't illuminate it." }
    - { name: 'Confusion (1/Day)', desc: 'The glabrezu targets up to three creatures within 90 feet. Each target makes a DC 16 Wisdom saving throw, becoming confused for 1 minute on a failure. A target repeats this saving throw at the end of each of its turns, ending the effect on itself on a success.' }
combat:
    - { name: 'The glabrezu opens combat with two pincer attacks on the same target', desc: 'It uses Rend whenever it can. It uses Confusion to disrupt ranged attackers. When surrounded by melee attackers, it uses Darkness, relying on its truesight to fight at an advantage. The glabrezu fights until it believes it has no chance of victory, and then offers treasure and favors in exchange for a cease fire.' }

---
```statblock
monster: Glabrezu - A5E
```
