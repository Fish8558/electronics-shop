import csv

class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = '���� ���������'

    def __str__(self):
        return self.message