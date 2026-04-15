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

def calculator():
    """Основная функция калькулятора"""
    print("=" * 40)
    print("         КАЛЬКУЛЯТОР")
    print("=" * 40)
    print("\nДоступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Выход (exit)")
    print("=" * 40)
    
    while True:
        print("\nВыберите операцию (+, -, *, /) или напишите 'exit' для выхода:")
        operation = input("Операция: ").strip()
        
        if operation.lower() == 'exit':
            print("Спасибо за использование калькулятора! До свидания!")
            break
        
        if operation not in ['+', '-', '*', '/']:
            print("Ошибка: неизвестная операция. Попробуйте снова.")
            continue
        
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите корректные числа.")
            continue
        
        if operation == '+':
            print(f"\n{num1} + {num2} = {add(num1, num2)}")
        elif operation == '-':
            print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '*':
            print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '/':
            result = divide(num1, num2)
            print(f"\n{num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()
