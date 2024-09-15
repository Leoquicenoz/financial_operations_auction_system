from .database import connect_db

# New user creation function
def create_user(user):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO users (username, role, password) 
                      VALUES (?, ?, ?)''', (user.username, user.role, user.password))

    conn.commit()
    conn.close()

# New operation creation function
def create_operation(operation, operator_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO operations (required_amount, annual_interest, limit_date, operator_id, status)
                      VALUES (?, ?, ?, ?, ?)''', 
                      (operation.required_amount, operation.annual_interest, operation.limit_date, operator_id, True))

    conn.commit()
    conn.close()

# New bid creation function
def create_bid(bid):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO bids (amount, interest_rate, operation_id)
                      VALUES (?, ?, ?)''', 
                      (bid.amount, bid.interest_rate, bid.operation_id))

    conn.commit()
    conn.close()
