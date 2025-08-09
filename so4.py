from datetime import datetime


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = ["Еда", "Транспорт", "Развлечения", "Покупки", "Другое"]

    def add_expense(self, amount, category, description=""):
        """Добавляет новый расход"""
        if category not in self.categories:
            print(f"❌ Категория '{category}' не найдена")
            print(f"Доступные категории: {', '.join(self.categories)}")
            return

        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        self.expenses.append(expense)
        print(f"✅ Расход {amount}₽ добавлен в категорию '{category}'")

    def get_total_by_category(self):
        """Подсчитывает общие расходы по категориям"""
        totals = {cat: 0 for cat in self.categories}

        for expense in self.expenses:
            totals[expense['category']] += expense['amount']

        return totals

    def show_summary(self):
        """Показывает сводку расходов"""
        if not self.expenses:
            print("📊 Расходов пока нет")
            return

        total = sum(exp['amount'] for exp in self.expenses)
        category_totals = self.get_total_by_category()

        print("\n💰 Сводка расходов:")
        print("-" * 30)
        print(f"Общие расходы: {total}₽")
        print("\nПо категориям:")

        for category, amount in category_totals.items():
            if amount > 0:
                percentage = (amount / total) * 100
                print(f"  {category}: {amount}₽ ({percentage:.1f}%)")

        print(f"\nВсего записей: {len(self.expenses)}")


# Демонстрация работы
tracker = ExpenseTracker()

# Добавляем расходы
tracker.add_expense(500, "Еда", "Обед в кафе")
tracker.add_expense(200, "Транспорт", "Метро")
tracker.add_expense(1500, "Покупки", "Новая футболка")
tracker.add_expense(800, "Развлечения", "Кино")

# Показываем сводку
tracker.show_summary()
