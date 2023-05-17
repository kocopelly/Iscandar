---
statblock: true
name: 'Wereboar - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Humanoid
cr: 4
ac: 12
hp: 78
hit_dice: '12d8 + 24'
speed: '30 ft. (40 ft. in boar form)'
stats:
    - 16
    - 10
    - 14
    - 10
    - 10
    - 10
damage_immunities: 'damage from nonmagical, non-silvered weapons'
skillsaves:
    - { perception: 2 }
senses: 'passive Perception 12'
languages: Common
traits:
    - { name: 'Relentless (1/Day)', desc: 'If the wereboar takes 14 or less damage that would reduce it to 0 hit points, it is instead reduced to 1 hit point.' }
    - { name: Wolfsbane, desc: 'Lycanthropes are repelled by the wolfsbane flower. A lycanthrope in hybrid or beast form is poisoned while within 10 feet of a living or dried wolfsbane flower that it can smell. If wolfsbane is applied to a weapon or ammunition, lycanthropes are damaged by the weapon as if it were silver. An application of wolfsbane lasts for 1 hour.' }
actions:
    - { name: 'Multiattack (Humanoid or Hybrid Form Only)', desc: 'The wereboar makes two attacks, only one of which can be with its tusks.' }
    - { name: 'Maul (Humanoid or Hybrid Form Only)', desc: 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage.' }
    - { name: 'Tusks (Boar or Hybrid Form Only)', desc: 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage. If the boar moves at least 20 feet straight towards the target before the attack, the attack deals an extra 7 (2d6) slashing damage. If the target is a creature, it makes a DC 13 Strength saving throw, falling prone on a failure. If the target is a humanoid, it makes a DC 12 Constitution saving throw. On a failure, it is cursed with wereboar lycanthropy.' }
'bonus actions':
    - { name: Shapeshift, desc: "The wereboar changes its form to a boar, a boar-humanoid hybrid, or into its true form, which is a humanoid. While shapeshifted, its statistics are unchanged. It can't speak in boar form. Its equipment is not transformed. It reverts to its true form if it dies." }
    - { name: 'Frenzied Tusks (While Bloodied, Boar or Hybrid Form Only)', desc: 'The wereboar attacks with its tusks.' }
combat:
    - { name: 'The boar nearly always fights in hybrid form', desc: "Even if it's trying to hide its identity, it's likely to shift to hybrid form and use Frenzied Tusks when bloodied. It fights in a rage; unless given breathing room to calm down, it fights to the death." }

---
```statblock
monster: Wereboar - A5E
```
