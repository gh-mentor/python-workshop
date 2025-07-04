from queue import Queue
import threading
import time

class Consumer:
    def __init__(self, shared_queue):
        self.shared_queue = shared_queue

    def consume(self):
        while True:
            item = self.shared_queue.get()
            if item is None:  # Check for termination signal
                break
            print(f"Consumed: {item}")
            self.shared_queue.task_done()
            time.sleep(1)  # Simulate processing time
