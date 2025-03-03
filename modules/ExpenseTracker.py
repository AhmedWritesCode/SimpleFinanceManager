import pandas as pd
from datetime import datetime

class ExpenseTracker:

  def __init__(self, file_path = "data/transaction.csv"):
    self.file_path = file_path
    try:
      self.transactions = pd.read_csv(file_path)
    except FileNotFoundError:
      self.transactions = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])
      self.transactions.to_csv(file_path, index=False)

  def log_expense(self, category, amount, currency="$", notes =""):
    """# LOG A NEW EXPENSE."""
    new_entry = {

            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Category": category,
            "Amount": amount,
            "Currency": currency,
            "Notes": notes

    }
        
    self.transactions = pd.concat([self.transactions, pd.DataFrame([new_entry])], ignore_index=True)
    self.save_transactions()

  def save_transactions(self):
      """# SAVE TRANSACTIONS TO A CSV FILE."""
      self.transactions.to_csv(self.file_path, index=False)

  def view_transactions(self):
      """# VIEW ALL LOGGED TRANSACTIONS."""
      return self.transactions