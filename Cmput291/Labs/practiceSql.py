import sqlite3

conn = sqlite3.connect('./movie.db')
c = conn.cursor()

c.execute('''
    DROP TABLE movie;
    ''')

c.execute('''
    CREATE TABLE movie (
        title text,
        movie_number int,
        primary key (title));
        ''')

c.execute('''
            alter table movie add year integer;''')

c.execute('''alter table movie add duration integer;''')

c.execute('''
            insert into movie values
            ('Spiderman', 1 ,2000, 100),
            ('The Dark Knight', 2, 2008, 152),
            ('Zootopia', 3, 2016, 108);
            ''')

movie_number = (1,)
c.execute('''
            select *
            from movie
            where movie_number = ?;
            ''', movie_number)

row = c.fetchone()

print(row[0])

"""
c.execute('select * from movie;')
rows = c.fetchall()
print(rows)
"""

conn.row_factory = sqlite3.Row

c.execute('select * from movie;')

row = c.fetchone()

print(row.keys())

conn.commit()
conn.close()