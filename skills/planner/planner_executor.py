import sys
import os

# File path Sentinel se pass ho raha hai
task_file = sys.argv[1]  # <- ye Needs_Action/Test_Planner_Task.md

with open(task_file, "r", encoding="utf-8") as f:
    content = f.read()

# Ab process karo jaise pehle
print(f"Processing {task_file}...")
print(content)

# Agar Done folder me move karna hai
DONE_FOLDER = os.path.join(os.path.dirname(task_file), "../Done")
os.makedirs(DONE_FOLDER, exist_ok=True)
done_path = os.path.join(DONE_FOLDER, os.path.basename(task_file))
os.rename(task_file, done_path)
print(f"Moved to Done: {done_path}")