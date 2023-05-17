import json
import os
import re
import yaml

# Load JSON files with monster data
with open('MM.json', 'r') as f:
    j = json.load(f)
keys = [n for n in list(j['Monsters'].keys()) if 'Monster' in n]
monsters = {}
for key in keys:
    for k, v in j['Monsters'][key].items():
        monsters[k] = v

# Unpack nested monsters
def unpack_recursive(monsters):

    temp = {}
    remove = []
    rec = False
    
    for monster_name, monster_data in monsters.items():
        if not monster_data.get('content'):
            remove.append(monster_name)
            for subname, subdata in monster_data.items():
                temp[subname] = subdata

    monsters.update(temp)
    for r in remove:
        del monsters[r]
        
    for monster_name, monster_data in monsters.items():
        if not monster_data.get('content'):
            rec = True
            break
            
    if rec:
        monsters = unpack_recursive(monsters)
    
    return monsters

monsters = unpack_recursive(monsters)

# Remove templates
remove = []
for monster_name, monster_data in monsters.items():
    if 'Template' in monster_name:
        remove.append(monster_name)
for r in remove:
    del monsters[r]

# Convert to YAML
def convert_to_yaml(monsters):
    yaml_data = {}
    for monster_name, monster_data in monsters.items():
        if monster_data.get('content'):
            content = monster_data['content']
            yaml_data[monster_name] = {
                "statblock": True,
                "name": monster_name,
                "size": "",
                "type": "",
                "subtype": "",
                "alignment": "",
                "ac": 0,
                "hp": 0,
                "hit_dice": "",
                "speed": "",
                "stats": [0, 0, 0, 0, 0, 0],
                "saves": [],
                "skillsaves": [],
                "damage_vulnerabilities": "",
                "damage_resistances": "",
                "damage_immunities": "",
                "condition_immunities": "",
                "senses": "",
                "languages": "",
                "cr": 0,
                "spells": [],
                "traits": [],
                "actions": [],
                "legendary_actions": [],
                "bonus_actions": [],
                "reactions": []
            }
            # Parse content
            # Size, type, alignment
            if content[0].startswith('*'):
                yaml_data[monster_name]['size'] = content[0].split()[0].replace('*', '')
                yaml_data[monster_name]['type'] = content[0].split()[1].replace(',', '')
                yaml_data[monster_name]['alignment'] = content[0].split()[2].replace('*', '')
            # Armor class
            if content[1].startswith('**Armor Class**'):
                yaml_data[monster_name]['ac'] = int(content[1].split()[2])
            # Hit points
            if content[2].startswith('**Hit Points**'):
                yaml_data[monster_name]['hp'] = int(content[2].split()[2])
                yaml_data[monster_name]['hit_dice'] = content[2].split()[3].replace('(', '').replace(')', '')
            # Speed
            if content[3].startswith('**Speed**'):
                yaml_data[monster_name]['speed'] = content[3].split('** ')[1]
            # Stats
            if isinstance(content[4], dict):
                for stat, value in content[4]['table'].items():
                    yaml_data[monster_name]['stats'][['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'].index(stat)] = int(value[0].split()[0])

            last = 5
            for i in range(5, len(content)):
                # Saving throws
                if content[i].startswith('**Saving Throws**'):
                    for save in content[i].split('** ')[1].split(', '):
                        yaml_data[monster_name]['saves'].append({save.split()[0]: save.split()[1].replace('+','').replace('-','')})
                    last = i
                # Skills
                if content[i].startswith('**Skills**'):
                    for skill in content[i].split('** ')[1].split(', '):
                        yaml_data[monster_name]['skillsaves'].append({skill.split()[0]: skill.split()[1].replace('+','').replace('-','')})
                    last = i
                # Senses
                if content[i].startswith('**Senses**'):
                    yaml_data[monster_name]['senses'] = content[i].split('** ')[1]
                    last = i
                # Languages
                if content[i].startswith('**Languages**'):
                    yaml_data[monster_name]['languages'] = content[i].split('** ')[1]
                    last = i
                # Challenge
                if content[i].startswith('**Challenge**'):
                    cr = content[i].split('** ')[1].split()[0]
                    # convert cr to decimal
                    cr = float(cr) if cr.isdigit() else float(cr.split('/')[0]) / float(cr.split('/')[1])
                    yaml_data[monster_name]['cr'] = cr
                    last = i
                # Damage vulnerabilities
                if content[i].startswith('**Damage Vulnerabilities**'):
                    yaml_data[monster_name]['damage_vulnerabilities'] = content[i].split('** ')[1]
                    last = i
                # Damage resistances
                if content[i].startswith('**Damage Resistances**'):
                    yaml_data[monster_name]['damage_resistances'] = content[i].split('** ')[1]
                    last = i
                # Damage immunities
                if content[i].startswith('**Damage Immunities**'):
                    yaml_data[monster_name]['damage_immunities'] = content[i].split('** ')[1]
                    last = i
                # Condition immunities
                if content[i].startswith('**Condition Immunities**'):
                    yaml_data[monster_name]['condition_immunities'] = content[i].split('** ')[1]
                    last = i

            # Extract Spells
            for i in range(5, len(content)):
                if 'Innate Spellcasting.' in content[i]:
                    desc = content[i].split('** ')[1]

                    # Split the string using regex
                    split_list = re.split(r"\s+(?=\d/|\*)", content[i+1])

                    # Process the split list to obtain the desired format
                    result_list = []
                    for item in split_list:
                        if ":" in item:
                            key, values = item.split(":")
                            key = key.strip()
                            values = [value.strip("* ") for value in re.findall(r"\*(.*?)\*", values)]
                            if values:
                                result_list.append(key)
                                result_list.append(values)
                            else:
                                result_list.append(item.strip())
                        elif "*" in item:
                            values = [value.strip("* ") for value in re.findall(r"\*(.*?)\*", item)]
                            result_list.append(values)
                        else:
                            result_list.append(item.strip())
                    yaml_data[monster_name]['spells'].append(desc)
                    indexes = []
                    for idx, item in enumerate(result_list):
                        if ':' in item:
                            indexes.append(idx)
                    for idx in indexes:
                        if idx != indexes[-1]:
                            left = result_list[idx]
                            right = result_list[idx + 1: indexes[indexes.index(idx) + 1]]
                            # flatten right list
                            right = [item for sublist in right for item in sublist]
                            # surround right list with brackets
                            right = [f"[[{item}]]" for item in right]
                            # append to spells as string
                            spell_str = f"{left} {', '.join(right)}"
                            yaml_data[monster_name]['spells'].append(spell_str)
                    # remove spell lines from content
                    content = content[:i] + content[i+2:]
                    break

            # Other content
            index_tuples = []
            for i in range(5, len(content)):
                if '*Actions*' in content[i]:
                    index_tuples.append(('actions', i))
                elif '*Legendary Actions*' in content[i]:
                    index_tuples.append(('legendary_actions', i))
                elif '*Bonus Actions*' in content[i]:
                    index_tuples.append(('bonus_actions', i))
                elif '*Reactions*' in content[i]:
                    index_tuples.append(('reactions', i))
            
            # sort index_tuples by index
            index_tuples = sorted(index_tuples, key=lambda x: x[1])
            if len(content) > last:
                if index_tuples:
                    traits = content[last + 1:index_tuples[0][1]]
                else:
                    traits = content[last + 1:]
            # Use re to split on asterisks (2-3), extract two groups: name and description
            for trait in traits:
                if trait.startswith('*'):
                    name = re.split('\*{1,3}', trait)[1]
                    description = re.split('\*{1,3}', trait)[2]
                    yaml_data[monster_name]['traits'].append({
                        'name': name,
                        'desc': description
                    })
            # Other content
            for key, i in index_tuples:
                if key == 'actions':
                    if index_tuples.index((key, i))+1 < len(index_tuples):
                        stop = index_tuples[index_tuples.index((key, i))+1][1]
                    else:
                        stop = len(content)
                    actions = content[i+1:stop]
                    for action in actions:
                        if action.startswith('*'):
                            name = re.split('\*{1,3}', action)[1]
                            description = re.split('\*{1,3}', action)[2:]
                            # join description list into string
                            description = ''.join(description)
                            # insert * to beginning of description
                            yaml_data[monster_name]['actions'].append({
                                'name': name,
                                'desc': description
                            })
                elif key == 'legendary_actions':
                    if index_tuples.index((key, i))+1 < len(index_tuples):
                        stop = index_tuples[index_tuples.index((key, i))+1][1]
                    else:
                        stop = len(content)
                    legendary_actions = content[i+1:stop]
                    for legendary_action in legendary_actions:
                        if legendary_action.startswith('*'):
                            name = re.split('\*{1,3}', legendary_action)[1]
                            description = re.split('\*{1,3}', legendary_action)[2]
                            yaml_data[monster_name]['legendary_actions'].append({
                                'name': name,
                                'desc': description
                            })
                        else:
                            yaml_data[monster_name]['legendary_actions'].append({
                                'name': 'Legendary Action',
                                'desc': legendary_action
                            })
                elif key == 'bonus_actions':
                    if index_tuples.index((key, i))+1 < len(index_tuples):
                        stop = index_tuples[index_tuples.index((key, i))+1][1]
                    else:
                        stop = len(content)
                    bonus_actions = content[i+1:stop]
                    for bonus_action in bonus_actions:
                        if bonus_action.startswith('*'):
                            name = re.split('\*{1,3}', bonus_action)[1]
                            description = re.split('\*{1,3}', bonus_action)[2]
                            yaml_data[monster_name]['bonus_actions'].append({
                                'name': name,
                                'desc': description
                            })
                elif key == 'reactions':
                    if index_tuples.index((key, i))+1 < len(index_tuples):
                        stop = index_tuples[index_tuples.index((key, i))+1][1]
                    else:
                        stop = len(content)
                    reactions = content[i+1:stop]
                    for reaction in reactions:
                        if reaction.startswith('*'):
                            name = re.split('\*{1,3}', reaction)[1]
                            description = re.split('\*{1,3}', reaction)[2]
                            yaml_data[monster_name]['reactions'].append({
                                'name': name,
                                'desc': description
                            })
    # rename 'traits' to 'straits'
    for monster_name, monster_data in yaml_data.items():
        if monster_data.get('traits'):
            monster_data['straits'] = monster_data.pop('traits')

    return yaml_data

# Extract spells from monster traits
def extract_spells(yaml_data):
    monster_list = []
    for monster_name, monster_data in yaml_data.items():
        if monster_data.get('traits'):
            for trait in monster_data['traits']:
                for name, description in trait.items():
                    if name == 'Innate Spellcasting.':
                        monster_list.append(monster_name)
    return monster_list

yaml_data = convert_to_yaml(monsters)

# Export to individual yaml files with four spaces
for monster_name, monster_data in yaml_data.items():
    # change monster_name to escape slashes
    monster_name = monster_name.replace('/', '-')
    # Paste yaml into markdown file per:
    # ---
    # monster_data
    # ---
    # ```statblock
    # monster: monster_name
    # ```
    monster_data = '---\n' + yaml.dump(monster_data, default_flow_style=False, indent=4) + '---\n```statblock\nmonster: ' + monster_name + '\n```' 

    with open(f'./5eMM/{monster_name}.md', 'w') as f:
        f.write(monster_data)




