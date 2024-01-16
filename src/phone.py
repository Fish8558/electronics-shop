from src.item import Item


class Phone(Item):
    """
    ����� ����������� �� Item, ���������� ��������
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __perp__(self):
        return f"{self.__class__.__name__}, ('{self.name}'), {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        ������ ���������� ���-����
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if number <= 0:
            print('ValueError: ���������� ���������� SIM-���� ���������� ����� � ������ ����.')
        else:
            self.__number_of_sim = number
