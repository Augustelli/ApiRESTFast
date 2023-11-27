from abc import ABC, abstractmethod


class BaseController(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, item_id : int):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self, item_id : int, data : dict):
        pass

    @abstractmethod
    def delete(self, item_id : int):
        pass