class EmailTask:
    def __init__(self):
        self.emails = [
            {"id": 1, "text": "Win a lottery!", "label": "spam"},
            {"id": 2, "text": "Meeting at 5pm", "label": "important"},
            {"id": 3, "text": "50% discount sale", "label": "promo"},
        ]
        self.index = 0

    def reset(self):
        self.index = 0
        return {"observation": self.emails[self.index]}

    def apply_action(self, action):
        correct_label = self.emails[self.index]["label"]
        is_correct = action.lower() == correct_label

        self.index += 1
        done = self.index >= len(self.emails)

        next_obs = None if done else self.emails[self.index]

        return next_obs, is_correct

    def is_done(self):
        return self.index >= len(self.emails)