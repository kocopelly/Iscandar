---
statblock: true
name: 'Ankylo'
image: ![[Ankylo.jpg]]
size: Large
type: Humanoid
alignment: Lawful Neutral
cr: 4
ac: 18
hp: 80
hit_dice: '10d10 + 30'
speed: '40 ft.'
stats:
    - 20
    - 12
    - 18
    - 10
    - 14
    - 12
senses: 'darkvision 60 ft., passive Perception 11'
languages: 'Common, Saurian'
saves:
    - { strength: 7 }
    - { constitution: 6 }
skillsaves:
    - { athletics: 7 }
    - { perception: 4 }
actions:
    - { name: Slam, desc: 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 16 (2d8 + 7) bludgeoning damage.' }
    - { name: Tail Swipe, desc: 'Melee Weapon Attack: +8 to hit, reach 10 ft., all creatures in a 10-foot radius around the Ankylo. Hit: 14 (2d6 + 7) bludgeoning damage. Each creature must succeed on a DC 15 Dexterity saving throw or be knocked prone.' }
straits:
    - { name: 'Armored Defense', desc: 'The Ankylos thick, resilient scales provide it with a +2 bonus to AC.' }
    - { name: 'Tenacious Endurance', desc: 'When reduced to 0 hit points but not killed outright, the Ankylo can make a Constitution saving throw with a DC of 5 + the damage taken. On a success, the Ankylo drops to 1 hit point instead.' }
---
```statblock 
	monster: Ankylo
```