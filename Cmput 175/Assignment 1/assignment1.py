#----------------------------------------------------
# Assignment 1
# 
# Author: Ethan Chiu
# Collaborators: None
# References: Python Documentation, Stack Overflow
#----------------------------------------------------
# Note to TA: This got really messy, I'm still not 100%
# what the best way to use a dictionary is but I can
# tell this was NOT it. Please have mercy.
#----------------------------------------------------
"""
this program takes 4 different files of a stores stock of items, as well as supplier
information and makes a text document of a reciept of items the store must by to replenish their stock.
refrences: python documentation, StackOverflow
"""
def readFiles():
    toRead = ['products.txt', 'suppliers.txt', 'availability.txt', 'onshelves.txt']
    toSplit = []
    # open and read each file into a list to be split and sorted
    for i in toRead:
        tempFile = open(i, 'r')
        toSplit.append(tempFile.read())
        tempFile.close()
    return toSplit

def makeInventory(toSplit):
    """ 
    this function takes each set of text and splits them into a dictionary

    input - list of texts to split
    output - inventory of the store
    """
    splitText = [[],[]]
    # split the first list of products into a dictionary of lists.
    # replace \n with ; first to make splitting easier.
    splitText[0] = toSplit[0].replace('\n', ';').split(';')
    # split the list of onshelves to add to the dictionary of inventory items
    splitText[1] = toSplit[3].replace('\n', '#').split('#') 
    # Inventory is a dictionary of the stock of items, where the key is the id number of the product
    # and the value is a list in the form [name, amount].
    inventory = dict()
    while len(splitText[0]) >= 2:
        inventory[splitText[0].pop(0)] = [splitText[0].pop(1)]
    while len(splitText[1]) > 1:
        inventory[splitText[1].pop(0)].append(splitText[1].pop(0))
    return inventory

def makeContacts(toSplit):
    """
    this function makes lists of supplier's contacts as well as the availability of their products

    input - lists of texts to split
    output - contacts of supplier, products each supplier sells
    """
    splitStore, splitSelling = [], []
    # split the list of suppliers into a dictionary of lists
    splitStore = toSplit[1].replace('\n',';').split(';')
    splitSelling = toSplit[2].replace('\n', ',').split(',')
    # Contacts is a dictionary of the supplier info, where the key is the phone number
    # and the value is a list in the form [store name, address].
    # Available is a dictionary of a suppliers stock, where the key is the phone numeber
    # and the value is a list in the form [product, price].
    contacts = dict()
    available = dict()
    while len(splitStore) >= 3:
        contacts[splitStore.pop(0)] = [splitStore.pop(1), splitStore.pop(1)]
    while len(splitSelling) >= 3:
        key = splitSelling.pop(1)
        if key in available:
            available[key].append([splitSelling.pop(0), splitSelling.pop(0)])
        else:
            available[key] = ([[splitSelling.pop(0), splitSelling.pop(0)]])
    return contacts, available

def makeOrders(inventory, contacts, available):
    """ This function checks inventory values to determine if items need to be bought.
    If a item does, it is added to a list.
    Returns list of items to buy and amount, as well as a list of who to buy from

    input - inventory, contacts, product availability
    output - amount of products to buy, suppliers to buy from
    """
    # nested list of things to buy, where the list is [product code, amount to buy]
    toBuy = []
    for invKey, invList in inventory.items():
        if int(invList[1]) < 50:
            toBuy.append([invKey, 50 - int(invList[1])])
    buyFrom = comparePrice(toBuy, inventory, contacts, available)
    return buyFrom

def comparePrice(toBuy, inventory, contacts, available):
    """
    This functions compares the prices offered by different stores and chooses the
    most competitive price per item.
    Returns nested dictionary where all the details of an item, as where as you need to buy it from are listed.
    This is the final set of data needed.

    input - products to buy, availability of sellers
    output - who to buy from
    """
    # dictionary of list of suppliers to buy from, where the list is [product code, who to buy from]
    buyFrom = {}
    for i in toBuy:
        itemCode = i[0]
        bestSeller = None
        bestPrice = None
        for availKey, availList in available.items():
            for product in availList:
                if bestSeller == None and product[0] == itemCode:
                    bestSeller = availKey
                    bestPrice = product[1]
                else:
                    if  product[0] == itemCode and product[1] < bestPrice:
                        bestPrice = product[1]
                        bestSeller = availKey
        buyFrom[itemCode] = {
            'name': inventory[itemCode],
            'quantity': i[1],
            'supplier': contacts[bestSeller][0],
            'number': bestSeller,
            'cost': float(bestPrice) * i[1]
            }
    return buyFrom

def findBigSeller(buyFrom, recieptContent):
    """
    This function finds the order(s) with the largest total cost
    and adds the seller information at the end of the reciept
    
    input - what to buy, who to buy from, contacts, reciept content
    output - receipt content
    """
    biggestKey = None
    biggestPrice = None
    for key, product in buyFrom.items():
        if biggestPrice == None:
            biggestKey = [key]
            biggestPrice = [product['cost']]
        elif product['cost'] == biggestPrice[0]:
            biggestKey.append(key)
        elif product['cost'] > biggestPrice[0]:
            biggestKey = [key]
            biggestPrice = [product['cost']]
    for i in range(len(biggestKey)):
        recieptContent += ('\nHighest Cost: ' + buyFrom[biggestKey[i]]['supplier'] + ' ' + '(' + buyFrom[biggestKey[i]]['number'][:3] + ') ' + buyFrom[biggestKey[i]]['number'][3:6] + ' ' + buyFrom[biggestKey[i]]['number'][6:10] + ' [$' + str(buyFrom[biggestKey[i]]['cost']) + ']')
    return recieptContent
    
def printReciept(buyFrom):
    """
    This function takes the dictionary buyFrom in order to make a reciept

    input - buyFrom
    output - .txt file of the reciept
    """
    reciept = open('orders.txt', 'w')
    # constants that will be used in the reciept
    rowBorder = ('+' + '-' * 14 + '+' + '-' * 18 + '+' + '-' * 8 + '+' + '-' * 16 + '+' + '-' * 10 + '+')
    columnTitle = ('\n| Product Code | Product Name     |Quantity| Supplier       | Cost     |')
    recieptContent = rowBorder + columnTitle
    # for every product to buy, add the supplier and cost to the content string
    totalCost = 0.0
    for key, product in buyFrom.items():
        if product['quantity'] > 40:
            supplier = ('*' + product['supplier'][:15])
        else:
            supplier = product['supplier'][:16]
        recieptContent += ('\n|  ' + key + '   | ' +  '%-16s' % supplier + ' |' + '%7s' % str(product['quantity']) + ' | (' + product['number'][:3] + ') ' + product['number'][3:6] + ' ' + product['number'][6:10] + ' | $' + '%7s' % str('%.2f' % product['cost']) + ' |')
        totalCost += product['cost']
    recieptContent += ('\n' + rowBorder)
    # add total cost
    recieptContent += ('\n| Total cost   |                $ ' + '%9.2f' % totalCost + '|')
    recieptContent += ('\n' + '+' + '-' * 14 + '+' + '-' * 27 + '+')
    # find the supplier(s) with the largest order
    recieptContent = findBigSeller(buyFrom, recieptContent)
    reciept.write(recieptContent)
    print(recieptContent)

def main():
    # read files needed
    toSplit = readFiles()
    # functions to make the needed dictionaries
    inventory = makeInventory(toSplit)
    contacts, available = makeContacts(toSplit)
    # function to stock items
    buyFrom = makeOrders(inventory, contacts, available)
    printReciept(buyFrom)
    input()

main()