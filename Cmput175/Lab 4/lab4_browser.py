#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:Simulate how search history is stored
#
# Author: Ethan Chiu
# Collaborators/references: stackOverflow
#----------------------------------------------------

def getAction():
    '''
    prompts user for a action
    Inputs: none
    Returns: what action the user requests
    '''
    availActions = ['=', '<', '>', 'q']
    userAction = input('Enter "=" to enter a URL, "<" to go back, ">" to go forward, "q" to quit: ')  
    if userAction not in availActions:
        print('Invalid Entry')
        return getAction()
    else:
        return userAction


def goToNewSite(current, pages):
    '''
    prompts user to enter a address and goes to it
    Inputs: current index, list of pages
    Returns: address
    '''   
    site = input('URL: ')
    current += 1
    pages.insert(current, site)
    for i in range(len(pages) - (current + 1)):
        pages.pop()
    return current

    
def goBack(current, pages):
    '''
    goes back a page if possible
    Inputs: current index, list of pages
    Returns: current index
    '''    
    if current - 1 >= 0:
        current -= 1
        return current
    else:
        print('Cannot go Back')
        return current


def goForward(current, pages):
    '''
    goes forward a page if possible
    Inputs: current index, list of pages
    Returns: current index
    '''    
    try:
        pages[current + 1]
        current += 1
        return current
    except IndexError:
        print('Cannot go Forward')
        return current


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()

'''
Worksheet Questions
Step 1: Web browser opened; home page displayed
webpages: www.cs.ualberta.ca
currentIndex: 0
Cannot go forward, cannot go back. No change to webpages or currentIndex.

Step 2: Go to new site; www.google.ca displayed
webpages: www.cs.ualberta.ca | www.google.ca
currentIndex: 1

Step 3: Go back to previous page; www.cs.ualberta.ca displayed
webpages: www.cs.ualberta.ca | www.google.ca
currentIndex: 0
Complete the rest (draw extra boxes for list elements, as needed)…

Step 4: Go forward to next page; www.google.ca displayed
webpages: www.cs.ualberta.ca | www.google.ca
currentIndex: 1

Step 5: Go to new site; www.docs.python.org displayed
webpages: www.cs.ualberta.ca | www.google.ca | www.docs.python.org
currentIndex: 2

Step 6: Go back to previous page; www.google.ca displayed
webpages: www.cs.ualberta.ca | www.google.ca | www.docs.python.org
currentIndex: 1

Step 7: Go back to previous page; www.cs.ualberta.ca displayed
webpages: www.cs.ualberta.ca | www.google.ca | www.docs.python.org
currentIndex: 0

Step 8: Go to new site; www.beartracks.ualberta.ca displayed
webpages: www.cs.ualberta.ca | www.beartracks.ualberta.ca
currentIndex: 1

Step 9: Try to go forward, but can’t; www.beartracks.ualberta.ca displayed
webpages: www.cs.ualberta.ca | www.beartracks.ualberta.ca
currentIndex: 1

Step 10: Go back to previous page; www.cs.ualberta.ca displayed
webpages: www.cs.ualberta.ca | www.beartracks.ualberta.ca
currentIndex: 0

Step 11: Go forward to next page; www.beartracks.ualberta.ca displayed
webpages: www.cs.ualberta.ca | www.beartracks.ualberta.ca
currentIndex: 1
'''
    