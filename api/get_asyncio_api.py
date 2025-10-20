from utils.base import _BaseCrystalPayIO
from utils.models import (CheckoutBalance,
                          CheckoutBalancesCoins,
                          CheckoutMe, 
                          PaymentMethods, 
                          PaymentMethod
                          )
 


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
        # print(response["balances"])
        return CheckoutBalance(
            error=response["error"],
            errors=response["errors"],
            balances=CheckoutBalancesCoins.model_validate(response["balances"])
        )
        

class _Payment(_BaseCrystalPayIO):
    async def methods(self) -> PaymentMethods:
        """Obtaining information on payment methods."""
        response = await self._make_request("method/list", "post", json=self._DEFAULT_PAYLOAD)
        # print(response)
        return PaymentMethods(
            error=response["error"],
            errors=response["errors"],
            method=PaymentMethod.model_validate(response["methods"])
        )