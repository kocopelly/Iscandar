---
statblock: true
name: 'Horned Devil - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Fiend
cr: 11
ac: 18
hp: 168
hit_dice: '16d10 + 80'
speed: '30 ft., fly 60 ft.'
stats:
    - 20
    - 16
    - 20
    - 12
    - 16
    - 16
damage_resistances: 'cold; damage from nonmagical, non-silvered weapons'
damage_immunities: 'fire, poison'
condition_immunities: poisoned
saves:
    - { strength: 9 }
    - { dexterity: 7 }
    - { wisdom: 7 }
    - { charisma: 7 }
skillsaves:
    - { athletics: 9 }
    - { intimidation: 7 }
senses: 'darkvision 120 ft., passive Perception 13'
languages: 'Infernal, telepathy 120 ft.'
traits:
    - { name: "Devil's Sight", desc: "The devil's darkvision penetrates magical darkness." }
    - { name: 'Lawful Evil', desc: 'The devil radiates a Lawful and Evil aura.' }
    - { name: 'Magic Resistance', desc: 'The devil has advantage on saving throws against spells and magical effects.' }
actions:
    - { name: Multiattack, desc: 'The devil makes two attacks with its fork and one with its tail. It can replace any melee attack with Hurl Flame.' }
    - { name: Fork, desc: 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 12 (2d6 + 5) piercing damage plus 3 (1d6) fire damage.' }
    - { name: Tail, desc: 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) piercing damage. If the target is a creature other than an undead or construct, it makes a DC 17 Constitution saving throw. On a failure, it receives an infernal wound and takes 11 (2d10) ongoing piercing damage. Each time the devil hits the wounded target with this attack, the ongoing damage increases by 11 (2d10). A creature can spend an action to make a DC 12 Medicine check, ending the ongoing damage on a success. At least 1 hit point of magical healing also ends the ongoing damage.' }
    - { name: 'Hurl Flame', desc: 'Ranged Spell Attack: +7 to hit, range 150 ft., one target. Hit: 10 (3d6) fire damage. If the target is an unattended flammable object or a creature, it catches fire, taking 5 (1d10) ongoing fire damage. A creature can use an action to extinguish this fire.' }
    - { name: 'Inferno (1/Day, While Bloodied)', desc: 'The devil waves its fork, igniting a trail of roaring flame. Any creature within 10 feet of the devil makes a DC 15 Dexterity saving throw, taking 49 (14d6) fire damage on a failure or half damage on a success.' }
reactions:
    - { name: 'Pin (1/Day)', desc: "When a creature misses the devil with a melee attack, the devil makes a fork attack against that creature. On a hit, the target is impaled by the fork and grappled (escape DC 17). Until this grapple ends, the devil can't make fork attacks or use Inferno, but the target takes 7 (2d6) piercing damage plus 3 (1d6) fire damage at the beginning of each of its turns." }
combat:
    - { name: 'The horned devil prefers to fight in melee, especially against weak enemies', desc: "It goads a ranged creature into making a melee attack, pins it, and keeps it pinned while hurling flame at other opponents. If fighting a melee combatant, the devil tries to pin the creature while 10 feet away from it, so that the creature can't counterattack. When bloodied, it releases a pinned opponent in order to use Inferno. The horned devil follows orders to the letter and rarely retreats, but it might agree to a ceasefire if its orders aren't specific." }

---
```statblock
monster: Horned Devil - A5E
```
