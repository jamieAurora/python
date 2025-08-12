#inventory = {'rope':1, 'torch':2, 'gold coin':42}

#def displayInventory(inventory):
 #item_total = 0
 #for k, v in inventory.items():
 # print(k,":", v)
 # item_total = item_total + v
# print("Item Total: ", item_total)
#displayInventory(inventory)

"""def addToInventory(inventory, addedItems):
 newDict = {}
 #write code
 i = 0
 while i < len(addedItems): 
  print(addedItems[i])
  for k, v in inventory.items():
   if k == addedItems[i]:
    print("Found Match")
    #v+= 1
    inventory.update({k:v + 1})
   else:
    print("No Match")
    newDict.update({addedItems[i]: 1})
  
  i+= 1
 print("newdict",newDict)
 #for k, v in newDict.items():
  #inventory.update({k:v})
 print("Inventory",inventory)"""

def addToInventory(inventory, addedItems):
    new_dict = {}
    for item in addedItems:
        if item in inventory:
            # if there's already a key in the inventory dict...
            inventory[item] += 1
            # ...then set the key equal to its current value + 1, incrementing it
        else:
            # if there isn't already a key in the inventory dict...
            new_dict[item] = 1
            # update newDict with the new key, and value, which will be 1

    print("newDict is: ", new_dict)
    print("inventory is: ", inventory)
    #return new_dict
    inventory.update(new_dict)
    print("Inventory is", inventory)
    
                


inv = {'gold coin':42,'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
#print(newDict)