from abc import ABC, abstractmethod


class DatabaseReader(ABC):

    @abstractmethod
    def insert_row(self):
        pass

    @abstractmethod
    def delete_row(self, condition):
        pass
