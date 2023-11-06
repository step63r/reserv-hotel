import datetime

class Hotel:
    """_summary_
    """
    def __init__(self, hotel_id: str, pref_code: int, hotel_name: str):
        """_summary_

        Parameters
        ----------
        hotel_id : str
            _description_
        pref_code : int
            _description_
        hotel_name : str
            _description_
        """
        self._hotel_id = hotel_id
        self._pref_code = pref_code
        self._hotel_name = hotel_name

    @property
    def hotel_id(self) -> str:
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        return self._hotel_id
    
    @property
    def pref_code(self) -> int:
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        return self._pref_code
    
    @property
    def hotel_name(self) -> str:
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        return self._hotel_name

class RoomType:
    """_summary_
    """
    def __init__(self, room_type_id: int, room_type_name: str):
        """_summary_

        Parameters
        ----------
        room_type_id : _type_
            _description_
        room_type_name : _type_
            _description_
        """
        self._room_type_id = room_type_id
        self._room_type_name = room_type_name
    
    @property
    def room_type_id(self) -> int:
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        return self._room_type_id
    
    @property
    def room_type_name(self) -> str:
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        return self._room_type_name

class CheckinTime:
    """_summary_
    """
    def __init__(self, checkin_value: str, checkin_name: str):
        """_summary_

        Parameters
        ----------
        checkin_value : str
            _description_
        checkin_name : str
            _description_
        """
        self._checkin_value = checkin_value
        self._checkin_name = checkin_name
    
    @property
    def checkin_value(self) -> str:
        """_summary_

        Returns
        -------
        str
            _description_
        """
        return self._checkin_value
    
    @property
    def checkin_name(self) -> str:
        """_summary_

        Returns
        -------
        str
            _description_
        """
        return self._checkin_name

class LoginInfo:
    """_summary_
    """
    def __init__(self, login_address: str, login_pass: str, login_tel: str):
        """_summary_

        Parameters
        ----------
        login_address : str
            _description_
        login_pass : str
            _description_
        login_tel : str
            _description_
        """
        self._login_address = login_address
        self._login_pass = login_pass
        self._login_tel = login_tel
    
    @property
    def login_address(self) -> str:
        """_summary_

        Returns
        -------
        str
            _description_
        """
        return self._login_address
    
    @property
    def login_pass(self) -> str:
        """_summary_

        Returns
        -------
        str
            _description_
        """
        return self._login_pass
    
    @property
    def login_tel(self) -> str:
        """_summary_

        Returns
        -------
        str
            _description_
        """
        return self._login_tel


class ProcessFormat:
    """_summary_
    """
    def __init__(
            self,
            hotel: Hotel,
            checkin_date: datetime.date,
            type: RoomType,
            strict_room_type: bool,
            enable_no_smoking: bool,
            enable_smoking: bool,
            smoking_first: bool,
            checkin_value: CheckinTime,
            enable_auto_retry: bool,
            enable_overwrite: bool):
        """_summary_

        Parameters
        ----------
        hotel : Hotel
            _description_
        checkin_date : datetime.date
            _description_
        type : RoomType
            _description_
        strict_room_type : bool
            _description_
        enable_no_smoking : bool
            _description_
        enable_smoking : bool
            _description_
        smoking_first : bool
            _description_
        checkin_value : CheckinTime
            _description_
        enable_auto_retry : bool
            _description_
        enable_overwrite : bool
            _description_
        """
        self._hotel = hotel
        self._checkin_date = checkin_date
        self._type = type
        self._strict_room_type = strict_room_type
        self._enable_no_smoking = enable_no_smoking
        self._enable_smoking = enable_smoking
        self._smoking_first = smoking_first
        self._checkin_value = checkin_value
        self._enable_auto_retry = enable_auto_retry
        self._enable_overwrite = enable_overwrite
    
    @property
    def hotel(self) -> Hotel:
        """_summary_

        Returns
        -------
        Hotel
            _description_
        """
        return self._hotel
    
    @property
    def checkin_date(self) -> datetime.date:
        """_summary_

        Returns
        -------
        datetime.date
            _description_
        """
        return self._checkin_date
    
    @property
    def type(self) -> RoomType:
        """_summary_

        Returns
        -------
        RoomType
            _description_
        """
        return self._type
    
    @property
    def strict_room_type(self) -> bool:
        """_summary_

        Returns
        -------
        bool
            _description_
        """
        return self._strict_room_type
    
    @property
    def enable_no_smoking(self) -> bool:
        """_summary_

        Returns
        -------
        bool
            _description_
        """
        return self._enable_no_smoking
    
    @property
    def enable_smoking(self) -> bool:
        """_summary_

        Returns
        -------
        bool
            _description_
        """
        return self._enable_smoking
    
    @property
    def smoking_first(self) -> bool:
        """_summary_

        Returns
        -------
        bool
            _description_
        """
        return self._smoking_first
    
    @property
    def checkin_value(self) -> CheckinTime:
        """_summary_

        Returns
        -------
        CheckinTime
            _description_
        """
        return self._checkin_value
    
    @property
    def enable_auto_retry(self) -> bool:
        """_summary_

        Returns
        -------
        bool
            _description_
        """
        return self._enable_auto_retry
    
    @property
    def enable_overwrite(self) -> bool:
        """_summary_

        Returns
        -------
        bool
            _description_
        """
        return self._enable_overwrite
