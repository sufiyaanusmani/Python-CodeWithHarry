import re

# findall, search, split, sub, finditer
# pattr = re.compile(r'fass')
# pattr = re.compile(r'.')
# pattr = re.compile(r'.adm')
# pattr = re.compile(r'^adm')

matches = pattr.finditer(myStr)

for match in matches:
    print(match)
