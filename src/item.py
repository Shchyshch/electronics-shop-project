import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    path = '../src/items.csv'

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

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты класса Item и дочерних от него')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        try:
            cls.all = []
            with open(cls.path, newline='') as csvfile:
                data = csv.DictReader(csvfile)
                for row in data:
                    cls(row['name'], float(row['price']), int(row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except TypeError:
            raise InstantiateCSVError
        except ValueError:
            raise InstantiateCSVError
        except KeyError:
            raise InstantiateCSVError

    @staticmethod
    def string_to_number(str_):
        return int(float(str_))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate


class InstantiateCSVError(Exception):

    def __init__(self):
        self.message = 'Файл item.csv поврежден'

    def __str__(self):
        return self.message
