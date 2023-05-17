---
statblock: true
name: 'Assassin - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Humanoid
cr: 7
ac: 16
hp: 97
hit_dice: '15d8 + 30'
speed: '35 ft.'
stats:
    - 10
    - 16
    - 14
    - 12
    - 12
    - 12
saves:
    - { dexterity: 6 }
    - { intelligence: 4 }
    - { wisdom: 4 }
skillsaves:
    - { acrobatics: 6 }
    - { deception: 4 }
    - { perception: 4 }
    - { stealth: 6 }
senses: 'blindsight 10 ft., darkvision 30 ft., passive Perception 14'
languages: 'any two'
traits:
    - { name: Assassinate, desc: "During the first turn of combat, the assassin has advantage on attack rolls against any creature that hasn't acted. On a successful hit, each creature of the assassin's choice that can see the assassin's attack is rattled until the end of the assassin's next turn." }
    - { name: 'Dangerous Poison', desc: 'As part of making an attack, the assassin can apply a dangerous poison to their weapon (included below). The assassin carries 3 doses of this poison. A single dose can coat one melee weapon or up to 5 pieces of ammunition.' }
    - { name: Evasion, desc: 'When the assassin makes a Dexterity saving throw against an effect that deals half damage on a success, they take no damage on a success and half damage on a failure.' }
    - { name: 'Sneak Attack (1/Turn)', desc: "The assassin deals an extra 21 (6d6) damage when they hit with a weapon attack while they have advantage on the attack, or when the assassin's target is within 5 feet of an ally of the assassin while the assassin doesn't have disadvantage on the attack." }
actions:
    - { name: Shortsword, desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage plus 10 (3d6) poison damage.' }
    - { name: 'Hand Crossbow', desc: 'Ranged Weapon Attack: +6 to hit, range 30/120 ft., one target. Hit: 6 (1d6 + 3) piercing damage plus 10 (3d6) poison damage.' }
'bonus actions':
    - { name: 'Cunning Action', desc: 'The assassin takes the Dash, Disengage, Hide, or Use an Object action.' }
    - { name: 'Rapid Attack', desc: 'The assassin attacks with their shortsword.' }
    - { name: 'Assassins specialize in dealing quiet, sudden death', desc: 'While some kill for pay, others do so for ideological or political reasons.' }

---
```statblock
monster: Assassin - A5E
```
