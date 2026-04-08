---
title: WorkBenchRL
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# WorkBenchRL 🚀

## 🧠 Overview
WorkBenchRL is a multi-task reinforcement learning environment designed to simulate real-world workflows such as email triage, data cleaning, and code review.

Unlike traditional RL environments focused on games, this project brings RL into practical, productivity-oriented tasks.

---

## 🚀 Motivation
Most reinforcement learning environments are game-based (Atari, Chess, etc.).

**WorkBenchRL focuses on real-world decision-making tasks**, making it more relevant for:
- AI assistants
- Autonomous workflows
- LLM evaluation systems

---

## 🎯 Tasks

- **Email Classification (Easy)**  
- **Data Cleaning (Medium)**  
- **Code Review (Hard)**  

---

## 🧩 Environment Design

### 🔹 Observation Space

**Email Task**
```json
{"text": "Win a lottery!"}
```

**Data Cleaning Task**
```json
{"Name": "NULL", "Age": "30", "Salary": "??"}
```

**Code Review Task**
```python
"def add(a, b): return a - b"
```

### 🔹 Action Space

**Email Task**
- "spam"
- "important"
- "promo"

**Data Cleaning Task**
```json
{"Name": "Unknown", "Age": "30", "Salary": "0"}
```

**Code Review Task**
```python
def add(a, b): return a + b
```

## 🎁 Reward Function
+0.10 → Correct action
-0.05 → Incorrect action
Final score = correctness ratio (0 to 1)

## ⚙️ How It Works
1. Environment provides observation
2. Agent takes action
3. Reward is assigned
4. Task progresses step-by-step
5. Final score is computed
   
## 📊 Example Output
```md
[START] task=email env=workbench model=simple-agent
[STEP] step=1 action=spam reward=0.10 done=false error=None
[STEP] step=2 action=important reward=0.10 done=false error=None
[STEP] step=3 action=promo reward=0.10 done=true error=None
[END] success=true steps=3 rewards=0.10,0.10,0.10 score=1.00
```

```markdown
## 📊 Baseline Performance

| Task           | Score |
|----------------|------|
| Email          | 1.00 |
| Data Cleaning  | 1.00 |
| Code Review    | 1.00 |
```

👉 Deterministic design ensures reproducible results.

## 🏗️ Project Structure
```
workbenchrl/
│── inference.py
│── openenv.yaml
│── Dockerfile
│── requirements.txt
│── README.md
│
├── env/
│   └── environment.py
│
├── tasks/
│   ├── email_task.py
│   ├── data_task.py
│   └── code_task.py
```

## ⚡ Setup
```bash
pip install -r requirements.txt
```

## ▶️ Run
```bash
python3 inference.py
```

## 🚀 Deployment

This environment is containerized using Docker and deployed on Hugging Face Spaces.

## 🧠 Key Highlights
Multi-task RL environment
Real-world task simulation
Deterministic grading
Step-wise reward shaping
Lightweight and efficient

## 🏁 Conclusion

WorkBenchRL demonstrates how reinforcement learning can move beyond games into real-world applications, providing a foundation for evaluating intelligent agents in practical workflows.