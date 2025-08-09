from datetime import datetime, timedelta
import json


class HabitTracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, name):
        """Добавляет новую привычку"""
        if name not in self.habits:
            self.habits[name] = []
            print(f"✅ Привычка '{name}' добавлена!")
        else:
            print(f"❌ Привычка '{name}' уже существует")

    def mark_done(self, habit_name):
        """Отмечает привычку как выполненную сегодня"""
        today = datetime.now().strftime("%Y-%m-%d")

        if habit_name in self.habits:
            if today not in self.habits[habit_name]:
                self.habits[habit_name].append(today)
                print(f"🎉 Привычка '{habit_name}' отмечена на сегодня!")
            else:
                print(f"⚠️ Привычка '{habit_name}' уже отмечена сегодня")
        else:
            print(f"❌ Привычка '{habit_name}' не найдена")

    def get_streak(self, habit_name):
        """Подсчитывает текущую серию выполнения привычки"""
        if habit_name not in self.habits:
            return 0

        dates = sorted(self.habits[habit_name])
        if not dates:
            return 0

        streak = 0
        current_date = datetime.now().date()

        for i in range(len(dates)):
            check_date = datetime.strptime(dates[-(i + 1)], "%Y-%m-%d").date()
            expected_date = current_date - timedelta(days=i)

            if check_date == expected_date:
                streak += 1
            else:
                break

        return streak

    def show_stats(self):
        """Показывает статистику по всем привычкам"""
        print("\n📊 Статистика привычек:")
        print("-" * 40)

        for habit, dates in self.habits.items():
            streak = self.get_streak(habit)
            total_days = len(dates)
            print(f"{habit}:")
            print(f"  🔥 Текущая серия: {streak} дней")
            print(f"  📈 Всего выполнено: {total_days} раз")
            print()


# Демонстрация работы
tracker = HabitTracker()

# Добавляем привычки
tracker.add_habit("Зарядка")
tracker.add_habit("Чтение")
tracker.add_habit("Медитация")

# Отмечаем выполнение
tracker.mark_done("Зарядка")
tracker.mark_done("Чтение")

# Показываем статистику
tracker.show_stats()
