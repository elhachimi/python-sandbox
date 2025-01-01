# /// script
# dependencies = ["watchdog"]
# ///

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
import subprocess


class FilleChangeHandler(PatternMatchingEventHandler):
    def __init__(self, command):
        super().__init__(patterns=["*.py"])
        self.command = command

    def on_modified(self, event):
        subprocess.run(f"{self.command} {event.src_path}", shell=True)
        self.changed_file = event.src_path


if __name__ == "__main__":
    path_to_watch = "./src"
    command_to_run = "python3 "
    event_handler = FilleChangeHandler(command=command_to_run)
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)

    print("Watching for file changes...")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
