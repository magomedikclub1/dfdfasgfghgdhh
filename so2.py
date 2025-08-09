import random
import string


def generate_password(length=12, include_symbols=True, include_numbers=True):
    """Генерирует случайный пароль заданной длины"""

    # Базовый набор символов - буквы
    chars = string.ascii_letters

    # Добавляем цифры если нужно
    if include_numbers:
        chars += string.digits

    # Добавляем специальные символы если нужно
    if include_symbols:
        chars += "!@#$%^&*"

    # Генерируем пароль
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def check_password_strength(password):
    """Проверяет силу пароля"""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Добавьте больше символов 11(минимум 8)")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Добавьте заглавные буквы")

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Добавьте цифры")

    strength = ["Очень слабый", "Слабый", "Средний", "Сильный", "Очень сильный"][score]
    return strength, feedback


# Демонстрация работы
print("🔐 Генератор паролей")
print("-" * 30)

for i in range(3):
    password = generate_password(length=random.randint(8, 16))
    strength, tips = check_password_strength(password)
    print(f"Пароль: {password}")
    print(f"Сила: {strength}")
    if tips:
        print(f"Советы: {', '.join(tips)}")
    print()
