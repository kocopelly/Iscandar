import json
import os
import re
import yaml

# Convert table dictionaries
# {'d10': ['1', '2–6', '7–8', '9–10'],
#  'Behavior': ['The creature uses all its movement to move in a random direction. To determine the direction, roll a d8 and assign a direction to each die face. The creature doesn’t take an action this turn.',
#   'The creature doesn’t move or take actions this turn.',
#   'The creature uses its action to make a melee attack against a randomly determined creature within its reach. If there is no creature within its reach, the creature does nothing this turn.',
#   'The creature can act and move normally.']}
def table_to_string(table):
    # zip table values
    table = list(zip(*table.values()))
    # convert to string
    table = '\n*'.join([':* '.join(row) for row in table])
    # insert * before table
    table = '*' + table
    return table


# Load JSON files with monster data
with open('spells.json', 'r') as f:
    j = json.load(f)

# Import spell lists
spell_lists = j['Spellcasting']['Spell Lists']

# Convert level string to int
def level_str_to_int(level_str):
    if level_str == 'Cantrips (0 Level)':
        return 0
    else:
        return int(re.search(r'\d+', level_str).group())

# Create spell data
spell_data = {}
for class_name, spell_list in spell_lists.items():
    for level_str, spells in spell_list.items():
        for spell in spells:
            if spell not in spell_data:
                spell_data[spell] = {
                    'classes': [],
                    'level': level_str_to_int(level_str)
                }
            spell_data[spell]['classes'].append(class_name.replace(' Spells', ''))

bad = []
# Load spell descriptions
for spell, data in j['Spellcasting']['Spell Descriptions'].items():
    if not data.get('content'): continue
    data = data['content']
    # Split long lines
    new = []
    for d in data:
        # if d is not a string skip
        if type(d) != str: 
            new.append(d)
            continue
        # insert newlines before each **Text:** with regex
        d = re.sub(r'(\*\*.?:\*\*)', r'\n\1', d).strip()
        # use re to replace '**:' with ':**'
        d = re.sub(r'\*\*:', ':\*\*', d)
        # split on newlines and insert into data
        new.extend(d.split('\n'))
    data = new


    updates = {
        'ritual': False, 
        'concentration': False,
        'name': spell,
        'source': '5ePHB',
        }
    last = 0
    for i, d in enumerate(data):
        updates['school'] = data[0].split(' ')[1].replace('*', '')
        updates['short_description'] = data[0].replace('*', '')
        if 'ritual' in data[0].lower():
            updates['ritual'] = True
        if type(d) != str: continue
        if d.startswith('**Casting Time'):
            updates['casting_time'] = d.split('* ')[1]
            last = i
        elif d.startswith('**Range'):
            updates['range'] = d.split('* ')[1]
            last = i
        elif d.startswith('**Components'):
            updates['components'] = d.split('* ')[1]
            last = i
        elif d.startswith('**Duration'):
            updates['duration'] = d.split('* ')[1]
            # check for concentration
            if 'concentration' in d.lower():
                updates['concentration'] = True
            last = i
    # if spell == 'Augury':
        # break
    description_lines = data[last+1:]
    desc = ''
    for line in description_lines:
        # if line is list convert to bullets
        if type(line) == list:
            # convert list to bullets
            line = '\n'.join(['* ' + l for l in line])
        if type(line) == dict:
            # convert table to string
            line = table_to_string(line['table'])
        desc = desc + '\n' + line
    desc = desc.strip().replace('***', '*').replace('**', '*').replace('*', '**')
    updates['description'] = desc
    spell_data[spell].update(updates)

# Export to individual yaml files with four spaces
for spell_name, spell_data in spell_data.items():
    # Replace slashes in spell names
    spell_name = spell_name.replace('/', '-')
    spell_data = '---\n' + yaml.dump(spell_data, default_flow_style=False, indent=4) + '---\n' 
    spell_data = spell_data + '''
| `=this.name` | `=this.short_description` |
| ------------ | ------------------------- |
| Classes      | `=this.classes`           |
| Components   | `=this.components`        |
| Duration     | `=this.duration`          |
| Description  | `=this.description`       |'''
    with open(f'./spells/{spell_name}.md', 'w') as f:
        f.write(spell_data)