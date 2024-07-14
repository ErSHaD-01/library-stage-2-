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
