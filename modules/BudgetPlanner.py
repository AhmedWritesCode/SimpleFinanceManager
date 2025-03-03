class BudgetPlanner:
    def __init__(self):
        self.budgets = {}  # Dictionary to store budgets {category: limit}

    def set_budget(self, category, limit):
        """Set a budget for a specific category."""
        self.budgets[category] = limit

    def check_budget(self, category, spent):
        """Check if the user is nearing or exceeding their budget."""
        if category in self.budgets:
            limit = self.budgets[category]
            if spent >= limit:
                return f"Budget exceeded for {category}!"
            elif spent >= 0.8 * limit:
                return f"Warning: You're nearing your budget for {category}."
            else:
                return f"You're within your budget for {category}."
        return f"No budget set for {category}."