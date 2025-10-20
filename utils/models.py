from typing import List
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