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
        year = input('Enter the published year : ')
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
                (delete_val,)
            )
        if delete == 2:
            ct.cur.execute(
                "DELETE FROM book WHERE writer=?",
                (delete_val,)
            )
        if delete == 3:
            ct.cur.execute(
                "DELETE FROM book WHERE year=?",
                (delete_val,)
            )
        ct.db.commit()
        ct.db.close()        
    def select():
        print('What do you want to view : ')
        print('name --> 1')
        print('writer --> 2')
        print('year --> 3')
        print('all --> 4')
        select = int(input('Enter the number(1/2/3/4) : '))
        os.system('cls')
        if select == 1:
            res = ct.cur.execute(
                """SELECT name FROM book"""
            )
            for i in res:
                print(i)
        if select == 2:
            res = ct.cur.execute(
                """SELECT writer FROM book"""
            )
            for i in res:
                print(i)        
        if select == 3:
            res = ct.cur.execute(
                """SELECT year FROM book"""
            )
            for i in res:
                print(i)
        if select == 4:
            res = ct.cur.execute(
                """SELECT * FROM book"""
            )
            for i in res:
                print(i)        
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
    def delete():
        print('What do you want to delete : ')
        print('name --> 1')
        print('book --> 2')
        print('age --> 3')
        delete = int(input('Enter the number(1/2/3) : '))
        os.system('cls')
        delete_val = input('Enter the delete value : ')
        if delete == 1:
            ct.cur.execute(
                "DELETE FROM writer WHERE name=?",
                (delete_val,)
            )
        if delete == 2:
            ct.cur.execute(
                "DELETE FROM writer WHERE book=?",
                (delete_val,)
            )
        if delete == 3:
            ct.cur.execute(
                "DELETE FROM writer WHERE age=?",
                (delete_val,)
            )
        ct.db.commit()
        ct.db.close()
    def select():
        print('What do you want to view : ')
        print('name --> 1')
        print('book --> 2')
        print('age --> 3')
        print('all --> 4')
        select = int(input('Enter the number(1/2/3/4) : '))
        os.system('cls')
        if select == 1:
            res = ct.cur.execute(
                """SELECT name FROM writer"""
            )
            for i in res:
                print(i)
        if select == 2:
            res = ct.cur.execute(
                """SELECT book FROM writer"""
            )
            for i in res:
                print(i)        
        if select == 3:
            res = ct.cur.execute(
                """SELECT age FROM writer"""
            )
            for i in res:
                print(i)
        if select == 4:
            res = ct.cur.execute(
                """SELECT * FROM writer"""
            )
            for i in res:
                print(i)   
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
    def delete():
        print('What do you want to delete : ')
        print('name --> 1')
        print('id --> 2')
        print('number --> 3')
        delete = int(input('Enter the number(1/2/3) : '))
        os.system('cls')
        delete_val = input('Enter the delete value : ')
        if delete == 1:
            ct.cur.execute(
                "DELETE FROM member WHERE name=?",
                (delete_val,)
            )
        if delete == 2:
            ct.cur.execute(
                "DELETE FROM member WHERE id=?",
                (delete_val,)
            )
        if delete == 3:
            ct.cur.execute(
                "DELETE FROM member WHERE number=?",
                (delete_val,)
            )
        ct.db.commit()
        ct.db.close()
    def select():
        print('What do you want to view : ')
        print('name --> 1')
        print('id --> 2')
        print('number --> 3')
        print('all --> 4')
        select = int(input('Enter the number(1/2/3/4) : '))
        os.system('cls')
        if select == 1:
            res = ct.cur.execute(
                """SELECT name FROM member"""
            )
            for i in res:
                print(i)
        if select == 2:
            res = ct.cur.execute(
                """SELECT id FROM member"""
            )
            for i in res:
                print(i)        
        if select == 3:
            res = ct.cur.execute(
                """SELECT number FROM member"""
            )
            for i in res:
                print(i)
        if select == 4:
            res = ct.cur.execute(
                """SELECT * FROM member"""
            )
            for i in res:
                print(i)

class main():
    def __init__(self):    
        ct()
        print('option --> 1')
        print('action --> 2')
        first_move = int(input('Enter the number(1/2) : '))
        os.system('cls')
        if first_move == 1:
            print('view data --> 1')
            what_request = int(input('Enter the number(1) : '))
            os.system('cls')
            if what_request == 1:
                print('book --> 1' + '\n' + 'writer --> 2' + '\n' + 'member --> 3')
                view = int(input('Enter the number(1/2/3) : '))
                os.system('cls')
                if view == 1:
                    book.select()
                elif view == 2:
                    writer.select()
                elif view == 3:
                    member.select()        
        elif first_move == 2:
            print('add data --> 1')
            print('update data --> 2')
            print('delete data --> 3')
            add_or_update_or_delelet = int(input('Enter the number(1/2) : '))
            os.system('cls')
            if add_or_update_or_delelet == 1:
                print('book --> 1' + '\n' + 'writer --> 2' + '\n' + 'member --> 3')
                add = int(input('Enter the number(1/2/3) : '))
                os.system('cls')
                if add == 1:
                    book.vorodi()
                elif add == 2:
                    writer.vorodi()
                elif add == 3:
                    member.vorodi()
            elif add_or_update_or_delelet == 2:
                print('book --> 1' + '\n' + 'writer --> 2' + '\n' + 'member --> 3')
                update = int(input('Enter the number(1/2/3) : '))
                os.system('cls')
                if update == 1:
                    book.update()
                elif update == 2:
                    writer.update()
                elif update == 3:
                    member.update()        
            elif add_or_update_or_delelet == 3:
                print('book --> 1' + '\n' + 'writer --> 2' + '\n' + 'member --> 3')
                delete = int(input('Enter the number(1/2/3) : '))
                os.system('cls')
                if delete == 1:
                    book.delete()
                elif delete == 2:
                    writer.delete()
                elif delete == 3:
                    member.delete()        

a = main()
a.__init__


