import sqlite3
from .schemas import UserCreate
from passlib.context import CryptContext

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
    
# Function to get a user by username
def get_user_by_username(username: str):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return {
            "id": user[0],
            "username": user[1],
            "role": user[2]
        }
    return None

# Function to get a password by username
def get_password_by_username(username: str):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    password = cursor.fetchone()
    conn.close()

    if password:
        return password[0]
    return None

# Create a password context for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_user(user: UserCreate):
    conn = connect_db()
    cursor = conn.cursor()

    # Hash the password before storing it
    hashed_password = hash_password(user.password)

    # Insert a new user into the users table
    cursor.execute('''INSERT INTO users (username, role, password)
                      VALUES (?, ?, ?)''', (user.username, user.role, hashed_password))
    
    conn.commit()
    conn.close()

    # Return the created user for confirmation
    return {
        "username": user.username,
        "role": user.role
    }

create_tables()
