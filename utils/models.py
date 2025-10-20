from typing import Dict, List, Literal, Optional
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
    
    
class PayoffCreate(BaseCrystalPayModels):
    id: str
    method: str
    commission: int | float
    amount: int | float
    rub_amount: int | float
    receive_amount: int | float
    deduction_amount: int | float
    subtract_from: str
    currency: str
    
    
class PayoffAction(BaseCrystalPayModels):
    id: str
    state: str
    method: str
    currency: str
    commission: int | float
    amount: int | float
    rub_amount: int | float
    receive_amount: int | float
    deduction_amount: int | float
    subtract_from: str
    wallet: str
    message: str
    callback_url: str
    extra: str
    created_at: str
    
    
class Tickers(BaseCrystalPayModels):
    tickers: List[str]


class TickersData(BaseCrystalPayModels):
    base_currency: str
    currencies: Dict[str, int | float]
    

class HistoryBaseData(BaseModel):
    id: str
    state: str
    method: Optional[str]
    currency: str
    amount: int | float
    created_at: str
    expired_at: Optional[str] = None


class HistoryPayments(BaseCrystalPayModels):
    payments: List[HistoryBaseData]
    

class HistoryPayoffs(BaseCrystalPayModels):
    payoffs: List[HistoryBaseData]
    
    
class HistorySummaryData(BaseModel):
    payed_amount: int | float
    total_count: int | float
    payed_count: int | float


class HistorySummary(BaseCrystalPayModels):
    incoming: HistorySummaryData
    outgoing: HistorySummaryData