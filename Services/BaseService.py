from abc import ABC, abstractmethod


class BaseService(ABC):

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id : int):
        pass

    @abstractmethod
    def save(self, modelInstance):
        pass

    @abstractmethod
    def update(self, modelInstance):
        pass

    @abstractmethod
    def delete(self, modelInstance):
        pass

