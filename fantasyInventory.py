inventory = {'rope':1, 'torch':2, 'gold coin':42}

def displayInventory(inventory):
 item_total = 0
 for k, v in inventory.items():
  print(k,":", v)
  item_total = item_total + v
 print("Item Total: ", item_total)
displayInventory(inventory)