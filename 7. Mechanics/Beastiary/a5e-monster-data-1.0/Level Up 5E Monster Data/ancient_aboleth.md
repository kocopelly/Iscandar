---
statblock: true
name: 'Ancient Aboleth - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Huge
type: Aberration
cr: 11
ac: 17
hp: 342
hit_dice: '36d10 + 144'
speed: '10 ft., swim 40 ft.'
stats:
    - 20
    - 12
    - 18
    - 20
    - 20
    - 18
saves:
    - { dexterity: 5 }
    - { constitution: 8 }
    - { intelligence: 9 }
    - { wisdom: 9 }
skillsaves:
    - { deception: 8 }
    - { history: 9 }
    - { stealth: 5 }
senses: 'blindsight 30 ft., darkvision 120 ft., passive Perception 15'
languages: 'Deep Speech, telepathy 120 ft.'
traits:
    - { name: Amphibious, desc: 'The aboleth can breathe air and water.' }
    - { name: 'Innate Spellcasting', desc: "The aboleth's spellcasting ability is Charisma (spell save DC 16). It can innately cast the following spells, requiring no components:" }
    - { name: '3/day each: detect thoughts (range 120 ft', desc: '), project image (range 1 mile), phantasmal force' }
    - { name: 'Legendary Resistance (3/Day)', desc: 'When the aboleth fails a saving throw, it can choose to succeed instead. When it does so, one of its eyes flashes with green light and then turns dull black. Once all 3 of its eyes are black, it is blind beyond the range of its blindsight until it finishes a long rest.' }
actions:
    - { name: Multiattack, desc: 'The aboleth attacks three times with its tentacle.' }
    - { name: Tentacle, desc: 'Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 19 (4d6 + 5) bludgeoning damage. The aboleth can choose instead to deal 0 damage. If the target is a creature, it makes a DC 16 Constitution saving throw. On a failure, it contracts a disease called the Sea Change. On a success, it is immune to this disease for 24 hours. While affected by this disease, the target has disadvantage on Wisdom saving throws. After 1 hour, the target grows gills, it can breathe water, its skin becomes slimy, and it begins to suffocate if it goes 12 hours without being immersed in water for at least 1 hour. This disease can be removed with a disease-removing spell cast with at least a 4th-level spell slot, and it ends 24 hours after the aboleth dies.' }
    - { name: 'Slimy Cloud (1/Day, While Bloodied)', desc: 'While underwater, the aboleth exudes a cloud of inky slime in a 30-foot-radius sphere. Each non-aboleth creature in the area when the cloud appears makes a DC 16 Constitution saving throw. On a failure, it takes 44 (8d10) poison damage and is poisoned for 1 minute. The slime extends around corners, and the area is heavily obscured for 1 minute or until a strong current dissipates the cloud.' }
legendary_actions:
    - { name: 'The aboleth can take 2 legendary actions, choosing from the options below', desc: "Only one legendary action can be used at a time and only at the end of another creature's turn. It regains spent legendary actions at the start of its turn." }
    - { name: Move, desc: 'The aboleth moves up to its swim speed without provoking opportunity attacks.' }
    - { name: 'Telepathic Summon', desc: 'One creature within 90 feet makes a DC 16 Wisdom saving throw. On a failure, it must use its reaction, if available, to move up to its speed toward the aboleth by the most direct route that avoids hazards, not avoiding opportunity attacks. This is a magical charm effect.' }
    - { name: 'Baleful Charm (Costs 2 Actions)', desc: "The aboleth targets one creature within 60 feet that has contracted Sea Change. The target makes a DC 16 Wisdom saving throw. On a failure, it is magically charmed by the aboleth until the aboleth dies. The target can repeat this saving throw every 24 hours and when it takes damage from the aboleth or the aboleth's allies. While charmed in this way, the target can communicate telepathically with the aboleth over any distance and it follows the aboleth's orders." }
    - { name: 'Soul Drain (Costs 2 Actions)', desc: 'One creature charmed by the aboleth takes 22 (4d10) psychic damage, and the aboleth regains hit points equal to the damage dealt.' }
    - { name: 'Elite Recovery', desc: 'The aboleth ends one negative effect currently affecting it. It can use this action as long as it has at least 1 hit point, even while unconscious or incapacitated.' }
    - { name: 'Look Upon My Works (1/Day)', desc: "Each creature within 90 feet makes a DC 16 Wisdom saving throw. On a failure, the creature sees a fragmentary vision of the aboleth's memories, taking 33 (6d10) psychic damage. After taking the damage, the creature forgets the vision, but it may learn one piece of lore." }
    - { name: 'Lunging Attack', desc: 'The aboleth moves up to its swim speed without provoking opportunity attacks and makes a tentacle attack.' }
combat:
    - { name: 'The aboleth strikes as many enemies as possible with its tentacles in order to infect them with the Sea Change, and then uses Baleful Charm on the biggest threats', desc: 'When hurt, it uses Slimy Cloud and escapes through a hidden exit. Its thralls sacrifice themselves to cover its retreat.' }

---
```statblock
monster: Ancient Aboleth - A5E
```
