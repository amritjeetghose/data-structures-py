heros=['spider man','thor','hulk','iron man','captain america']
#1. Length of the list
print('array length:', len(heros))
#2. Add 'black panther' at the end of this list
heros.append('black panther')
for data in heros:
    print(f"data: {data}")
#3. You realize that you need to add 'black panther' after 'hulk',
#  so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
hulk_index=heros.index('hulk')
heros.insert(hulk_index+1,'black panther')
for data in heros:
    print(f"data: {data}")
#4. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code.
heros=[hero if hero not in ['thor','hulk'] else 'doctor strange' for hero in heros]
print("---------")
for data in heros:
    print(f"data: {data}")
#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
print("---------")
print(dir(heros))
heros.sort();
print("---------")
print(heros)