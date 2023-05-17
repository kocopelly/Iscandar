---
statblock: true
name: 'Swarm of Khalkos Spawn - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Aberration
cr: 2
ac: 16
hp: 71
hit_dice: '11d8 + 22'
speed: '30 ft., fly 30 ft.'
stats:
    - 6
    - 16
    - 14
    - 18
    - 14
    - 12
damage_resistances: 'fire, psychic, radiant; bludgeoning, piercing, slashing'
condition_immunities: 'charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned'
saves:
    - { intelligence: 5 }
    - { wisdom: 4 }
    - { charisma: 3 }
senses: 'darkvision 60 ft., passive Perception 12'
languages: 'telepathy 120 ft.'
traits:
    traits: ['Challenge 6 (2,300 XP)']
    0: { name: 'Detect Alignment', desc: 'The swarm knows the alignment of creatures within 30 feet.' }
    1: { name: Swarm, desc: "The swarm can occupy another creature's space and move through any opening large enough for a Tiny creature. It can't gain hit points or temporary hit points." }
actions:
    - { name: Sting, desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 13 (4d4+3) piercing damage plus 14 (4d6) poison damage, or 8 (2d4+3) piercing damage plus 7 (2d6) poison damage if the swarm is bloodied.' }
    - { name: 'Chaos Pheromones', desc: 'The swarm emits a cloud of pheromones in the air in a 10-foot-radius. The cloud spreads around corners. Each non-khalkos creature in the area makes a DC 12 Intelligence saving throw. On a failure, the creature is confused for 1 minute. It repeats the saving throw at the end of each of its turns, ending the effect on itself on a success. If the creature makes its saving throw or the condition ends for it, it is immune to the chaos pheromones of khalkos spawn for the next 24 hours.' }
combat:
    - { name: 'The khalkos spawn starts combat by using Chaos Pheromones on clusters of enemies and then stings a creature, preferably one affected by its pheromones', desc: '' }

---
```statblock
monster: Swarm of Khalkos Spawn - A5E
```
