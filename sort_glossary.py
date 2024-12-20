import yaml

with open('glossary.yaml', 'r') as f:
    glossary = yaml.safe_load(f)

# check for duplicates
terms = set()
for item in glossary:
    term = item['en'] if isinstance(item['en'], str) else item['en'][0]
    if term in terms:
        assert False, f'Duplicate term: {term}'
    terms.add(term)


# sort by term
def sort_key(x):
    if isinstance(x['en'], str):
        return x['en'].lower()
    return x['en'][0].lower()

glossary_sorted = sorted(glossary, key=sort_key)

# write to file
yaml_str = yaml.dump(
    glossary_sorted,
    default_flow_style=False,
    allow_unicode=True,
    indent=2)

yaml_str = yaml_str.replace("  - ", "    - ")

with open('glossary_sorted.yaml', 'w') as f:
    f.write(yaml_str)
