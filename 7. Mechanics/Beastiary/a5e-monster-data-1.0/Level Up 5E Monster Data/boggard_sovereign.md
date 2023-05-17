---
statblock: true
name: 'Boggard Sovereign - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Humanoid
cr: 3
ac: 13
hp: 67
hit_dice: '9d10 + 18'
speed: '20 ft., swim 40 ft.'
stats:
    - 16
    - 12
    - 14
    - 12
    - 14
    - 12
skillsaves:
    - { stealth: 3 }
    - { perception: 3 }
    - { intimidation: 3 }
senses: 'passive Perception 13'
languages: 'Boggard, Common'
traits:
    - { name: Amphibious, desc: 'The boggard can breathe air and water.' }
    - { name: 'Speak with Frogs and Toads', desc: 'The boggard can communicate with frogs and toads.' }
actions:
    - { name: 'Parting Bite', desc: 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) piercing damage plus 7 (2d6) poison damage. On a hit, the boggard may jump up to its Speed horizontally and half its Speed vertically without provoking opportunity attacks.' }
    - { name: 'Incite Frenzy (1/Day)', desc: 'Each boggard and frog with a Bite attack within 60 feet may use its reaction to make a Bite attack.' }
    - { name: 'Earthshaking Croak (1/Day)', desc: 'Each non-frog and non-boggard creature within 30 feet makes a DC 12 Constitution saving throw, taking 14 (4d6) thunder damage and falling prone on a failure, or taking half damage on a success.' }
    - { name: 'Summon Frog Guardians (1/Day)', desc: "The boggard magically summons two Medium frog guardians, which wriggle from the ground in an empty space within 30 feet. They follow the boggard's orders and disappear after 1 minute. They have the statistics of boggards except they have Intelligence 2, have no spear attack, and can make a bite attack as part of their Vaulting Leap." }
combat:
    - { name: 'The boggard sovereign prefers to stay out of melee range, often leaping onto high and hard-to-reach places', desc: 'It uses Earthshaking Croak, Incite Frenzy, and Summon Frog Guardians from a distance. If forced into melee, it attacks with its parting bite. If this attack hits, it hops away.' }

---
```statblock
monster: Boggard Sovereign - A5E
```
