---
statblock: true
name: 'Fey Knight - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Fey
cr: 4
ac: 16
hp: 58
hit_dice: '9d8 + 18'
speed: '35 ft., fly 60 ft. (maximum elevation 10 feet)'
stats:
    - 14
    - 18
    - 14
    - 12
    - 16
    - 16
condition_immunities: 'charmed, unconscious'
saves:
    - { dexterity: 6 }
    - { wisdom: 5 }
    - { charisma: 5 }
skillsaves:
    - { deception: 5 }
    - { nature: 3 }
    - { perception: 5 }
    - { stealth: 6 }
    - { survival: 5 }
senses: 'passive Perception 15'
languages: 'Common, Elvish, Sylvan'
traits:
    - { name: 'Faerie Form', desc: "The knight can magically change its size between Medium and Tiny as an action. While tiny, the bludgeoning, piercing, and slashing damage dealt by the knight's attacks is halved. Additionally, it has disadvantage on Strength checks and advantage on Dexterity checks. Its statistics are otherwise unchanged." }
    - { name: 'Faerie Light', desc: 'As a bonus action, the knight can cast dim light for 30 feet, or extinguish its glow.' }
actions:
    - { name: Multiattack, desc: 'The knight makes two melee attacks.' }
    - { name: 'Glittering Scimitar', desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage plus 7 (2d6) cold, fire, or lightning damage (its choice).' }
    - { name: Longbow, desc: 'Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit: 8 (1d8 + 4) piercing damage plus 14 (4d6) poison damage. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even if it regains hit points, and it is asleep while poisoned in this way.' }
    - { name: 'Fey Glamour', desc: "The knight targets one humanoid within 30 feet. The target makes a DC 13 Wisdom saving throw. On a failure, it is magically charmed by the knight for 1 day. If the knight or one of the knight's allies harms the target, the target repeats the saving throw, ending the effect on itself on a success. If a target's saving throw is successful, or if the effect ends for it, the creature is immune to this knight's Fey Charm for a year and a day." }
reactions:
    - { name: "Nature's Shield", desc: "When the knight would be hit by an attack while the knight is within 5 feet of a tree or other large plant, the knight's AC magically increases by 3 against that attack as the plant interposes branches or vines between the knight and the attacker." }
combat:
    - { name: 'If possible, the knight fights within the shielding reach of trees, and it ambushes opponents when it can', desc: "If its opponents can't fly, it flies at its maximum elevation of 10 feet, just out of reach of Medium creatures without ranged or reach weapons. It prefers ranged combat but does not retreat if engaged in melee." }

---
```statblock
monster: Fey Knight - A5E
```
