# assignment3.py by echiu and sowon
# mar 13, 2021
# CMPUT 291 B1

import sqlite3

#---open database and make cursor---
conn = sqlite3.connect('./A3.db')
c = conn.cursor()
c.execute('pragma foreign_keys=on;')

def query1():
    # ask for area
    area = input("Enter an area to list the titles of accepted"
    " papers in the given area in descending order of their overall"
    " review score.\nArea: ")
    # run query
    c.execute('''
        select distinct p.title from papers p, reviews r
        where r.paper = p.id and p.area = ? and p.decision = \'A\'
        group by p.title
        order by avg(r.overall) desc;
        ''', (area,))
    rows = c.fetchall()
    if len(rows) == 0: # if nothing is returned tell user
        print("There are no accepted papers in this area")
    else:   
        print("Accepted papers in this area:")
        for i in range(len(rows)):
            print(rows[i][0])

def query2():
    #ask for email
    email = input("Enter a user's email to list the titles of papers"
    "were assigned to review.\nEmail: ")
    # run query
    c.execute('''
        select p.title from papers p, reviews r, users u 
        where r.paper = p.id and r.reviewer = u.email and u.email = ?
        order by p.id;
    ''', (email,))
    rows = c.fetchall()
    if len(rows) == 0: # if nothing is returned tell user
        print("No paper has been assigned to this reviewer")
    else:
        print("Papers assigned to this user:")
        for i in range(len(rows)):
            print(rows[i][0])

def query3():
    try:
        # ask for percentage
        x = float(input("Enter a percentage (X%) for which to find inconsistent"
        " papers.\nX: "))
        per = x/100 # get decimal form
        # run query
        c.execute('''
            select distinct p.id as ID, p.title as TITLE from papers p, reviews r 
            where r.paper = p.id and 
                ? < abs(1 - r.overall /(
                select avg(r2.overall) 
                from reviews r2
                where r2.paper = p.id
                )
            );
            ''', (per,))
        rows = c.fetchall()
        if len(rows) == 0: # if nothing is returned tell user
            print("No papers are inconsistent when X = " + str(x))
        else:
            print("The following papers are inconsistent when X = " + str(x) + ":")
            for i in range(len(rows)):
                for j in range(len(rows[i])):
                    print(rows[i][j], end=" ")
                print("")
    except: # if not a number is entered
        print("A number was not entered")

def query4():
    try:
        # ask for the range
        print("Enter a range from X to Y.")
        x = float(input("X: "))
        y = float(input("Y: "))
        print("Searching for reviewers that have reviewed a paper with a difference" +
        "score between " + str(x) + "and " + str(y))
        # run query
        c.execute('''
            select u.email, u.name
            from users u, DiffScore d, papers p, reviews r
            where p.id = d.pid and p.id = r.paper and r.reviewer = u.email and
            d.difference > ? and d.difference < ?;
            ''', (x,y,))
        rows = c.fetchall()
        if len(rows) == 0: # if nothing is returned tell user
            print("No users were found")
        else:
            print("The following users were found:")
            for i in range(len(rows)):
                print(rows[i][0])
    except: # if a number is not entered
        print("A number was not entered")

def makeView():
    # makes the DiffScore view for later use in query 4
    c.execute("drop view if exists DiffScore") # if the view has previously been made clear it
    c.execute('''create view DiffScore as
        select distinct id as pid, title as ptitle, abs(pOverall - areaAvg) as difference
            from (
                select avg(r.overall) as areaAvg, p.area as avgArea
                from reviews r, papers p
                where r.paper = p.id 
                group by p.area
            )
            LEFT OUTER JOIN (
                select avg(r.overall) as pOverall, p.area as pArea, p.id, p.title
                from papers p, reviews r
                where r.paper = p.id
                group by p.id
            )
            on pArea = avgArea
        order by pid
        ''')

def main():
    makeView() # make the view DiffScore
    print("Welcome to the confrence management system")
    exitBool = False
    # loop indefinetley until exit option is chose
    while not exitBool:
        print("Please select an option by entering a number:\n"
        "1. Find accepted papers\n"
        "2. Find papers assigned for review\n"
        "3. Find papers with inconsistent reviews\n"
        "4. Find papers according to difference score\n"
        "5. Exit")
        # ask user for option
        option = input("Option: ")
        if option == '1':
            query1()
        elif option == '2':
            query2()
        elif option == '3':
            query3()
        elif option == '4':
            query4()
        elif option == "5":    
            exitBool = True
        else:
            print("Please enter a valid number")
        print("\n\n") # add whitespace after every choice or query just to make things more visually clear

main()

# finishing up
conn.commit()
conn.close()