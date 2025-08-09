import re
from collections import Counter


def analyze_text(text):
    """Анализирует текст и возвращает статистику по словам"""

    # Приводим к нижнему регистру и убираем знаки препинания
    clean_text = re.sub(r'[^\w\s]', '', text.lower())

    # Разбиваем на слова
    words = clean_text.split()

    # Подсчитываем статистику
    word_count = len(words)
    unique_words = len(set(words))
    most_common = Counter(words).most_common(5)

    # Средняя длина слова
    avg_length = sum(len(word) for word in words) / len(words) if words else 0

    return {
        'total_words': word_count,
        'unique_words': unique_words,
        'most_common': most_common,
        'average_word_length': round(avg_length, 2)
    }


def print_analysis(stats):
    """Красиво выводит статистику"""
    print("📊 Анализ текста:")
    print(f"Всего слов: {stats['total_words']}")
    print(f"Уникальных слов: {stats['unique_words']}")
    print(f"Средняя длина слова: {stats['average_word_length']} символов")
    print("\n🔥 Топ-5 самых частых слов:")

    for word, count in stats['most_common']:
        print(f"  '{word}': {count} раз")


# Пример использования
sample_text = """
Python - это мощный язык программирования. Python используется для веб-разработки,
анализа данных, машинного обучения и многого другого. Изучение Python открывает
множество возможностей для разработчиков.
"""

if __name__ == "__main__":
    stats = analyze_text(sample_text)
    print_analysis(stats)

    print("\n" + "=" * 50)
    print("Попробуйте ввести свой текст для анализа!")
