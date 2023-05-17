---
statblock: true
name: 'Mimic - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Monstrosity
cr: 2
ac: 12
hp: 52
hit_dice: '8d8 + 16'
speed: '30 ft. (15 ft. in object form)'
stats:
    - 18
    - 14
    - 14
    - 6
    - 14
    - 8
condition_immunities: 'grappled, prone'
skillsaves:
    - { stealth: 4 }
senses: 'darkvision 60 ft., passive Perception 12'
traits:
    - { name: 'False Appearance', desc: 'While the mimic is motionless, it is indistinguishable from an inanimate object.' }
    - { name: Sticky, desc: 'A creature, object, or weapon that touches the mimic is stuck to the mimic. A creature can use an action to make a DC 14 Strength check, freeing itself or an object or creature within reach on a success. The effect also ends when the mimic chooses to end it or when the mimic dies.' }
    - { name: 'Telepathic Sense', desc: 'A mimic telepathically senses the presence of humanoids within 120 feet and gains a mental image of any inanimate object desired by any of the creatures it senses. This ability is blocked by 3 feet of wood or dirt, 1 foot of stone, 1 inch of common metal, or a thin sheet of lead.' }
    - { name: 'Water Soluble', desc: 'If the mimic is splashed with at least 1 gallon of water, it assumes its true form and the DC to escape its Sticky trait is reduced to 10 until the end of its next turn.' }
actions:
    - { name: Multiattack, desc: 'The mimic makes a bite attack and a pseudopod attack.' }
    - { name: Pseudopod, desc: "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d4 + 4) bludgeoning damage, and the target is subjected to the mimic's Sticky trait." }
    - { name: Bite, desc: "Melee Weapon Attack: +6 to hit, reach 5 ft., one creature stuck to the mimic. Hit: 9 (2d4 + 4) piercing damage, and the target is restrained until it is no longer stuck to the mimic. While a creature is restrained by the mimic, the mimic can't bite a different creature." }
    - { name: Swallow, desc: "The mimic makes a bite attack against a Medium or smaller creature restrained by it. If the attack hits and the mimic has not swallowed another creature, the target is swallowed and no longer stuck to the mimic. A swallowed creature has total cover from attacks from outside the mimic, is blinded and restrained, and takes 5 (2d4) acid damage at the start of each of the mimic's turns." }
    - { name: 'If a swallowed creature deals 10 or more damage to the mimic in a single turn, or if the mimic dies, the target falls prone in an unoccupied space of its choice within 5 feet of the mimic and is no longer swallowed', desc: '' }
'bonus actions':
    - { name: Shapeshift, desc: 'The mimic changes its form to resemble an inanimate object of its approximate size or changes into its true form, which is an amorphous blob. Objects it is carrying or stuck to are not transformed. While shapeshifted, its statistics are unchanged. It reverts to its true form if it dies.' }
combat:
    - { name: 'The mimic waits in object form for a creature to touch it and then uses its bite', desc: 'If a creature within 5 feet of it shows no inclination to touch it, it attacks with its pseudopod and then bites the stuck target. The mimic tries to swallow creatures it has restrained, using its pseudopod to defend itself against other assailants. If the mimic swallows a creature, it shifts to its true form and tries to escape.' }

---
```statblock
monster: Mimic - A5E
```
