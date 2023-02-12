import doctest


class Beam:
    """ Базовый класс балки. """
    def __init__(self, height: int, width: int, material: str):
        """ Инициализация экземпляра класса.

        :param height: Высота сечения балки
        :param width: Ширина сечения балки
        :param material: Материал балки

        Примеры:
        >>> beam = Beam(100, 100, "Бетон")  # инициализация экземпляра класса
        """
        self.material = material

        if not isinstance(height, int):
            raise TypeError("Высота балки должна быть типа int")
        if height < 0:
            raise ValueError("Высота балки должна быть положительным числом")
        self.height = height

        if not isinstance(width, int):
            raise TypeError("Ширина балки должна быть типа int")
        if width < 0:
            raise ValueError("Ширина балки должна быть положительным числом")
        self.width = width

    def __str__(self):
        return f"Балка высотой {self.height} мм, шириной {self.width} мм. Материал: {self.material}."

    def __repr__(self):
        return f"{self.__class__.__name__}(height={self.height!r}, width={self.width!r}, material={self.material!r})"

    def area(self):
        """
        Площадь сечения балки

        Примеры:
        >>> beam = Beam(100, 100, "Бетон")
        >>> beam.area()
        """

        return self.height * self.width


class IBeam(Beam):
    """ Дочерний класс двутавровой балки """
    def __init__(self, height: int, width: int, material: str, thickness_wall: int, thickness_shelf: int):
        """ Инициализация экземпляра класса.

        :param thickness_wall: Толщина стенки
        :param thickness_shelf: Ширина полки

        Примеры:
        >>> ibeam = IBeam(100,200, "Сталь", 2, 2)  # инициализация экземпляра класса
        """

        super().__init__(height, width, material)

        if not isinstance(thickness_wall, int):
            raise TypeError("Толщина стенки балки должна быть типа int")
        if thickness_wall < 0:
            raise ValueError("Толщина стенки балки должна быть положительным числом")
        self.thickness_wall = thickness_wall

        if not isinstance(thickness_shelf, int):
            raise TypeError("Толщина полки балки должна быть типа int")
        if thickness_shelf < 0:
            raise ValueError("Толщина полки балки должна быть положительным числом")
        self.thickness_shelf = thickness_shelf

    def __str__(self):
        return f"Двутавровая балка высотой {self.height} мм, шириной {self.width} мм. Материал: {self.material}. Толщина стенки: {self.thickness_wall} мм. Толщина полки: {self.thickness_shelf} мм."

    def __repr__(self):
        return f"{self.__class__.__name__}(height={self.height!r}, width={self.width!r}, material={self.material!r}, thickness_wall = {self.thickness_wall}, thickness_shelf = {self.thickness_shelf})"

    def area(self):
        """
        Площадь сечения двутавровой балки.
        Метод перегружен, т.к. двутавровая балка имеет сложное сечение.

        Примеры:
        >>> ibeam = IBeam(100,200, "Сталь", 2, 2)
        >>> ibeam.area()
        """

        return (self.height - 2 * self.thickness_shelf) * self.thickness_wall + 2 * self.width * self.thickness_shelf


if __name__ == "__main__":
    doctest.testmod()
    pass
