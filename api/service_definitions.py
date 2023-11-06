import abc
from enum import Enum

class ReserveService(Enum):
    """
    All services defined by this functions.

    Parameters
    ----------
    Enum : _type_
        _description_
    """
    TOYOKO_INN = 1


class ReservationBase(metaclass=abc.ABCMeta):
    """_summary_

    Parameters
    ----------
    metaclass : _type_, optional
        _description_, by default abc.ABCMeta
    """
    def __init__(self):
        """_summary_
        """
        self._count = 0
        self._message = ''

    @property
    def count(self) -> int:
        """_summary_

        Returns
        -------
        int
            _description_
        """
        return self._count
    
    @property
    def message(self) -> str:
        """_summary_

        Returns
        -------
        str
            _description_
        """
        return self._message

    @abc.abstractclassmethod
    def execute(self) -> bool:
        """_summary_
        """
        pass
