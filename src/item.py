import csv
import os.path

PATH_TO_CVS_FILE = os.path.join(os.path.dirname(__file__), "items.csv")


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self.__name)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        sum_product = self.price * self.quantity

        return sum_product

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @property
    def name(self):
        if len(self.__name) <= 10:
            return self.__name
        else:
            raise Exception('Длина наименования товара превышает 10 символов')


    @name.setter
    def name(self, data):
        self.__name = data

    @classmethod
    def instantiate_from_csv(cls):
        with open(PATH_TO_CVS_FILE, newline='') as csvfile:
            csv_data = csv.DictReader(csvfile)
            for row in csv_data:
                name, price, quantity = row.values()
                price = cls.string_to_number(price)
                quantity = cls.string_to_number(quantity)
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(num):
        if "." in num:
            return float(num)
        return int(num)
