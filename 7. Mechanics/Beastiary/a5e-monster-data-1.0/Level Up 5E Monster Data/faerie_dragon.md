---
statblock: true
name: 'Faerie Dragon - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Tiny
type: Dragon
cr: 1
ac: 15
hp: 14
hit_dice: '4d4 + 4'
speed: '10 ft., fly 60 ft.'
stats:
    - 3
    - 20
    - 12
    - 14
    - 12
    - 16
skillsaves:
    - { arcana: 4 }
    - { perception: 3 }
    - { stealth: 7 }
senses: 'darkvision 60 ft., passive Perception 13'
languages: 'Draconic, Sylvan, telepathy 60 ft. (with other dragons only)'
traits:
    0: { name: 'Innate Spellcasting', desc: "The dragon's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast spells, requiring no material components. The dragon gains additional spells as it ages." }
    traits: ['5 years old, at will: dancing lights, mage hand, minor illusion', '10 years old, 1/day: suggestion', '30 years old, 1/day: major image', '50 years old, 1/day: hallucinatory terrain']
    1: { name: 'Magic Resistance', desc: 'The dragon has advantage on saving throws against spells and magical effects.' }
actions:
    - { name: Bite, desc: 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 1 piercing damage.' }
    - { name: 'Euphoria Breath (Recharge 56)', desc: 'The dragon breathes an intoxicating gas at a creature within 5 feet. The target makes a DC 11 Wisdom saving throw. On a failure, the target is confused for 1 minute. The target repeats the saving throw at the end of each of its turns, ending the effect on a success.' }
    - { name: 'Prismatic Light (3/Day)', desc: "The dragon's scales pulse with light. Each creature within 15 feet that can see the dragon makes a DC 13 Wisdom saving throw. On a failure, the creature is magically blinded until the end of its next turn." }
    - { name: 'Beast Form (1/Day, 50+ Years Old Only)', desc: "The dragon targets one creature within 15 feet. The target makes a DC 13 Wisdom saving throw. On a failure, it is magically transformed into a harmless Tiny beast, such as a mouse or a songbird, for 1 minute. While in this form, its statistics are unchanged, except it can't speak or take actions, reactions, or bonus actions. It gains movement modes appropriate to its form, such as a climb or fly speed, of up to 30 feet. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. The effect also ends if the target takes damage." }
'bonus actions':
    - { name: Invisibility, desc: 'The dragon and any equipment it wears or carries magically turns invisible. This invisibility ends if the dragon falls unconscious, dismisses the effect, or uses Bite, Euphoria Breath, Prismatic Light, or Beast Form.' }
combat:
    - { name: "Faerie dragons don't like to fight alone", desc: 'When forced to do so, they use hit and run tactics, turning visible only to use an ability such as Euphoria Breath or Prismatic Light. When fighting alongside allies, they team up against a foe, turning invisible after each attack. A faerie dragon usually retreats as soon as it is wounded.' }

---
```statblock
monster: Faerie Dragon - A5E
```
