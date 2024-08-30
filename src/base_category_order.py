from abc import ABC, abstractmethod


class BaseCategoryOrder(ABC):
    """ Базовый абстрактный классс """
    @abstractmethod
    def __str__(self):
        pass
