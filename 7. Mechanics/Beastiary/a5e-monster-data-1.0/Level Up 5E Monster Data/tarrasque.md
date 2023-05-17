---
statblock: true
name: 'Tarrasque - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Titanic
type: Monstrosity
cr: 30
ac: 25
hp: 1
hit_dice: '60d20 + 600'
speed: '60 ft., burrow 30 ft.'
stats:
    - 30
    - 12
    - 30
    - 4
    - 14
    - 14
damage_immunities: 'fire, poison; damage from nonmagical weapons'
condition_immunities: 'charmed, frightened, paralyzed, petrified, poisoned'
saves:
    - { strength: 19 }
    - { dexterity: 10 }
    - { constitution: 19 }
    - { intelligence: 6 }
    - { wisdom: 11 }
    - { charisma: 11 }
senses: 'blindsight 120 ft., tremorsense 60 ft., passive Perception 12'
traits:
    - { name: 'Astounding Leap', desc: "The tarrasque's high jump distance is equal to its Speed." }
    - { name: 'Bloodied Regeneration', desc: "While the tarrasque is bloodied, it regains 50 hit points at the start of each of its turns. A wish spell can suppress this trait for 24 hours. The tarrasque dies only if it starts its turn with 0 hit points and doesn't regenerate." }
    - { name: 'Immortal Nature', desc: "The tarrasque doesn't require air, sustenance, or sleep." }
    - { name: 'Legendary Resistance (3/Day)', desc: 'If the tarrasque fails a saving throw, it can choose to succeed instead.' }
    - { name: 'Magic Resistance', desc: 'The tarrasque has advantage on saving throws against spells and magical effects.' }
    - { name: 'Reflective Carapace', desc: 'When the tarrasque is targeted by a magic missile spell, a line spell, or a spell that requires a ranged attack roll, roll a d6. On a 1 to 3, the tarrasque is unaffected. On a 4 to 6, the tarrasque is unaffected, and the spell is reflected back, targeting the caster as if it originated from the tarrasque.' }
    - { name: 'Siege Monster', desc: 'The tarrasque deals double damage to objects and structures.' }
actions:
    - { name: Multiattack, desc: "The tarrasque attacks with its bite, claw, horns, and tail. It can use Swallow instead of its bite. If it's bloodied, it also recharges and then uses Radiant Breath." }
    - { name: Bite, desc: "Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 42 (5d12 + 10) piercing damage. If the target is a creature, it is grappled (escape DC 27). Until this grapple ends, the target is restrained and the tarrasque can't bite a different creature." }
    - { name: Claw, desc: 'Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 32 (5d8 + 10) slashing damage.' }
    - { name: Horns, desc: 'Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 37 (5d10 + 10) piercing damage.' }
    - { name: Tail, desc: 'Melee Weapon Attack: +19 to hit, reach 20 ft., one target. Hit: 27 (5d6 + 10) bludgeoning damage. If the target is a Huge or smaller creature, it falls prone.' }
    - { name: Swallow, desc: "The tarrasque makes a bite attack against a Large or smaller creature it is grappling. If the attack hits, the target is swallowed and the grapple ends. A swallowed creature has total cover from attacks from outside the tarrasque, it is blinded and restrained, and it takes 35 (10d6) acid damage and 35 (10d6) bludgeoning damage at the start of each of the tarrasque's turns." }
    - { name: 'If a swallowed creature deals 70 or more damage to the tarrasque in a single turn, or if the tarrasque dies, the tarrasque vomits up all swallowed creatures', desc: '' }
    - { name: 'Radiant Breath (Recharge 56)', desc: 'The tarrasque exhales radiant energy in a 90-foot cone. Each creature in that area makes a DC 27 Constitution saving throw, taking 105 (30d6) radiant damage on a failed save or half damage on a success.' }
legendary_actions:
    - { name: 'The tarrasque can take 3 legendary actions, choosing from the options below', desc: "Only one legendary action can be used at a time and only at the end of another creature's turn. It regains spent legendary actions at the start of its turn." }
    - { name: Attack, desc: 'The tarrasque attacks with its claw or tail.' }
    - { name: Move, desc: 'The tarrasque moves up to half its Speed.' }
    - { name: Roar, desc: "Each creature of the tarrasque's choice within 120 feet makes a DC 19 Charisma saving throw. On a failure, it is frightened for 1 minute. A creature repeats the saving throw at the end of its turns, with disadvantage if the tarrasque is in line of sight, ending the effect on itself on a success. If it succeeds on a saving throw or the effect ends on it, it is immune to the tarrasque's Roar for 24 hours." }
    - { name: 'Elite Recovery (While Bloodied)', desc: 'The tarrasque ends one negative effect currently affecting it. It can use this action as long as it has at least 1 hit point, even while unconscious or incapacitated.' }
    - { name: 'Chomp (Costs 2 Actions)', desc: 'The tarrasque makes a bite attack or uses Swallow.' }
    - { name: 'Inescapable Earth (Costs 3 Actions)', desc: "Each flying creature or object within 300 feet falls and its flying speed is reduced to 0 until the start of the tarrasque's next turn." }
combat:
    - { name: "The tarrasque's preferred mode of combat is to use its multiattack and then to use a legendary action to Chomp a target", desc: "It uses its Radiant Breath, when available, on three or more creatures that have seriously hurt it. It uses its Astounding Leap and Radiant Breath (sometimes together) to deal with flying enemies. If it still can't reach flying creatures, it uses Inescapable Earth." }
    - { name: 'When the tarrasque is first bloodied, it tries to retreat and find a new, faraway land to devastate', desc: 'If pursued or prevented from escaping, it fights to the death.' }

---
```statblock
monster: Tarrasque - A5E
```
