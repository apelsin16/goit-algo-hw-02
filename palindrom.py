from collections import deque

def is_palindrome(input_string):
    # Видалення пробілів та переведення рядка в нижній регістр
    processed_string = input_string.replace(" ", "").lower()
    # Створення двосторонньої черги
    char_deque = deque(processed_string)

    # Перевірка, чи є рядок паліндромом
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклад використання функції
input_string = "Анна"
print("Is the input string a palindrome?", is_palindrome(input_string))
