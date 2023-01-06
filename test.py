import unittest
from p2papp import P2PApp

class TestP2PApp(unittest.TestCase):
    def setUp(self):
        self.app = P2PApp()
    
    def test_add_user(self):
        self.app.add_user("Alice")
        self.assertIn("Alice", self.app.users)
        self.assertEqual(self.app.users["Alice"].username, "Alice")
        self.assertEqual(self.app.users["Alice"].balance, 0)
        self.assertRaises(ValueError, self.app.add_user, "Alice")
    
    def test_deposit(self):
        self.app.add_user("Alice")
        self.app.deposit("Alice", 100)
        self.assertEqual(self.app.users["Alice"].balance, 100)
        self.assertRaises(ValueError, self.app.deposit, "Bob", 100)
    
    def test_send_money(self):
        self.app.add_user("Alice")
        self.app.add_user("Bob")
        self.app.deposit("Alice", 100)
        self.app.send_money("Alice", "Bob", 50)
        self.assertEqual(self.app.users["Alice"].balance, 50)
        self.assertEqual(self.app.users["Bob"].balance, 50)
        self.assertRaises(ValueError, self.app.send_money, "Alice", "Bob", 200)
        self.assertRaises(ValueError, self.app.send_money, "Charlie", "Bob", 50)
        self.assertRaises(ValueError, self.app.send_money, "Alice", "Charlie", 50)
    
    def test_check_balance(self):
        self.app.add_user("Alice")
        self.app.deposit("Alice", 100)
        self.assertEqual(self.app.check_balance("Alice"), 100)
        self.assertRaises(ValueError, self.app.check_balance, "Bob")
    
    def test_transfer_out(self):
        self.app.add_user("Alice")
        self.app.deposit("Alice", 100)
        self.app.transfer_out("Alice", 50)
        self.assertEqual(self.app.users["Alice"].balance, 50)
        self.assertRaises(ValueError, self.app.transfer_out, "Alice", 200)
        self.assertRaises(ValueError, self.app.transfer_out, "Bob", 50)

if __name__ == "__main__":
    unittest.main()

