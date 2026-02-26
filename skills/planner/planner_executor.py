import os

INBOX = "../Inbox"
PLANS = "../Plans"

# Ensure Plans folder exists
if not os.path.exists(PLANS):
    os.makedirs(PLANS)

for file in os.listdir(INBOX):
    if file.endswith(".md"):
        with open(os.path.join(INBOX, file), 'r', encoding='utf-8') as f:
            content = f.read()
        
        plan_file = os.path.join(PLANS, f"Plan_{file}")
        with open(plan_file, 'w', encoding='utf-8') as f:
            f.write(f"# Plan generated for {file}\n\n")
            f.write("Steps to complete task based on instructions:\n")
            f.write(content[:300] + "...\n")  # Sample summary
        print(f"Plan created: {plan_file}")