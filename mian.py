import sqlite3
import os
class ct():
    db = sqlite3.connect('data.db')
    cur = db.cursor()

    cur.execute(
    """CREATE TABLE IF NOT EXISTS book(
        name TEXT,
        writer TEXT,
        year INTEGER
    )"""
    )

    cur.execute(
    """CREATE TABLE IF NOT EXISTS writer(
        name TEXT,
        book TEXT,
        age INTEGER
    )"""
    )

    cur.execute(
    """CREATE TABLE IF NOT EXISTS member(
        name TEXT,
        id INTEGER,
        number INTEGER(11)
    )"""
    )

class book():
    def vorodi():
        name = input('Enter the book name : ')
        writer = input('Enter the writer name : ')
        year = input('Enter the published yera : ')
        ct.cur.execute(
            """INSERT INTO book(name , writer , year) VALUES(? , ? , ?)""",
            (name , writer , year)
        )
        ct.db.commit()
        ct.db.close()
    def update():
        print('What do you want to update : ')
        print('name --> 1')
        print('writer --> 2')
        print('year --> 3')
        update = int(input('Enter the number(1/2/3) : '))
        os.system('cls')
        defualt_val = input('Enter the defualt value : ')    
        update_val = input('Enter the update value : ')    
        if update == 1:
            ct.cur.execute(
                "UPDATE book SET name=? WHERE name=?",
                (update_val , defualt_val)
            )
        if update == 2:
            ct.cur.execute(
                "UPDATE book SET writer=? WHERE writer=?",
                (update_val , defualt_val)
            )        
        if update == 3:
            ct.cur.execute(
                "UPDATE book SET year=? WHERE year=?",
                (update_val , defualt_val)
            )      
        ct.db.commit()
        ct.db.close()
    def delete():
        print('What do you want to delete : ')
        print('name --> 1')
        print('writer --> 2')
        print('year --> 3')
        delete = int(input('Enter the number(1/2/3) : '))
        os.system('cls')
        delete_val = input('Enter the delete value : ')
        if delete == 1:
            ct.cur.execute(
                "DELETE FROM book WHERE name=?",
                (delete_val)
            )
        if delete == 2:
            ct.cur.execute(
                "DELETE FROM book WHERE writer=?",
                (delete_val)
            )
        if delete == 3:
            ct.cur.execute(
                "DELETE FROM book WHERE year=?",
                (delete_val)
            )    



class writer():
    def vorodi():
        name = input('Enter the writer name : ')
        book = input('Enter the writer books : ')
        age = input('Enter the writer age : ')
        ct.cur.execute(
            """INSERT INTO writer(name , book , age) VALUES(? , ? , ?)""",
            (name , book , age)
        )
        ct.db.commit()
        ct.db.close()
    def update():
        print('What do you want to update : ')
        print('name --> 1')
        print('book --> 2')
        print('age --> 3')
        update = int(input('Enter the number(1/2/3) : '))
        os.system('cls')
        defualt_val = input('Enter the defualt value : ')    
        update_val = input('Enter the update value : ')    
        if update == 1:
            ct.cur.execute(
                "UPDATE writer SET name=? WHERE name=?",
                (update_val , defualt_val)
            )
        if update == 2:
            ct.cur.execute(
                "UPDATE writer SET book=? WHERE book=?",
                (update_val , defualt_val)
            )        
        if update == 3:
            ct.cur.execute(
                "UPDATE writer SET age=? WHERE age=?",
                (update_val , defualt_val)
            )      
        ct.db.commit()
        ct.db.close()

class member():
    def vorodi():
        name = input('Enter your name : ')
        id_ = input('Enter your id : ')
        number = input('Enter your number : ')
        ct.cur.execute(
            """INSERT INTO member(name , id , number) VALUES(? , ? , ?)""",
            (name , id_ , number)
        )
        ct.db.commit()
        ct.db.close()
    def update():
        print('What do you want to update : ')
        print('name --> 1')
        print('id --> 2')
        print('number --> 3')
        update = int(input('Enter the number(1/2/3) : '))
        os.system('cls')
        defualt_val = input('Enter the defualt value : ')    
        update_val = input('Enter the update value : ')    
        if update == 1:
            ct.cur.execute(
                "UPDATE member SET name=? WHERE name=?",
                (update_val , defualt_val)
            )
        if update == 2:
            ct.cur.execute(
                "UPDATE member SET id=? WHERE id=?",
                (update_val , defualt_val)
            )        
        if update == 3:
            ct.cur.execute(
                "UPDATE member SET number=? WHERE number=?",
                (update_val , defualt_val)
            )      
        ct.db.commit()
        ct.db.close()


