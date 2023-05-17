---
statblock: true
name: 'Forgotten God - A5E'
source: 'Level Up: Monstrous Menagerie'
size: Large
type: Celestial
cr: 10
ac: 17
hp: 161
hit_dice: '17d8 + 85'
speed: '40 ft., fly 40 ft.'
stats:
    - 20
    - 18
    - 20
    - 10
    - 20
    - 20
damage_resistances: 'poison, radiant; damage from nonmagical weapons'
condition_immunities: 'fatigue, frightened, poisoned'
saves:
    - { constitution: 9 }
    - { wisdom: 9 }
    - { charisma: 9 }
skillsaves:
    - { arcana: 4 }
    - { history: 4 }
    - { intimidation: 9 }
    - { perception: 9 }
    - { persuasion: 9 }
    - { religion: 9 }
senses: 'truesight 120 ft., passive Perception 19'
languages: All
traits:
    - { name: Aligned, desc: 'The forgotten god radiates a weak alignment aura, most often Lawful and Good, Chaotic and Good, Lawful and Evil, or Chaotic and Evil. Its behavior may not match its alignment.' }
    - { name: 'Flawed Spellcasting', desc: "The god's innate spellcasting ability is Wisdom (save DC 17).The god can try to cast flame strike or spirit guardians at will with no material component. When the god tries to cast the spell, roll 1d6. On a 1, 2, or 3 on the die, the spell visibly fails and has no effect. The god's action for the turn is not wasted, but it can't be used to cast a spell." }
    - { name: 'Legendary Resistance (3/Day)', desc: 'When the god fails a saving throw, it can choose to succeed instead. When it does so, it seems to flicker and shrink, as if it is using up its essence.' }
    - { name: 'Divine Nature', desc: "A forgotten god doesn't require air, sustenance, or sleep." }
actions:
    - { name: 'Divine Weapon', desc: 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 9 (1d8 + 5) damage (damage type based on the form of the weapon or implement) plus 3 (1d6) radiant damage.' }
    - { name: 'Stunning Gaze (Gaze)', desc: 'The god targets a creature within 60 feet. The target makes a DC 17 Charisma saving throw. On a failure, the target takes 10 (3d6) radiant damage and is stunned until the end of its next turn. On a success, the target is immune to Stunning Gaze for 24 hours.' }
    - { name: 'Divine Wrath (1/Day, While Bloodied)', desc: "Each creature of the god's choice within 60 feet makes a DC 17 Constitution saving throw, taking 28 (8d6) radiant damage on a failure or half damage on a success." }
    - { name: 'Spirit Guardians (3rd-Level; V, S, Concentration)', desc: 'Spirits of former divine servants surround the god in a 10-foot radius for 10 minutes. The god can choose creatures they can see to be unaffected by the spell. Other creatures treat the area as difficult terrain, and when a creature enters the area for the first time on a turn or starts its turn there, it makes a DC DC 17 Wisdom saving throw, taking 10 (3d6) radiant damage on a failed save or half damage on a success.' }
    - { name: 'Flame Strike (5th-Level; V, S)', desc: 'A 10-foot-radius, 40-foot-high column of divine flame appears centered on a point the god can see within 60 feet. Each creature in the area makes a DC 17 Dexterity saving throw, taking 14 (4d6) fire damage and 14 (4d6) radiant damage on a failed save, or half damage on a success.' }
combat:
    - { name: 'On its turn, the forgotten god prefers Flawed Spellcasting, surrounding itself with spirit guardians or blasting creatures with flame strike', desc: 'It tries to be within 10 feet of an enemy so it can attack with its divine weapon if the spell fails. It uses Divine Wrath when available. The god reserves its legendary actions for Stunning Glance, unless most targets have already made their saving throw against it.' }

---
```statblock
monster: Forgotten God - A5E
```
