class WorkBenchEnv:
    def __init__(self, task):
        self.task = task
        self.correct_count = 0
        self.total_steps = 0

    def reset(self):
        self.correct_count = 0
        self.total_steps = 0
        return self.task.reset()["observation"]

    def step(self, action):
        observation, correct = self.task.apply_action(action)

        # Track steps
        self.total_steps += 1

        # Reward logic
        if correct:
            self.correct_count += 1
            reward = 0.1
        else:
            reward = -0.05

        done = self.task.is_done()

        info = {"error": None}

        return observation, reward, done, info

    def state(self):
        return {
            "correct": self.correct_count,
            "total": self.total_steps
        }

    # ✅ FINAL SCORE (0 → 1)
    def get_score(self):
        if self.total_steps == 0:
            return 0.0
        return self.correct_count / self.total_steps