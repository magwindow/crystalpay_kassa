from typing import Literal

from utils.base import _BaseCrystalPayIO
from utils.models import (CheckoutBalance,
                          CheckoutBalancesCoins,
                          CheckoutMe, 
                          PaymentMethods, 
                          PaymentMethod,
                          BaseCrystalPayModels,
                          PaymentInvoice
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
        
    async def edit(self, method: str, extra_commission_percent: int, enabled: bool) -> BaseCrystalPayModels:
        """Changing payment method settings.
        :param method: Payment method, for example: LZTMARKET, BITCOIN.
        :param extra_commission_percent: Additional cash desk commission for the payment method (in percent).
        :param enabled: Enable/disable payment method.
        """

        self._DEFAULT_PAYLOAD.update(
            {
                "method": method,
                "extra_commission_percent": extra_commission_percent,
                "enabled": enabled,
            }
        )

        response = await self._make_request("method/edit", "post", json=self._DEFAULT_PAYLOAD)
        return BaseCrystalPayModels.model_validate(response)
    
    
class _Invoice(_BaseCrystalPayIO):
    async def create(
        self,
        amount: float | int,
        lifetime: int,
        type: Literal["purchase", "topup"]="purchase",
        *,
        amount_currency: str | None=None,
        required_method: str | None=None,
        description: str | None=None,
        redirect_url: str | None=None,
        callback_url: str | None=None,
        extra: str | None=None,
        payer_details: str | None=None
    ) -> PaymentInvoice:
        """Initiating payment transaction.

        :param amount: The amount of the transaction.
        :param lifetime: The duration (in seconds) for which the payment link is valid.
        :param type: The type of the transaction, either "purchase" or "topup" (default is "purchase").
        :param amount_currency: The currency code for the transaction amount (e.g., "USD").
        :param required_method: The specific payment method required for the transaction.
        :param description: A description or note for the transaction.
        :param redirect_url: The URL to redirect to after the payment is completed.
        :param callback_url: The URL for receiving callback notifications after payment.
        :param extra: Additional information or parameters for the transaction.
        :param payer_details: Additional details about the payer.
        """

        self._DEFAULT_PAYLOAD.update(
            {
                "amount": amount,
                "lifetime": lifetime,
                "type": type,
                "amount_currency": amount_currency,
                "required_method": required_method,
                "description": description,
                "redirect_url": redirect_url,
                "callback_url": callback_url,
                "extra": extra,
                "payer_details": payer_details   
            }
        )

        response = await self._make_request("invoice/create", "post", json=self._DEFAULT_PAYLOAD)
        return PaymentInvoice.model_validate(response)