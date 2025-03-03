import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_spending_trends(transactions):
        """# PLOT SPENDING TRENDS BY CATEGORY."""
        spending_by_category = transactions.groupby("Category")["Amount"].sum()
        spending_by_category.plot(kind="bar", color="skyblue")
        plt.title("Spending Trends by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        plt.show()