---
statblock: true
name: 'Ogre Mage - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Giant
cr: 7
ac: 16
hp: 102
hit_dice: '12d10 + 36'
speed: '30 ft., fly 30 ft.'
stats:
    - 18
    - 10
    - 16
    - 14
    - 12
    - 16
skillsaves:
    - { arcana: 5 }
    - { deception: 6 }
    - { perception: 4 }
    - { stealth: 3 }
senses: 'darkvision 60 ft., passive Perception 14'
languages: 'Common, Giant'
traits:
    0: { name: 'Innate Spellcasting', desc: "The ogre's innate spellcasting ability is Charisma (spell save DC 14). It can innately cast the following spells, requiring no material components:" }
    traits: ['At will: darkness, invisibility', '1/day: charm person, cone of cold, gaseous form, hold person']
    1: { name: 'Iron Magic Resistance', desc: 'While wielding its iron club, the ogre mage has advantage on saving throws against spells and magical effects. Whenever the ogre mage rolls a saving throw against a spell or magical effect, the iron club emits visible sparks even if the ogre mage is invisible.' }
    2: { name: Regeneration, desc: 'The ogre mage regains 10 hit points at the beginning of its turn as long as it has at least 1 hit point.' }
actions:
    - { name: Multiattack, desc: 'The ogre makes two melee attacks.' }
    - { name: 'Claw (Ogre Mage Form Only)', desc: 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.' }
    - { name: 'Iron Club', desc: 'Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 17 (2d12 + 4) bludgeoning damage, or 10 (1d12 + 4) bludgeoning damage in Small or Medium form. When the ogre hits or touches a target with its club, it can end any spell on the target that was cast with a 3rd-level or lower spell slot.' }
    - { name: 'Read Scroll (1/Day)', desc: "The ogre casts a spell from a magical scroll without expending the scroll's magic." }
    - { name: 'Darkness (2nd-Level; V, S, Concentration)', desc: "Magical darkness spreads from a point within 30 feet of the ogre, filling a 15-foot-radius sphere and spreading around corners. It remains for 1 minute. A creature with darkvision can't see through this darkness, and nonmagical light can't illuminate it." }
    - { name: 'Hold Person (2nd-Level; V, S, Concentration)', desc: 'One humanoid the ogre can see within 60 feet makes a DC 14 Wisdom saving throw. On a failure, the target is paralyzed for 1 minute, repeating the saving throw at the end of each of its turns, ending the effect on a success.' }
    - { name: 'Invisibility (2nd-Level; V, S, Concentration)', desc: 'The ogre is invisible for 1 hour. The spell ends if the ogre attacks or casts a spell.' }
    - { name: 'Gaseous Form (3rd-Level; V, S, Concentration)', desc: "The ogre and its gear becomes a hovering cloud of gas for 1 hour. Its Speed is 0, and its fly speed is 30. It can't attack, use or drop objects, talk, or cast spells. It can enter another creature's space and pass through small holes and cracks but can't pass through liquid. It is resistant to nonmagical damage, has advantage on Strength, Dexterity and Constitution saving throws, and can't fall." }
    - { name: 'Cone of Cold (5th-Level; V, S)', desc: 'Frost blasts from the ogre in a 60-foot cone. Each creature in the area makes a DC 14 Constitution saving throw, taking 36 (8d8) cold damage on a failure or half damage on a success.' }
'bonus actions':
    - { name: Shapeshift, desc: 'The ogre changes its form into a Small or Medium humanoid, or back into its true form, which is a Large giant. Other than its size, its statistics are the same in each form. Its iron club, armor, and clothing change size with it. It reverts to its true form when it dies.' }

---
```statblock
monster: Ogre Mage - A5E
```
