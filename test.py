import unittest
from p2papp import P2PApp

class TestP2PApp(unittest.TestCase):
    def setUp(self):
        self.app = P2PApp()
    
    def test_add_user(self):
        self.app.add_user("Alice")
        self.assertIn("Alice", self.app.users)
        self.assertEqual(self.app.users["Alice"].username, "Alice")
        self.assertEqual(self.app.users["Alice"].balance, {'USD': 0, 'NGN': 0, 'GBP': 0, 'YUAN': 0})
        self.assertRaises(ValueError, self.app.add_user, "Alice")
    
    def test_deposit(self):
        self.app.add_user("Alice")
        self.app.deposit("Alice", "NGN", 100)
        self.assertEqual(self.app.users["Alice"].balance["NGN"], 100)
        self.assertRaises(ValueError, self.app.deposit, "Alice", "GHC", 100)
        self.assertRaises(ValueError, self.app.deposit, "Bob", "NGN", 100)
    
    def test_send_money(self):
        self.app.add_user("Alice")
        self.app.deposit("Alice", "YUAN", 50)
        self.app.deposit("Alice", "GBP", 50)
        self.app.add_user("Bob")
        self.app.send_money("Alice", "Bob", "GBP", 51)
        self.assertEqual(self.app.users["Alice"].balance["GBP"], 0)
        self.assertEqual(self.app.users["Bob"].balance["GBP"], 51)
        self.assertRaises(ValueError, self.app.send_money, "Alice", "Bob", "YUAN", 2000)
        self.assertRaises(ValueError, self.app.send_money, "Charlie", "Bob", "YUAN", 50)
        self.assertRaises(ValueError, self.app.send_money, "Alice", "Charlie", "YUAN", 50)
    
    def test_check_balance(self):
        self.app.add_user("Alice")
        self.app.deposit("Alice", "USD", 100)
        self.assertEqual(self.app.check_balance("Alice", "USD"), 100)
        self.assertRaises(ValueError, self.app.check_balance, "Bob", "NGN")
    
    def test_transfer_out(self):
        self.app.add_user("Alice")
        self.app.deposit("Alice", "NGN", 100)
        self.app.transfer_out("Alice", "NGN", 40)
        self.assertEqual(self.app.users["Alice"].balance["NGN"], 60)
        self.assertRaises(ValueError, self.app.transfer_out, "Alice", "NGN", 200)
        self.assertRaises(ValueError, self.app.transfer_out, "Bob", "NGN", 50)

if __name__ == "__main__":
    unittest.main()

