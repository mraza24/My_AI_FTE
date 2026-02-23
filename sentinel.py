import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class TaskHandler(FileSystemEventHandler):
    def process_task(self, event):
        if not event.is_directory and event.src_path.endswith('.md'):
            print(f"✨ Activity detected: {event.src_path}")
            # Claude ko autonomously chalanay ki command
            subprocess.run(["claude", "-p", "Check the Needs_Action folder, process the task, and move it to Done."], shell=True)

    def on_created(self, event):
        self.process_task(event)

    def on_modified(self, event):
        self.process_task(event)

if __name__ == "__main__":
    path = "./Needs_Action" 
    event_handler = TaskHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print("👀 Sentinel Active hai... Tasks ka intezar hai.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()