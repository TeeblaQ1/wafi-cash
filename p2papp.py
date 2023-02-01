class User:
    def __init__(self, username, balance):
        """Initiate the user class with a balance of zero, 
        also assume that the username is a unique identifier for each user"""
        self.username = username
        self.balance = balance

def convert_currency(amount, source_curr, dest_curr):
    MARKET_RATES = { "USD": 1, "NGN": 415, "GBP": 0.86, "YUAN" : 6.89}
    return (amount/MARKET_RATES[source_curr]) * MARKET_RATES[dest_curr]
class P2PApp:
    '''
    Market rates = { "USD": 1, "NGN": 415, GBP: 0.86, "YUAN" : 6.89}
    '''
    
    def __init__(self):
        self.users = {}
        self.MARKET_RATES = { "USD": 1, "NGN": 415, "GBP": 0.86, "YUAN" : 6.89}
    
    

    def add_user(self, username):
        """Add a new user to the app"""
        if username in self.users:
            raise ValueError(f"User {username} already exists")
        self.users[username] = User(username, balance={"USD": 0, "NGN": 0, "GBP": 0, "YUAN": 0})
    
    def deposit(self, username, currency, amount):
        """Deposit money into the app for the specified user specifying the currency"""
        if username not in self.users:
            raise ValueError(f"User {username} does not exist")
        if currency not in self.MARKET_RATES.keys():
            raise ValueError(f'We currently do not have the currency "{currency}"')
        self.users[username].balance[currency] += amount
    
    def send_money(self, sender, recipient, currency, amount):
        """Send money from the sender to the recipient"""
        if sender not in self.users:
            raise ValueError(f"User {sender} does not exist")
        if recipient not in self.users:
            raise ValueError(f"User {recipient} does not exist")
        if currency not in self.MARKET_RATES.keys():
            raise ValueError(f'We currently do not have the currency "{currency}"')
        # Here => Todo: check for insufficient value of that currency and supplement with other currencies
        # Check if the total balance is more than the amount to send after conversion
        currency_value = 0
        for key, value in  self.users[sender].balance.items():
            currency_value += convert_currency(value, key, currency)
        if currency_value < amount:
            raise ValueError(f"User {sender} does not have enough balance")
        if self.users[sender].balance[currency] >= amount:
            self.users[sender].balance[currency] -= amount
            self.users[recipient].balance[currency] += amount
        else:
            surplus = amount - self.users[sender].balance[currency]
            self.users[sender].balance[currency] = 0
            # loop through each currency, then convert it to the send_money_currency, ignoring the send_money_currency
            for current_currency in self.users[sender].balance.keys():
                if current_currency == currency:
                    continue
                balance_in_currency = convert_currency(self.check_balance(sender, current_currency), current_currency, currency)
                if balance_in_currency >= surplus:
                    self.users[sender].balance[current_currency] -= convert_currency(surplus, currency, current_currency)
                    self.users[sender].balance[currency] = 0
                    surplus = 0
                    break
                surplus -= convert_currency(self.users[sender].balance[current_currency], current_currency, currency)
                self.users[sender].balance[current_currency] = 0
            self.users[recipient].balance[currency] += amount
                    
    
    def check_balance(self, username, currency):
        """Check the balance of the specified user"""
        if username not in self.users:
            raise ValueError(f"User {username} does not exist")
        return self.users[username].balance[currency]
    
    def transfer_out(self, username, currency, amount):
        """Transfer money out of the app for the specified user"""
        if username not in self.users:
            raise ValueError(f"User {username} does not exist")
        if currency not in self.MARKET_RATES.keys():
            raise ValueError(f'We currently do not have the currency "{currency}"')
        
        # self.users[username].balance -= amount
        currency_value = 0
        for key, value in  self.users[username].balance.items():
            currency_value += convert_currency(value, key, currency)
        if currency_value < amount:
            raise ValueError(f"User {username} does not have enough balance")
        if self.users[username].balance[currency] >= amount:
            self.users[username].balance[currency] -= amount
        else:
            surplus = amount - self.users[username].balance[currency]
            self.users[username].balance[currency] = 0
            # loop through each currency, then convert it to the send_money_currency, ignoring the send_money_currency
            for current_currency in self.users[username].balance.keys():
                if current_currency == currency:
                    continue
                balance_in_currency = convert_currency(self.check_balance(username, current_currency), current_currency, currency)
                if balance_in_currency >= surplus:
                    self.users[username].balance[current_currency] -= convert_currency(surplus, currency, current_currency)
                    self.users[username].balance[currency] = 0
                    surplus = 0
                    break
                surplus -= convert_currency(self.users[username].balance[current_currency], current_currency, currency)
                self.users[username].balance[current_currency] = 0

