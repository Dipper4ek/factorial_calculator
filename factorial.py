def factorial(n):
    if n < 0:
        return "Факторіал не визначено для від’ємних чисел"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        number = int(input("Введіть ціле число: "))
        print(f"Факторіал числа {number} дорівнює {factorial(number)}")
    except ValueError:
        print("Будь ласка, введіть ціле число.")
