#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: Ethan Chiu
# Collaborators/references: Stack Overflow
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    prompts user for a action
    Inputs: none
    Returns: what action the user requests
    '''
    availActions = ['=', '<', '>', 'q']
    userAction = input('Enter "=" to enter a URL, "<" to go back, ">" to go forward, "q" to quit: ')  
    if userAction not in availActions:
        raise ValueError('Invalid entry')
    else:
        return userAction

def goToNewSite(current, bck, fwd):
    '''
    prompts user to enter a address and goes to it
    Inputs: current site, back and forward stacks
    Returns: new current site
    '''   
    bck.push(current)
    site = input('URL: ')
    current = site
    fwd.clear()
    return current
    
def goBack(current, bck, fwd):
    '''
    goes back a page if possible
    Inputs: current site, back and forward stacks
    Returns: new current site
    '''    
    try:
        site = bck.pop()
        fwd.push(current)
        current = site
        return current
    except Exception:
        print("Cannot go back.")
        return current

def goForward(current, bck, fwd):
    '''
    goes forward a page if possible
    Inputs: current site, back and forward stacks
    Returns: new current site
    '''    
    try:
        site = fwd.pop()
        bck.push(current)
        current = site
        return current
    except Exception:
        print("Cannot go forward.")
        return current

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    