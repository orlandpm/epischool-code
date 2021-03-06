import sqlite3

def query(query_text):
    conn = sqlite3.connect('factbook.db')
    cur = conn.cursor()
    cur.execute(query_text)

    column_names = []
    for column in cur.description:
        column_names.append(column[0])

    rows = cur.fetchall()
    dicts = []

    for row in rows:
        d = dict(zip(column_names, row))
        dicts.append(d)

    conn.close()
    return dicts

def get_all_facts():
    return query("""SELECT * FROM facts""")