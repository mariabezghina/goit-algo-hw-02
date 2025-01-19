import queue
import random
import time

# Create a queue of applications
application_queue = queue.Queue()

request_id_counter = 0

def generate_request():
    global request_id_counter
    request_id_counter += 1
    print(f"Generated request: {request_id_counter}")
    application_queue.put(request_id_counter)

def process_request():
    if not application_queue.empty():
        request_id = application_queue.get()
        print(f"Processing request: {request_id}")
        time.sleep(random.uniform(0.5, 1.5))  
        print(f"Request {request_id} processed successfully")
    else:
        print("The queue is empty")

try:
    while True:
        if random.random() < 0.7:
            generate_request()
        
        process_request()
        
        time.sleep(random.uniform(0.5, 2))
except KeyboardInterrupt:
    print("Exiting the application.")
    if not application_queue.empty():
        print(f"Remaining requests in the queue: {list(application_queue.queue)}")
    else:
        print("No remaining requests.")

