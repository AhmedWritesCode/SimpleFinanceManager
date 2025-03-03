
from modules.ExpenseTracker import ExpenseTracker
from modules.BudgetPlanner import BudgetPlanner
from modules.DataVisualization import Visualization
from modules.Export import Export

def main():
    tracker = ExpenseTracker()
    planner = BudgetPlanner()
    visualizer = Visualization()
    exporter = Export()

    # Example usage
    tracker.log_expense("Food", 50, currency="USD", notes="Dinner with friends")
    tracker.log_expense("Transportation", 20, currency="USD")

    print(tracker.view_transactions())

    planner.set_budget("Food", 100)
    print(planner.check_budget("Food", 50))

    visualizer.plot_spending_trends(tracker.view_transactions())
    exporter.export_to_excel(tracker.view_transactions())

if __name__ == "__main__":
    main()