# example.py
import multitasking
import time
import random
import signal

# Kill all tasks on ctrl-c (recommended for development)
signal.signal(signal.SIGINT, multitasking.killall)

# Or, wait for tasks to finish gracefully on ctrl-c:
# signal.signal(signal.SIGINT, multitasking.wait_for_tasks)

@multitasking.task  # <== this is all it takes! 🎉
def hello(count):
    sleep_time = random.randint(1, 10) / 2
    print(f"Hello {count} (sleeping for {sleep_time}s)")
    time.sleep(sleep_time)
    print(f"Goodbye {count} (slept for {sleep_time}s)")

if __name__ == "__main__":
    # Launch 10 concurrent tasks
    for i in range(10):
        hello(i + 1)

    # Wait for all tasks to complete
    multitasking.wait_for_tasks()
    print("All tasks completed!")