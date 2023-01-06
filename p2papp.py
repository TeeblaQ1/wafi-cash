class User:
    def __init__(self, username, balance=0):
        """Initiate the user class with a balance of zero, 
        also assume that the username is a unique identifier for each user"""
        self.username = username
        self.balance = balance

class P2PApp:
    def __init__(self):
        self.users = {}
    
    def add_user(self, username):
        """Add a new user to the app"""
        if username in self.users:
            raise ValueError(f"User {username} already exists")
        self.users[username] = User(username)
    
    def deposit(self, username, amount):
        """Deposit money into the app for the specified user"""
        if username not in self.users:
            raise ValueError(f"User {username} does not exist")
        self.users[username].balance += amount
    
    def send_money(self, sender, recipient, amount):
        """Send money from the sender to the recipient"""
        if sender not in self.users:
            raise ValueError(f"User {sender} does not exist")
        if recipient not in self.users:
            raise ValueError(f"User {recipient} does not exist")
        if self.users[sender].balance < amount:
            raise ValueError(f"User {sender} does not have enough balance")
        self.users[sender].balance -= amount
        self.users[recipient].balance += amount
    
    def check_balance(self, username):
        """Check the balance of the specified user"""
        if username not in self.users:
            raise ValueError(f"User {username} does not exist")
        return self.users[username].balance
    
    def transfer_out(self, username, amount):
        """Transfer money out of the app for the specified user"""
        if username not in self.users:
            raise ValueError(f"User {username} does not exist")
        if self.users[username].balance < amount:
            raise ValueError(f"User {username} does not have enough balance")
        self.users[username].balance -= amount

