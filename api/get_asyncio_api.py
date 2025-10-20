from typing import Any

from utils.models import CheckoutBalance, CheckoutBalancesCoins, CheckoutMe  
from utils.base import _BaseCrystalPayIO



class _Checkout(_BaseCrystalPayIO):
    async def me(self) -> CheckoutMe:
        """Cash register information."""
        response = await self._make_request("me/info", "post", json=self._DEFAULT_PAYLOAD)
        return CheckoutMe(**response)
    
    async def balance(self, hide_empty: bool=False) -> CheckoutBalance:
        """Cash balance receipt.
        :param hide_empty: Hide empty accounts.
        """
        self._DEFAULT_PAYLOAD.update({"hide_empty": hide_empty})
        response = await self._make_request("balance/info", "post", json=self._DEFAULT_PAYLOAD)
        print(response)
        return CheckoutBalance(
            error=response["error"],
            errors=response["errors"],
            balances=CheckoutBalancesCoins.model_validate(response["balances"])
        )