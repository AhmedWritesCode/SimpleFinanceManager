import pandas as pd

class Export:
    @staticmethod
    def export_to_excel(transactions, file_name="exported_report.xlsx"):
        """# EXPORT TRANSTACTIONS TO AN EXCEL FILE."""
        transactions.to_excel(file_name, index=False)
        print(f"Transactions exported to {file_name}")