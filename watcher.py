import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "receipts"

class ReceiptHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        filename = os.path.basename(event.src_path)
        print(f" New file detected: {filename} ")

if __name__ == "__main__":
    event_handler = ReceiptHandler()

    # Starts background thread
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)

    # Launches separate thread
    observer.start()

    print(f"Watching folder: {WATCH_FOLDER}")

    try:
        # Main thread loop until interrupt
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
