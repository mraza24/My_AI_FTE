import time
import subprocess
import os
import hashlib
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ── CONFIG ─────────────────────────────────────────
INBOX_PATH = "./Inbox"
NEEDS_ACTION_PATH = "./Needs_Action"
DONE_PATH = "./Done"
LOGS_PATH = "./Logs"
DASHBOARD_FILE = "./Dashboard.md"
REPORTER_SKILL = "./skills/reporter/SKILL.md"

CLAUDE_CMD_PATH = r"C:\Users\hp\AppData\Roaming\npm\claude.cmd"

processed_files = set()

# ── UTILITIES ─────────────────────────────────────

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def log_action(filename, action, status="Success"):

    if not os.path.exists(LOGS_PATH):
        os.makedirs(LOGS_PATH)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(LOGS_PATH, f"{timestamp}.md")

    with open(log_file, "w", encoding="utf-8") as f:
        f.write(
            f"# Log Entry\n\n"
            f"File: {filename}\n"
            f"Timestamp: {timestamp}\n"
            f"Action: {action}\n"
            f"Status: {status}\n"
        )


def update_dashboard():

    total = len(os.listdir(NEEDS_ACTION_PATH)) + len(os.listdir(DONE_PATH))
    completed = len(os.listdir(DONE_PATH))
    pending = len(os.listdir(NEEDS_ACTION_PATH))

    content = (
        f"# Dashboard\n\n"
        f"Total Tasks: {total}\n"
        f"Completed: {completed}\n"
        f"Pending: {pending}\n"
    )

    with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
        f.write(content)


# ── FILE HANDLER ─────────────────────────────────

class TaskHandler(FileSystemEventHandler):

    def process_task(self, filepath):

        if not filepath.endswith(".md"):
            return

        if not os.path.exists(filepath):
            return

        filehash = file_hash(filepath)

        if filehash in processed_files:
            return

        processed_files.add(filehash)

        filename = os.path.basename(filepath)
        folder = os.path.dirname(filepath)

        print(f"\n✨ Detected task: {filename}")

        # Inbox → Needs_Action
        if folder.endswith("Inbox"):

            new_path = os.path.join(NEEDS_ACTION_PATH, filename)

            try:
                shutil.move(filepath, new_path)
                filepath = new_path
                print(f"📥 Moved to Needs_Action: {filename}")

            except Exception as e:
                print(f"Move failed: {e}")
                return

        # Planner task
        if "planner" in filename.lower():

            print("🧠 Triggering Planner Executor...")

            try:
                subprocess.run(
                    ["python", "skills/planner/planner_executor.py", filepath],
                    check=True
                )

                log_action(filename, "Planner executed")

            except Exception as e:

                log_action(filename, "Planner failed", str(e))

        # Reporter task
        else:

            print("🤖 Triggering Claude Reporter...")

            try:

                result = subprocess.run(
                    [
                        CLAUDE_CMD_PATH,
                        "--dangerously-skip-permissions",
                        "-p",
                        f"Read {REPORTER_SKILL} and process {filepath}. "
                        f"Save output to {DONE_PATH}/{filename}."
                    ],
                    shell=True
                )

                status = "Success" if result.returncode == 0 else "Failed"

            except Exception as e:

                status = f"Failed ({e})"

            log_action(filename, "Reporter executed", status)
            update_dashboard()

            print(f"✅ Task processed: {filename} | Status: {status}")


    def on_created(self, event):

        if not event.is_directory:
            time.sleep(1)
            self.process_task(event.src_path)


    def on_modified(self, event):

        return


# ── MAIN ─────────────────────────────────────────

if __name__ == "__main__":

    for folder in [INBOX_PATH, NEEDS_ACTION_PATH, DONE_PATH, LOGS_PATH]:

        if not os.path.exists(folder):
            os.makedirs(folder)

    event_handler = TaskHandler()

    observer = Observer()

    observer.schedule(event_handler, INBOX_PATH, recursive=False)
    observer.schedule(event_handler, NEEDS_ACTION_PATH, recursive=False)

    observer.start()

    print("👀 Sentinel Active. Monitoring Needs_Action/ and Inbox/")
    print("📭 Waiting for NEW tasks...")

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()