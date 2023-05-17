---
statblock: true
name: 'Werewolf - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Humanoid
cr: 3
ac: 12
hp: 58
hit_dice: '9d8 + 18'
speed: '30 ft. (40 ft. in wolf form)'
stats:
    - 14
    - 14
    - 14
    - 10
    - 10
    - 10
damage_immunities: 'damage from nonmagical, non-silvered weapons'
skillsaves:
    - { perception: 2 }
    - { stealth: 4 }
    - { survival: 2 }
senses: 'darkvision 30 ft. (wolf or hybrid form only), passive Perception 14'
languages: Common
traits:
    - { name: 'Keen Hearing and Smell', desc: 'The werewolf has advantage on Perception checks that rely on hearing or smell.' }
    - { name: 'Pack Tactics', desc: "The werewolf has advantage on attack rolls against a creature if at least one of the werewolf's allies is within 5 feet of the creature and not incapacitated." }
actions:
    - { name: Multiattack, desc: 'The werewolf makes two melee attacks, only one of which can be with its bite.' }
    - { name: 'Greatclub (Humanoid or Hybrid Form Only)', desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) bludgeoning damage.' }
    - { name: 'Claw (Wolf or Hybrid Form Only)', desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage.' }
    - { name: 'Bite (Wolf or Hybrid Form Only)', desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage. If the target is a humanoid, it makes a DC 12 Constitution saving throw. On a failure, it is cursed with werewolf lycanthropy.' }
'bonus actions':
    - { name: Shapeshift, desc: "The werewolf changes its form to a wolf, a wolf-humanoid hybrid, or into its true form, which is a humanoid. While shapeshifted, its statistics are unchanged. It can't speak in wolf form. Its equipment is not transformed. It reverts to its true form if it dies." }
    - { name: 'Frenzied Bite (While Bloodied, Wolf or Hybrid Form Only)', desc: 'The werewolf makes a bite attack.' }
combat:
    - { name: 'Most werewolves prefer to fight in humanoid or wolf form, but some fight openly in hybrid form', desc: 'The werewolf prefers to attack with surprise or alongside allies. When bloodied, a werewolf lacking self-control instinctively switches to hybrid form and uses Frenzied Bite. A werewolf flees when reduced to 15 hit points or fewer.' }

---
```statblock
monster: Werewolf - A5E
```
