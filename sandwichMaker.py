import pyinputplus as pyip

#breadtype=wheat,white,protein
#proteintype:chicken,turkey,ham,tofu
#inputyesno to ask if they want cheese
#inputMenu() to ask for cheese type: cheddar, swiss, mozz
#inputYesNo to ask if they want mayo, mustard, lettuce, tomato

print("Choose bread type.")
breadResponse = pyip.inputMenu(['Wheat','White','Sourdough'])
print("Choose protein type.")
proteinResponse = pyip.inputMenu(['Chicken','Turkey','Ham','Tofu'])
print("Do you want cheese?")
cheeseOption = pyip.inputYesNo()
menuPrices = {'Wheat':1,'White':2,'Sourdough':3,
'Chicken':4,'Turkey':5,'Ham':6,'Tofu':7,
'Cheddar':8,'Swiss':9,'Mozzarella':10,'':0}


#print(cheeseOption)
cheeseResponse = ''
if cheeseOption == 'yes':
    print ("Chose yes")
    cheeseResponse = pyip.inputMenu(['Cheddar','Swiss','Mozzarella'])
    #return cheeseResponse
else:
    print ("Chose no")
    cheeseResponse = ''

totalValue = int(menuPrices[breadResponse]) + int(menuPrices[proteinResponse]) + int(menuPrices[cheeseResponse])
print("Your total cost is: ",totalValue)
