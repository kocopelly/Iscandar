---
casting_time: 1 action
classes:
- Bard
- Cleric
- Druid
- Sorcerer
components: V, S, M (fur or a feather from a beast)
concentration: true
description: "You touch a creature and bestow upon it a magical enhancement. Choose\
    \ one of the following effects; the target gains that effect until the spell ends.\n\
    **Bear\u2019s Endurance**. The target has advantage on Constitution checks. It\
    \ also gains 2d6 temporary hit points, which are lost when the spell ends.\n**Bull\u2019\
    s Strength**. The target has advantage on Strength checks, and his or her carrying\
    \ capacity doubles.\n**Cat\u2019s Grace**. The target has advantage on Dexterity\
    \ checks. It also doesn\u2019t take damage from falling 20 feet or less if it\
    \ isn\u2019t incapacitated.\n**Eagle\u2019s Splendor**. The target has advantage\
    \ on Charisma checks.\n**Fox\u2019s Cunning**. The target has advantage on Intelligence\
    \ checks.\n**Owl\u2019s Wisdom**. The target has advantage on Wisdom checks.\n\
    **At Higher Levels**. When you cast this spell using a spell slot of 3rd level\
    \ or higher, you can target one additional creature for each slot level above\
    \ 2nd."
duration: Concentration, up to 1 hour.
level: 2
name: Enhance Ability
range: Touch
ritual: false
school: transmutation
short_description: 2nd-level transmutation
source: 5ePHB
---

| `=this.name` | `=this.short_description` |
| ------------ | ------------------------- |
| Classes      | `=this.classes`           |
| Components   | `=this.components`        |
| Duration     | `=this.duration`          |
| Description  | `=this.description`       |