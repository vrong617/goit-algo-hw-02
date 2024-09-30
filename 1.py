import queue
import random
import time

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request(request_id):
    print(f"Generating request #{request_id}")
    request_queue.put(request_id)

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Processing request #{request_id}")
    else:
        print("No requests to process. The queue is empty.")

# Головний цикл програми
def main():
    request_id = 1
    while True:
        action = input("Press 'g' to generate a request, 'p' to process a request, or 'q' to quit: ")
        if action == 'g':
            generate_request(request_id)
            request_id += 1
        elif action == 'p':
            process_request()
        elif action == 'q':
            print("Exiting program...")
            break
        else:
            print("Invalid input. Please press 'g', 'p', or 'q'.")

if __name__ == "__main__":
    main()
