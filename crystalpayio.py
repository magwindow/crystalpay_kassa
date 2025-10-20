from utils.base import _BaseCrystalPayIO
from api.get_asyncio_api import _Checkout, _Payment

__all__ = ["CrystalPayIO"]


class CrystalPayIO(_BaseCrystalPayIO):
    @property
    def checkout(self) -> _Checkout:
        return _Checkout(self._login, self._secret)
    
    @property
    def payment(self) -> _Payment:
        return _Payment(self._login, self._secret)