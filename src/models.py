from datetime import datetime
import pandas as pd


class Expense:
    """Класс представляет одну запись о расходе."""

    def __init__(self, date_str: str, category: str, amount: float):
        try:
            self.date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Не верный формат даты {date_str}")

        if not isinstance(category, str):
            raise TypeError(f"Категория {category} должна быть строкой")
        self.category = category.strip()

        if not isinstance(amount, (int, float)):
            raise TypeError(f"Сумма {amount} должна быть числом")

        if amount < 0:
            raise ValueError(f"Сумма {amount} должна быть не отрицательной")

        self.amount = float(amount)


class Budget:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    @classmethod
    def from_csv(cls, file_path: str) -> "Budget":
        try:
            df = pd.read_csv(file_path, header=None, names=["date", "category", "amount"])

            df = df.dropna()

            return cls(df)

        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_path} не найден")
        except Expense as e:
            raise ValueError(f"Ошибка {e} при чтиении CSV")

    @property
    def total(self):
        return round(self.df["amount"].sum(), 2)

    @property
    def average(self):
        return round(self.df["amount"].mean(), 2)




if __name__ == '__main__':
    print("Привет из models")
    print("Привет из models1")
    print("Привет из models2")
    pred = Budget.from_csv("../data/sample.csv")
    print(pred.total)
    print(pred.average)