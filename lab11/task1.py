import psycopg2
import json

def connect():
    return psycopg2.connect(
        dbname="lab11",
        user="postgres",
        password="_VegasPete", 
        host="localhost",
        port="5432"
    )

# 1. Поиск по шаблону
def search(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    results = cur.fetchall()
    print("\nSearch results:")
    for row in results:
        print(row)
    cur.close()
    conn.close()

# 2. Вставка или обновление пользователя
def insert_or_update(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print(f"Inserted/updated: {name} — {phone}")
    cur.close()
    conn.close()

# 3. Множественная вставка с проверкой
def insert_many(users):
    conn = connect()
    cur = conn.cursor()
    json_data = json.dumps(users)
    cur.execute("CALL insert_many_users(%s)", (json_data,))
    conn.commit()
    print("Batch insert completed (invalid entries printed in NOTICE).")
    cur.close()
    conn.close()

# 4. Пагинация
def get_page(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    print(f"\nPage (limit={limit}, offset={offset}):")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# 5. Удаление по имени или номеру
def delete(identifier):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s)", (identifier,))
    conn.commit()
    print(f"Deleted entries with name or phone: {identifier}")
    cur.close()
    conn.close()


insert_or_update('Bagdar','87878')
insert_or_update('Aruzhan','12345678')
search('Bag')
get_page(1,0)
delete('Bagdar')
