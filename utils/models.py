from typing import List, Literal, Optional
from datetime import datetime

from pydantic import BaseModel

class BaseCrystalPayModels(BaseModel):
    error: bool
    errors: List[str]

class CheckoutMe(BaseCrystalPayModels):
    id: int
    name: str
    status_level: int | float
    created_at: datetime
    
class CryptoCurrency(BaseModel):
    amount: int | float
    currency: str
    
 

class CheckoutBalancesCoins(BaseModel):
    BITCOIN: CryptoCurrency
    BITCOINCASH: CryptoCurrency
    BNBCRYPTOBOT: CryptoCurrency
    BNBSMARTCHAIN: CryptoCurrency
    BTCCRYPTOBOT: CryptoCurrency
    CARDKZTP2P: CryptoCurrency
    CARDRUB: CryptoCurrency
    CARDRUBP2P: CryptoCurrency
    CARDRUBTRANSP2P: CryptoCurrency
    DASH: CryptoCurrency
    DOGECOIN: CryptoCurrency
    ETHCRYPTOBOT: CryptoCurrency
    ETHEREUM: CryptoCurrency
    LITECOIN: CryptoCurrency
    LTCCRYPTOBOT: CryptoCurrency
    LZTMARKET: CryptoCurrency
    MONERO: CryptoCurrency
    POLYGON: CryptoCurrency
    SBERPAYP2P: CryptoCurrency
    SBP: CryptoCurrency
    SBPP2P: CryptoCurrency
    SBPTRANSP2P: CryptoCurrency
    SOLANA: CryptoCurrency
    TONCOIN: CryptoCurrency
    TONCRYPTOBOT: CryptoCurrency
    TRON: CryptoCurrency
    USDCSPL: CryptoCurrency
    USDTBEP: CryptoCurrency
    USDTCRYPTOBOT: CryptoCurrency
    USDTPOL: CryptoCurrency
    USDTSPL: CryptoCurrency
    USDTTRC: CryptoCurrency
    
    
class CheckoutBalance(BaseCrystalPayModels):
    balances: CheckoutBalancesCoins
    

class PaymentMethodData(BaseModel):
    name: str
    enabled: bool
    extra_commission_percent: int | float
    minimal_status_level: int
    currency: str
    commission_percent: int | float
    commission: int | float


class PaymentMethod(BaseModel):
    BITCOIN: PaymentMethodData
    BITCOINCASH: PaymentMethodData
    BNBCRYPTOBOT: PaymentMethodData
    BNBSMARTCHAIN: PaymentMethodData
    BTCCRYPTOBOT: PaymentMethodData
    CARDKZTP2P: PaymentMethodData
    CARDRUB: PaymentMethodData
    CARDRUBP2P: PaymentMethodData
    CARDRUBTRANSP2P: PaymentMethodData
    CRYSTALPAY: PaymentMethodData
    DASH: PaymentMethodData
    DOGECOIN: PaymentMethodData
    ETHCRYPTOBOT: PaymentMethodData
    ETHEREUM: PaymentMethodData
    LITECOIN: PaymentMethodData
    LTCCRYPTOBOT: PaymentMethodData
    LZTMARKET: PaymentMethodData
    MONERO: PaymentMethodData
    POLYGON: PaymentMethodData
    SBERPAYP2P: PaymentMethodData
    SBP: PaymentMethodData
    SBPP2P: PaymentMethodData
    SBPTRANSP2P: PaymentMethodData
    SOLANA: PaymentMethodData
    TEST: PaymentMethodData
    TONCOIN: PaymentMethodData
    TONCRYPTOBOT: PaymentMethodData
    TRON: PaymentMethodData
    USDCSPL: PaymentMethodData
    USDTBEP: PaymentMethodData
    USDTCRYPTOBOT: PaymentMethodData
    USDTPOL: PaymentMethodData
    USDTSPL: PaymentMethodData
    USDTTRC: PaymentMethodData


class PaymentMethods(BaseCrystalPayModels):
    method: PaymentMethod
    

class PaymentInvoice(BaseCrystalPayModels):
    id: str
    url: str
    amount: int | float
    type: str
    
    
class PaymentInvoiceInfo(BaseCrystalPayModels):
    id: str
    url: str
    state: str
    type: Literal["purchase", "topup"]
    method: Optional[str]
    required_method: Optional[str]
    currency: str
    service_commission: int | float
    extra_commission: int | float
    amount: int | float
    pay_amount: int | float
    remaining_amount: int | float
    balance_amount: int | float
    description: Optional[str]
    redirect_url: str
    callback_url: Optional[str]
    extra: Optional[str]
    created_at: datetime
    expired_at: datetime