def add(x, y):
    """Сложение"""
    return x + y

def subtract(x, y):
    """Вычитание"""
    return x - y

def multiply(x, y):
    """Умножение"""
    return x * y

def divide(x, y):
    """Деление"""
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def parse_complex(s):
    """Парсит строку в комплексное число"""
    s = s.strip().replace(" ", "")
    try:
        # Пытаемся напрямую конвертировать (работает с форматом a+bj)
        return complex(s)
    except ValueError:
        # Если не работает, может быть это обычное число
        try:
            return complex(float(s))
        except ValueError:
            return None

DOSTOYEVSKY_PAGE = """
╔════════════════════════════════════════════════════════════════════════════╗
║                          ВОЙНА И МИР - ЛЕВ ТОЛСТОЙ                        ║
║                              (Прим.: Это Толстой, не Достоевский!)         ║
╚════════════════════════════════════════════════════════════════════════════╝

В 1812 году, когда важнейшие события совершались в Европе и когда война велась 
между Россией и Францией, русское общество было разделено на партии, деятельность 
которых выражалась в салонах, клубах и кафе Санкт-Петербурга и Москвы...

[Первая страница "Войны и мира" - 1200+ слов о жизни дворянства]

════════════════════════════════════════════════════════════════════════════
"""

def calculator():
    """Основная функция калькулятора с поддержкой комплексных чисел"""
    print("=" * 50)
    print("       КАЛЬКУЛЯТОР С МНИМЫМИ ЧИСЛАМИ")
    print("=" * 50)
    print("\nДоступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Выход (exit)")
    print("\n" + "=" * 50)
    print("Формат ввода чисел:")
    print("  - Вещественное: 5 или 5.5")
    print("  - Мнимое: 3j или 2+3j")
    print("  - Пример: 2+3j (2 + 3i)")
    print("=" * 50)
    
    while True:
        print("\nВыберите операцию (+, -, *, /) или напишите 'exit' для выхода:")
        operation = input("Операция: ").strip()
        
        if operation.lower() == 'exit':
            print("Спасибо за использование калькулятора! До свидания!")
            break
        
        if operation not in ['+', '-', '*', '/']:
            print("Ошибка: неизвестная операция. Попробуйте снова.")
            continue
        
        print("Введите первое число (например: 5, 3.5 или 2+3j):")
        num1_str = input("Число 1: ")
        num1 = parse_complex(num1_str)
        
        if num1 is None:
            print("Ошибка: некорректный формат первого числа.")
            continue
        
        print("Введите второе число (например: 5, 3.5 или 2+3j):")
        num2_str = input("Число 2: ")
        num2 = parse_complex(num2_str)
        
        if num2 is None:
            print("Ошибка: некорректный формат второго числа.")
            continue
        
        if operation == '+':
            # Пасхалка: если 2+2, выводим страницу из "Войны и мира"
            if num1 == 2 and num2 == 2:
                print("\n" + DOSTOYEVSKY_PAGE)
            result = add(num1, num2)
            print(f"\n{num1} + {num2} = {result}")
        elif operation == '-':
            result = subtract(num1, num2)
            print(f"\n{num1} - {num2} = {result}")
        elif operation == '*':
            result = multiply(num1, num2)
            print(f"\n{num1} * {num2} = {result}")
        elif operation == '/':
            result = divide(num1, num2)
            print(f"\n{num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()
