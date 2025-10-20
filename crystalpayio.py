from utils.base import _BaseCrystalPayIO
from api.get_asyncio_api import _Checkout

__all__ = ["CrystalPayIO"]


class CrystalPayIO(_BaseCrystalPayIO):
    @property
    def checkout(self) -> _Checkout:
        return _Checkout(self._login, self._secret)