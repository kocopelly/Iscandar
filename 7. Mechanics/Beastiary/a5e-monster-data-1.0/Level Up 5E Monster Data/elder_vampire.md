---
statblock: true
name: 'Elder Vampire - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Medium
type: Undead
cr: 11
ac: 16
hp: 285
hit_dice: '30d8 + 150'
speed: '40 ft., climb 30 ft.'
stats:
    - 20
    - 18
    - 20
    - 16
    - 16
    - 18
damage_resistances: 'necrotic; damage from nonmagical, non-silvered weapons'
saves:
    - { dexterity: 8 }
    - { wisdom: 7 }
    - { charisma: 8 }
skillsaves:
    - { perception: 7 }
    - { persuasion: 8 }
    - { stealth: 8 }
senses: 'darkvision 120 ft., truesight 120 ft., passive Perception 17'
languages: 'the languages it knew in life'
traits:
    - { name: 'Legendary Resistance (3/Day)', desc: 'When the vampire fails a saving throw, it can choose to succeed instead. When it does so, it visibly grows older. Its original appearance is restored when it finishes a long rest.' }
    - { name: 'Misty Recovery', desc: "When the vampire drops to 0 hit points, instead of falling unconscious, it turns into mist as if it had used the Mist Form legendary action. It can't revert to its vampire form, and it must reach its resting place within 2 hours or be destroyed. Once in its resting place, it reverts to vampire form and is paralyzed for 1 hour, at which time it regains 1 hit point. While paralyzed in this way, it can be destroyed by fire damage, radiant damage, damage from a magical weapon, or a wooden stake driven through the heart, but it is otherwise immune to damage." }
    - { name: Regeneration, desc: "The vampire regains 20 hit points at the start of its turn if it has at least 1 hit point and hasn't taken radiant damage since its last turn." }
    - { name: 'Spider Climb', desc: 'The vampire can climb even on difficult surfaces and upside down on ceilings.' }
    - { name: 'Vampire Weaknesses', desc: "Vampires' most common weaknesses are sunlight and running water. When the vampire ends its turn in contact with one of its weaknesses (such as being bathed in sunlight or running water), it takes 20 radiant damage. While in contact with its weakness, it can't use its Regeneration trait or its Mist Form or Shapechange actions." }
    - { name: 'Resting Place', desc: "Every vampire's lair contains a resting place, usually a coffin or sarcophagus, where the vampire must rest for at least an hour each day to recuperate its powers. This resting place is sprinkled with soil from its mortal homeland. If this soil is scattered or is subjected to a bless, hallow, or similar spell, the vampire is destroyed when reduced to 0 hit points." }
    - { name: 'Blood Frenzy', desc: 'While bloodied, the vampire can take 3 legendary actions instead of 1.' }
actions:
    - { name: 'Grab (Vampire Form Only)', desc: 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage plus 4 (1d8) necrotic damage. The target is grappled (escape DC 17) and restrained while grappled in this way.' }
    - { name: Charm, desc: "The vampire targets a creature within 30 feet, forcing it to make a DC 16 Wisdom saving throw. On a failure, the target is charmed by the vampire for 24 hours. While charmed it regards the vampire as a trusted friend and is a willing target for the vampire's bite. The target repeats the saving throw each time it takes damage, ending the effect on itself on a success. If the target's saving throw is successful or the effect ends for it, it is immune to this vampire's Charm for 24 hours." }
reactions:
    - { name: 'Hissing Scuttle (1/Day)', desc: 'When the vampire takes radiant damage, it moves up to its Speed without provoking opportunity attacks.' }
    - { name: 'Warding Charm (1/Day)', desc: 'When a creature the vampire can see targets it with a melee attack but before the attack is made, the vampire uses Charm on that creature.' }
'bonus actions':
    - { name: Bite, desc: "Melee Weapon Attack: +9 to hit, reach 5 ft., one target that is grappled, incapacitated, restrained, willing, or unaware of the vampire's presence. Hit: 10 (1d10 + 5) piercing damage plus 21 (6d6) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage dealt, and the vampire regains this number of hit points. The reduction lasts until the target finishes a long rest. If the target is reduced to 0 hit points by this attack, it dies and rises the following night as a vampire spawn in the vampire's thrall. Before the target first rises as a vampire spawn, a bless, gentle repose, or similar spell cast on the body prevents this transformation." }
legendary_actions:
    0: { name: 'The vampire can take 1 legendary action, choosing from the options below', desc: "Only one legendary action can be used at a time and only at the end of another creature's turn. It regains spent legendary actions at the start of its turn." }
    1: { name: 'Blood Charm', desc: 'The vampire uses Charm. A creature makes its initial saving throw with disadvantage if the vampire has hit it with a bite attack within the last 24 hours.' }
    2: { name: Grab, desc: 'The vampire makes a grab attack.' }
    3: { name: 'Mist Form', desc: "The vampire transforms into a mist or back into its true form. As mist, the vampire has a flying speed of 30, can't speak, can't take actions or manipulate objects, is immune to nonmagical damage from weapons, and has advantage on saving throws and Stealth checks. It can pass through a space as narrow as 1 inch without squeezing but can't pass through water. Anything it's carrying transforms with it." }
    4: { name: Shapechange, desc: "The vampire transforms into the shape of a Medium or smaller beast or back into its true form. While transformed, it has the beast's size and movement modes. It can't use reactions or legendary actions, and can't speak. Otherwise, it uses the vampire's statistics. Anything it's carrying transforms with it." }
    legendary_actions: ['The elder vampire has the following additional legendary actions, which it can use only while bloodied:']
    5: { name: 'Elite Recovery', desc: 'The vampire ends one negative effect currently affecting it. It can use this action as long as it has at least 1 hit point, even while unconscious or incapacitated.' }
    6: { name: 'Momentary Transformation (Vampire Form Only)', desc: 'The vampire uses Shapechange or Mist Form, moves up to its Speed without provoking opportunity attacks, and then returns to its true form.' }
    7: { name: 'Create Spawn (1/Day)', desc: "The vampire magically raises a dead humanoid as a vampire spawn under the vampire's control." }
    8: { name: 'Bite (Costs 2 Actions)', desc: 'The vampire makes a bite attack. On a hit, the target makes a DC 17 Constitution saving throw, falling asleep for 1 minute on a failure. The target wakes up if it takes damage or a creature uses an action to shake it awake.' }
    9: { name: 'Burning Blood (Costs 2 Actions)', desc: 'The vampire targets a creature within 60 feet, magically causing its blood to boil in its veins. The target makes a DC 16 Constitution saving throw, taking 31 (9d6) fire damage on a failed save or half damage on a success.' }
combat:
    - { name: 'The vampire grabs and bites its most vulnerable opponent', desc: 'Once it has weakened a foe with a bite attack, the vampire uses its Blood Charm on that target. When reduced to 30 hit points or fewer, the vampire retreats in animal or mist form through well-prepared escape routes, returning to take its revenge another day.' }

---
```statblock
monster: Elder Vampire - A5E
```
