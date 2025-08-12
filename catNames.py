catNames = []
while True:
 print('Enter name of cat ' + str(len(catNames) + 1) + ' Or nothing to stop:')
 name = input()
 if name == '':
  break
 catNames = catNames + [name]

print('Cat names are...')
for name in catNames:
 print('  ' + name)
 
cat = ['fat','gray','loud']
size, color, disposition = cat
print(disposition)
