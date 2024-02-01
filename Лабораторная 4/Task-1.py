if __name__ == "__main__":
    class Животное:
        """Базовый класс, представляющий животных."""

        def __init__(self, вид: str, звук: str):
            self._вид = вид  # Вид животного
            self._звук = звук  # Звук, издаваемый животным

        def сделать_звук(self) -> str:
            """
            Издать характерный звук животного.

            Returns:
            str: Звук, издаваемый животным.
            """
            return self._звук

        def получить_вид(self) -> str:
            """
            Получить вид животного.

            Returns:
            str: Вид животного.
            """
            return self._вид

        def __str__(self) -> str:
            return f"Животное {self._вид}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}({self._вид}, {self._звук})"


    class Собака(Животное):
        """Производный класс, представляющий собак."""

        def __init__(self, вид: str, звук: str, порода: str):
            super().__init__(вид, звук)
            self._порода = порода  # Порода собаки

        def сделать_звук(self) -> str:
            """
            Издать характерный звук собаки.

            Returns:
            str: Звук, издаваемый собакой.
            """
            return "Гав! Гав!"

        def __str__(self) -> str:
            return f"Собака породы {self._порода} {self._вид}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}({self._вид}, {self._звук}, {self._порода})"


    class Кошка(Животное):
        """Производный класс, представляющий кошек."""

        def __init__(self, вид: str, звук: str, окрас: str):
            super().__init__(вид, звук)
            self._окрас = окрас  # Окрас кошки

        def получить_окрас(self) -> str:
            """
            Получить окрас кошки.

            Returns:
            str: Окрас кошки.
            """
            return self._окрас

        def сделать_звук(self) -> str:
            """
            Издать характерный звук кошки.

            Returns:
            str: Звук, издаваемый кошкой.
            """
            return "Мяу!"

        def __str__(self) -> str:
            return f"Кошка окраса {self._окрас} {self._вид}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}({self._вид}, {self._звук}, {self._окрас})"
    pass
