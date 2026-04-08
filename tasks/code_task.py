class CodeReviewTask:
    def __init__(self):
        self.code_samples = [
            {
                "code": "def add(a, b): return a - b",
                "fix": "def add(a, b): return a + b"
            },
            {
                "code": "def is_even(n): return n % 2 == 1",
                "fix": "def is_even(n): return n % 2 == 0"
            }
        ]

        self.index = 0

    def reset(self):
        self.index = 0
        return {"observation": self.code_samples[self.index]["code"]}

    def apply_action(self, action):
        correct_fix = self.code_samples[self.index]["fix"]

        is_correct = action.strip() == correct_fix

        self.index += 1
        done = self.index >= len(self.code_samples)

        next_obs = None if done else self.code_samples[self.index]["code"]

        return next_obs, is_correct

    def is_done(self):
        return self.index >= len(self.code_samples)