class Reminder:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, task, due_date):
        """Add a new reminder."""
        self.reminders.append({"Task": task, "Due Date": due_date})

    def view_reminders(self):
        """View all reminders."""
        if not self.reminders:
            return "No reminders set."
        return "\n".join([f"{r['Task']} (Due: {r['Due Date']})" for r in self.reminders])