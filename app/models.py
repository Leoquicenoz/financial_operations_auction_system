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
def create_bid(bid, user_id: int):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO bids (amount, interest_rate, operation_id, user_id)
                      VALUES (?, ?, ?, ?)''', 
                      (bid.amount, bid.interest_rate, bid.operation_id, user_id))
    conn.commit()
    conn.close()

    return {
        "amount": bid.amount,
        "interest_rate": bid.interest_rate,
        "operation_id": bid.operation_id,
        "user_id": user_id
    }

# Get operation by ID
def get_operation_by_id(operation_id: int):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM operations WHERE id = ?", (operation_id,))
    operation = cursor.fetchone()
    conn.close()
    
    if operation:
        return {
            "id": operation[0],
            "required_amount": operation[1],
            "annual_interest": operation[2],
            "limit_date": operation[3],
            "operator_id": operation[4],
            "status": operation[5]
        }
    return None

# Get active operations
def get_active_operations():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''SELECT id, required_amount, annual_interest, limit_date, operator_id 
                      FROM operations WHERE status = 1''')
    
    operations = cursor.fetchall()
    conn.close()
    return operations

# Get bids by operation ID
def get_bids_by_operation_id(operation_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''SELECT id, amount, interest_rate, user_id
                      FROM bids WHERE operation_id = ?''', (operation_id,))
    
    bids = cursor.fetchall()
    conn.close()
    return bids
