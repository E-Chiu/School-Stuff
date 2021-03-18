#q1
bulbPrice = {
    'daffodil':0.35,
    'tulip':0.33,
    'crocus':0.25,
    'hyacinth':0.75,
    'bluebell':0.50
}
bulbStock = {}
# q2
year = 1
bulbStock['daffodil'] = year * 50
bulbStock['tulip'] = year * 100
#q3
bulbPrice['tulip'] = "%.2f"% (bulbPrice['tulip'] * 1.25)
bulbPrice['tulip'] = float(bulbPrice['tulip'])
#q4
bulbStock['hyacinth'] = 30
#q5
print("You have purchased the following bulbs:")
recieptList = []
for i in bulbStock.keys():
    recieptList.append(i)
recieptList.sort()
totalCount = 0
totalCost = 0
for i in recieptList:
    temp = i[:3].upper()
    print("%-5s"% (temp), '*', "%4d"% (bulbStock[i]), '= $', "%6.2f"% (bulbPrice[i] * bulbStock[i]))
    totalCount += bulbStock[i]
    totalCost += bulbPrice[i] * bulbStock[i]
totalCost = "%.2f"% (totalCost)
print('\n Thank you for purchasing ' + str(totalCount) + ' bulbs from Bluebell Greenhouses.')
print('Your total comes to $ ' + "%-6s"% (str(totalCost) + '.'))
 