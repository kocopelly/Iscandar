---
statblock: true
name: 'Pseudodragon Familiar - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Tiny
type: Dragon
cr: 1
ac: 13
hp: 7
hit_dice: '2d4 + 2'
speed: '15 ft., fly 60 ft.'
stats:
    - 6
    - 14
    - 12
    - 10
    - 12
    - 10
skillsaves:
    - { perception: 3 }
    - { stealth: 4 }
senses: 'blindsight 10 ft., darkvision 60 ft., passive Perception 16'
languages: "understands Common and Draconic but can't speak"
traits:
    - { name: 'Limited Telepathy', desc: 'The pseudodragon can magically communicate simple ideas, emotions, and images telepathically to any creature within 10 feet of it.' }
    - { name: 'Magic Resistance', desc: 'The pseudodragon has advantage on saving throws against spells and other magical effects.' }
    - { name: Familiar, desc: 'The pseudodragon can communicate telepathically with its master while they are within 1 mile of each other. When the pseudodragon is within 10 feet of its master, its master shares its Magic Resistance trait.' }
actions:
    - { name: Sting, desc: 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or become poisoned. At the end of its next turn, it repeats the saving throw. On a success, the effect ends. On a failure, it falls unconscious for 1 hour. If it takes damage, or a creature uses an action to shake it awake, it wakes up, and the effect ends.' }
    - { name: 'Telepathic Static (3/Day)', desc: "The pseudodragon targets one creature it can see within 10 feet, forcing it to make a DC 11 Charisma saving throw. On a failure, it's stunned until the end of its next turn as it suffers a barrage of telepathic imagery." }
combat:
    - { name: 'When alone, the pseudodragon uses Telepathic Static and then flees, stinging only if cornered', desc: 'When fighting alongside allies, the pseudodragon uses Telepathic Static and its sting on an enemy that is engaged in melee with an ally.' }

---
```statblock
monster: Pseudodragon Familiar - A5E
```
