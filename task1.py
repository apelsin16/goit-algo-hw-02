import queue
import time
import threading

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації заявок
def generate_request():
    while True:
        # Створення нової заявки
        request = "Request ID: " + str(time.time())
        # Додавання заявки до черги
        request_queue.put(request)
        print("New request generated:", request)
        # Затримка перед наступною генерацією заявки
        time.sleep(2)

# Функція для обробки заявок
def process_request():
    while True:
        # Якщо черга не пуста
        if not request_queue.empty():
            # Видалення заявки з черги
            request = request_queue.get()
            print("Processing request:", request)
            # Імітація обробки заявки
            time.sleep(3)
        else:
            print("No requests to process at the moment.")
        # Затримка перед наступною перевіркою черги
        time.sleep(1)

# Запуск окремих потоків для генерації та обробки заявок
generator_thread = threading.Thread(target=generate_request)
processor_thread = threading.Thread(target=process_request)

generator_thread.start()
processor_thread.start()
