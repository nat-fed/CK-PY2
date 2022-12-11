import doctest


class Car:
    def __init__(self, model: str,  engine_volume: float,  fuil_consumtion: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param model: Модель автомобиля
        :param engine_volume: Объем двигателя в литрах
        :param fuil_consumtion: Расход топлива л на 100 км

        Примеры:
        >>> car = Car("Mitsubishi Pajero Sport", 3, 8)  # инициализация экземпляра класса
        """
        self.model = model

        if not isinstance(engine_volume, (int, float)):
            raise TypeError("Объем двигателя должен быть типа int или float")
        if engine_volume <= 0:
            raise ValueError("Объем двигателя должен быть положительным числом")
        self.engine_volume = engine_volume

        if not isinstance(fuil_consumtion, (int, float)):
            raise TypeError("Расход топлива должно быть типа int или float")
        if fuil_consumtion <= 0:
            raise ValueError("Расход топлива должно быть положительным числом")
        self.fuil_consumtion = fuil_consumtion

    def increase_in_consumption(self, mileage: float) -> None:
        """
        Изменение расхода топлива с увеличение пробега автомобиля

        :param mileage: Пробег автомобиля в км

        Примеры:
        >>> car = Car("Mitsubishi Pajero Sport", 3, 8)
        >>> car.increase_in_consumption(100)
        """
        if not isinstance(mileage, (int, float)):
            raise TypeError("Пробег должен быть типа int или float")
        if mileage <= 0:
            raise ValueError("Пробег должен быть неотрицательным числом")
        ...

    def classification_of_liters(self) -> str:
        """
        Функция которая классифицирует автомобиль по объему двигателя

        :return: Классификация автомобиля по объему двигателя

        Примеры:
        >>> car = Car("Mitsubishi Pajero Sport", 3, 8)
        >>> car.classification_of_liters()
        """
        ...


class Building :
    def __init__(self, floors: int, square: float, purpose: str):
        """
        Создание и подготовка к работе объекта "Здание"

        :param floors: Этажность здания
        :param square: Площадь здания в м2
        :param purpose: Назначение здания

        Примеры:
         >>> building = Building(10, 1200, "Жилое") # инициализация экземпляра класса
        """
        if not isinstance(floors, (int)):
            raise TypeError("Этажность должна быть типа int")
        if floors < 0:
            raise ValueError("Этажность должна быть положительным числом")
        self.floors = floors

        if not isinstance(square, (int, float)):
            raise TypeError("Площадь должна быть типа int или float")
        if square < 0:
            raise ValueError("Площадь должна быть положительным числом")
        self.square = square

        self.purpose = purpose

    def is_high_rise(self, height_one_floor: float) -> bool:
        """
        Функция, которая определяет высоту здания

        :param height_one_floor: Высота этажа

        :return: Является ли здание высотным

        Примеры:
        >>> building = Building(10, 1200, "Жилое")
        >>> building.is_high_rise(2.7)
        """

        if not isinstance(height_one_floor, (int, float)):
            raise TypeError("Высота этажа должна быть типа int или float")
        if height_one_floor < 0:
            raise ValueError("Высота этажа должна быть положительным числом")
        ...

    def building_volume(self, height_one_floor: float) -> float:
        """
        Функция, которая определяет объем здания

        :return: Объем здания

        Примеры:
        >>> building = Building(10, 1200, "Жилое")
        >>> building.building_volume(2.7)
        """

        if not isinstance(height_one_floor, (int, float)):
            raise TypeError("Высота этажа должна быть типа int или float")
        if height_one_floor < 0:
            raise ValueError("Высота этажа должна быть положительным числом")
        ...


class Film:
    def __init__(self, language: str, name: str, year: float, duration: float):
        """
        Создание и подготовка к работе объекта "Фильм"

        :param language: Язык
        :param name: Название фильма
        :param year: Год выпуска фильма
        :param duration: Продолжительность фильма в минутах

        Примеры:
        >>> film = Film("русский", "Маленькие женщины", 2019, 135)  # инициализация экземпляра класса
        """

        self.language = language
        self.name = name

        if not isinstance(year, (int, float)):
            raise TypeError("Год должен быть типа int или float")
        if year < 0:
            raise ValueError("Год должен быть положительным числом")
        self.year = year

        if not isinstance(duration, (int, float)):
            raise TypeError("Продолжиельность должна быть типа int или float")
        if duration < 0:
            raise ValueError("Продолжиельность должна быть положительным числом")
        self.duration = duration

    def start(self) -> None:
        """
        Запуск фильма

        Примеры:
        >>> film = Film("русский", "Маленькие женщины", 2019, 135)
        >>> film.start()
        """
        ...

    def stop(self, moment: float) -> None:
        """
        Пауза фильма в определенный момент времени от начала
        :raise ValueError: Если время паузы превышает длительность фильм, вызываем ошибку.

        Пример:
        >>> film = Film("русский", "Маленькие женщины", 2019, 135)
        >>> film.stop(50)
        """

        if not isinstance(moment, (int, float)):
            raise TypeError("Момент паузы должен быть типа int или float")
        if moment < 0:
            raise ValueError("Момент паузы должен быть положительным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass
