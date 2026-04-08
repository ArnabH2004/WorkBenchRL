class DataCleaningTask:
    def __init__(self):
        self.data = [
            {"Name": "John", "Age": "25", "Salary": "50000"},
            {"Name": "NULL", "Age": "30", "Salary": "??"},
            {"Name": "Alice", "Age": "-", "Salary": "70000"},
        ]

        self.cleaned = [
            {"Name": "John", "Age": "25", "Salary": "50000"},
            {"Name": "Unknown", "Age": "30", "Salary": "0"},
            {"Name": "Alice", "Age": "0", "Salary": "70000"},
        ]

        self.index = 0

    def reset(self):
        self.index = 0
        return {"observation": self.data[self.index]}

    def apply_action(self, action):
        correct_row = self.cleaned[self.index]

        is_correct = action == correct_row

        self.index += 1
        done = self.index >= len(self.data)

        next_obs = None if done else self.data[self.index]

        return next_obs, is_correct

    def is_done(self):
        return self.index >= len(self.data)