---
statblock: true
name: "Will-o'-Wisp - A5E"
source: 'Level Up: Monstrous Menagerie'
size: Small
type: Undead
cr: 2
ac: 17
hp: 28
hit_dice: 8d6
speed: '0 ft., fly 50 ft. (hover)'
stats:
    - 2
    - 24
    - 10
    - 12
    - 14
    - 12
damage_resistances: 'acid, cold, fire, necrotic, thunder; damage from nonmagical weapons'
damage_immunities: 'lightning, poison'
condition_immunities: 'fatigue, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious'
senses: 'darkvision 120 ft., passive Perception 12'
languages: 'the languages it knew in life'
traits:
    - { name: Conductive, desc: "Each time a creature touches the will-o'-wisp or hits it with a metal melee weapon for the first time on a turn, the creature takes 7 (2d6) lightning damage. This trait doesn't function while the will-o'-wisp's glow is extinguished." }
    - { name: Insubstantial, desc: "The will-o'-wisp can't pick up or move objects or creatures. It can move through creatures and objects. It takes 5 (1d10) force damage if it ends its turn inside an object." }
    - { name: 'Treasure Sense', desc: "The will-o'-wisp knows the location of coins, gems, and other nonmagical wealth within 500 feet." }
    - { name: 'Undead Nature', desc: "A will-o'-wisp doesn't require air, sustenance, or sleep." }
actions:
    - { name: Shock, desc: "Melee Spell Attack: +4 to hit, reach 5 ft., one target. Hit: 10 (3d6) lightning damage. The will-o'-wisp can't make this attack while its glow is extinguished." }
'bonus actions':
    - { name: Illumination, desc: "The will-o'-wisp alters the radius of its glow (shedding bright light in a 5- to 20-foot radius and dim light for the same number of feet beyond that radius), changes the color of its glow, or extinguishes its glow (making it invisible)." }
combat:
    - { name: "The will-o'-wisp attacks, turns invisible, and then moves to safety", desc: "On its next turn it moves to melee range, turns visible, and attacks. It repeats this pattern. The will-o'-wisp fights only to preserve its treasure. It may retreat to summon allies or otherwise cause trouble." }

---
```statblock
monster: Will-o'-Wisp - A5E
```
