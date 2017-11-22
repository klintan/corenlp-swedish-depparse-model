# clean conll files

with open('sv-ud-dev.conllu') as f: 
	content = f.readlines()

content = [x for x in content if not x.startswith('#')]

with open('swedish-dev.conllu', 'w') as p:
	p.write("".join(content))