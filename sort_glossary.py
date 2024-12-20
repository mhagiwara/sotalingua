import yaml

def sort_key(x):
    if isinstance(x['en'], str):
        return x['en'].lower()
    return x['en'][0].lower()

glossary_sorted = []
with open('glossary.yaml', 'r') as f:
    glossary = yaml.safe_load(f)
    glossary_sorted = sorted(glossary, key=sort_key)

yaml_str = yaml.dump(
    glossary_sorted,
    default_flow_style=False,
    allow_unicode=True,
    indent=2)

yaml_str = yaml_str.replace("  - ", "    - ")

with open('glossary_sorted.yaml', 'w') as f:
    f.write(yaml_str)
