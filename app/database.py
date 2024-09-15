import sqlite3

# SQLite database connection function
def connect_db():
    conn = sqlite3.connect('auction_system.db')  
    return conn

# Function for creating the required tables
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Create user table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        role TEXT NOT NULL,
                        password TEXT NOT NULL
                      )''')

    # Create operations table
    cursor.execute('''CREATE TABLE IF NOT EXISTS operations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        required_amount REAL NOT NULL,
                        annual_interest REAL NOT NULL,
                        limit_date TEXT NOT NULL,
                        operator_id INTEGER NOT NULL,
                        status BOOLEAN NOT NULL
                      )''')

    # Create bids table
    cursor.execute('''CREATE TABLE IF NOT EXISTS bids (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount REAL NOT NULL,
                        interest_rate REAL NOT NULL,
                        operation_id INTEGER NOT NULL,
                        FOREIGN KEY (operation_id) REFERENCES operations (id)
                      )''')

    conn.commit()
    conn.close()

create_tables()
