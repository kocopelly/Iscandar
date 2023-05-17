---
statblock: true
name: 'Wallflower - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Plant
cr: 2
ac: 14
hp: 33
hit_dice: '6d8 + 12'
speed: '20 ft., climb 20 ft.'
stats:
    - 14
    - 14
    - 14
    - 2
    - 14
    - 5
damage_resistances: 'damage from nonmagical weapons'
skillsaves:
    - { stealth: 4 }
senses: 'darkvision 60 ft., passive Perception 12'
traits:
    - { name: 'Luring Scent', desc: 'When a beast, humanoid or fey creature begins its turn within 30 feet, the creature makes a DC 12 Constitution saving throw. On a failure, it moves as close as it can to the wallflower and ends its turn. Creatures immune to being charmed are immune to this effect. A creature that succeeds on the saving throw is immune to the Luring Scent of all wallflowers for 24 hours.' }
actions:
    - { name: Tentacles, desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage, and the target is grappled (escape DC 12). Until this grapple ends, the grick can't attack a different target with its tentacles." }
'bonus actions':
    - { name: Beak, desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature grappled by the grick. Hit: 9 (2d6 + 2) piercing damage.' }
combat:
    - { name: 'The grick tries to attack with surprise, seizing its prey with its tentacles and attacking with its beak', desc: "It climbs to safety if it's bloodied and not grappling a creature." }

---
```statblock
monster: Wallflower - A5E
```
