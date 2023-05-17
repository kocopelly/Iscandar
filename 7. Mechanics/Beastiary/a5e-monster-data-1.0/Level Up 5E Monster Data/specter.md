---
statblock: true
name: 'Specter - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Undead
cr: 1
ac: 12
hp: 22
hit_dice: 5d8
speed: '0 ft., fly 50 ft. (hover)'
stats:
    - 2
    - 14
    - 10
    - 10
    - 10
    - 14
damage_resistances: 'acid, cold, fire, lighting, thunder; damage from nonmagical weapons'
damage_immunities: 'necrotic, poison'
condition_immunities: 'charmed, fatigue, frightened, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious'
senses: 'darkvision 60 ft., passive Perception 10'
languages: "understands the languages it knew in life but can't speak"
traits:
    - { name: Incorporeal, desc: 'The specter can move through creatures and objects. It takes 5 (1d10) force damage if it ends its turn inside an object. If it takes radiant damage, it loses this trait until the end of its next turn.' }
    - { name: 'Sunlight Sensitivity', desc: 'While in sunlight, the specter has disadvantage on attack rolls, as well as on Perception checks that rely on sight.' }
    - { name: 'Undead Nature', desc: "A specter doesn't require air, sustenance, or sleep." }
actions:
    - { name: 'Life Drain', desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 10 (3d6) necrotic damage, and the target must succeed on a DC 10 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the creature finishes a long rest. The target dies if its hit point maximum is reduced to 0.' }
    - { name: Hurl, desc: 'The specter targets a Medium or smaller creature, or an object weighing no more than 150 pounds, within 30 feet of it. A creature makes a DC 12 Strength saving throw. On a failure, it is hurled up to 30 feet in any direction (including upwards), taking 3 (1d6) damage for every 10 feet it is hurled. An object is launched up to 30 feet in a straight line, and a creature in its path makes a DC 12 Dexterity saving throw, taking 7 (2d6) bludgeoning damage on a failure. On a success, the creature takes no damage, and the object keeps flying past it.' }
    - { name: Fade, desc: "While not in sunlight, the specter turns invisible and takes the Hide action. It remains invisible for 1 minute or until it uses Life Drain or takes damage. If the specter takes radiant damage, it can't use this action until the end of its next turn." }
combat:
    - { name: 'The specter attacks invisibly, using Hurl on its first turn and then becoming visible as it uses Life Drain', desc: 'It retreats if it takes radiant damage while bloodied.' }

---
```statblock
monster: Specter - A5E
```
