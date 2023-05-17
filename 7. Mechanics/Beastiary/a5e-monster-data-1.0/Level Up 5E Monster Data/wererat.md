---
statblock: true
name: 'Wererat - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Humanoid
cr: 2
ac: 12
hp: 33
hit_dice: '6d8 + 6'
speed: '30 ft.'
stats:
    - 10
    - 14
    - 12
    - 10
    - 10
    - 10
damage_resistances: 'damage from nonmagical, non-silvered weapons'
skillsaves:
    - { perception: 2 }
    - { stealth: 4 }
senses: 'darkvision 60 ft. (rat or hybrid form only), passive Perception 12'
languages: Common
traits:
    - { name: 'Keen Smell', desc: 'The wererat has advantage on Perception checks that rely on smell.' }
    - { name: 'Pack Tactics', desc: "The wererat has advantage on attack rolls against a creature if at least one of the wererat's allies is within 5 feet of the creature and not incapacitated." }
    - { name: Wolfsbane, desc: 'Lycanthropes are repelled by the wolfsbane flower. A lycanthrope in hybrid or beast form is poisoned while within 10 feet of a living or dried wolfsbane flower that it can smell. If wolfsbane is applied to a weapon or ammunition, lycanthropes are damaged by the weapon as if it were silver. An application of wolfsbane lasts for 1 hour.' }
actions:
    - { name: 'Shortsword (Humanoid or Hybrid Form Only)', desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 12 (3d6 + 2) piercing damage if the attack is made with advantage.' }
    - { name: 'Hand Crossbow (Humanoid or Hybrid Form Only)', desc: 'Melee or Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 12 (3d6 + 2) piercing damage if the attack is made with advantage.' }
    - { name: 'Bite (Rat or Hybrid Form Only)', desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage. If the target is a humanoid, it makes a DC 11 Constitution saving throw. On a failure, it is cursed with wererat lycanthropy.' }
'bonus actions':
    - { name: Shapeshift, desc: "The wererat changes its form to a giant rat, a rat-humanoid hybrid, or into its true form, which is a humanoid. While shapeshifted, its statistics are unchanged. It can't speak in rat form. Its equipment is not transformed. It reverts to its true form if it dies." }
    - { name: 'Frenzied Bite (While Bloodied, Rat or Hybrid Form Only)', desc: 'The wererat makes a bite attack.' }
combat:
    - { name: 'The wererat prefers to fight in hybrid form, in darkness if possible', desc: 'If its enemy has no obvious silver weapon or magical attack, it strikes with its shortsword, preferably using Pack Tactics; otherwise it attacks with its crossbow from hiding. It flees if bloodied and only uses Frenzied Bite if cornered.' }

---
```statblock
monster: Wererat - A5E
```
