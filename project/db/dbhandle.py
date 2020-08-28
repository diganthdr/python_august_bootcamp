import sqlite3

DB_NAME = 'covid_02.db'
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

#one time activity after DB is created.
#SQLite natively supports only the types TEXT, INTEGER, REAL, BLOB and NULL
try:
    cmd_create_table_state_cases = '''CREATE TABLE state_cases(day TEXT ,state_name TEXT,active_cases INTEGER)'''
    c.execute(cmd_create_table_state_cases)
    conn.commit()
except sqlite3.OperationalError as oe:
    print("Table \'state_cases\' exists. Continuing with rest of the code...")

try:
    cmd_create_table_news = "CREATE TABLE news(day TEXT , url TEXT unique, headlines TEXT)"
    c.execute(cmd_create_table_news)
    conn.commit()
except sqlite3.OperationalError as oe:
    print("Table \'news\' exists. Continuing with rest of the code...")


#Every run/day activity
#cmd_insert_row = '''INSERT INTO state_cases VALUES ('2020-08-25','Karnataka', 3445)'''
#cmd_insert_row = '''INSERT INTO state_cases VALUES ('2020-08-26','Karnataka', 3436)'''
#c.execute(cmd_insert_row)
#cmd_insert_row = '''INSERT INTO news VALUES('2020-08-26','test.com', "test headline")'''
#c.execute(cmd_insert_row)


def insert_row(table_name, row_content):
    '''
    Table name, input.
    row_content is tuple.

    form command from incoming row_content
    '''
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    cmd_insert_row = '''INSERT INTO %s VALUES %s''' %(table_name, row_content)
    try:
        c.execute(cmd_insert_row)
        conn.commit()
    except sqlite3.IntegrityError as ie:
        print("Unique constraint, (with date) clashes. Skipping", str(ie))

    conn.close()


def get_rows(table_name, this_date,number_of_rows=0):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    #cmd_select_all_state_cases = "SELECT * FROM %s " %(table_name)
    cmd_select_all_state_cases = "SELECT * FROM %s WHERE day = \'%s\'" %(table_name, this_date)
    print()
    rows = c.execute(cmd_select_all_state_cases)
    print("Rows from: ", table_name)
    for row in rows:
        print(row) 

def get_statewise_data_for_graph(table_name, this_date,number_of_rows=0):
    '''
    output, x and y axis data in list return (x,y)
    '''
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    x_axis_list = []
    y_axis_list = []
    #cmd_select_all_state_cases = "SELECT * FROM %s " %(table_name)
    cmd_select_all_state_cases = "SELECT * FROM %s WHERE day = \'%s\'" %(table_name, this_date)
    print()
    rows = c.execute(cmd_select_all_state_cases)
    print("Rows from state_cases")
    for row in rows:
        print(row) 
        x_axis_list.append(row[1])
        y_axis_list.append(row[2])
    
    print(x_axis_list, y_axis_list)
    return x_axis_list, y_axis_list


#cmd_select_all_news = "SELECT * FROM news"
#rows = c.execute(cmd_select_all_news)
#print("Rows from news")
#for row in rows:
#    print(row) 

#cmd_insert_row = '''INSERT INTO news VALUES('2020-08-26','test.com', "test headline")'''
#insert_row('news', ('2020-08-25','test.com', "test headline"))
#insert_row('news', ('2020-08-28','test2.com', "test headline"))
#insert_row('news', ('2020-08-29','test2.com', "test headline"))
#get_rows('news')
#get_rows('news', "2020-08-26", number_of_rows=0)
#get_statewise_data_for_graph('state_cases', "2020-08-27")