from datetime import datetime
from dataclasses import dataclass
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse


@dataclass
class ManageInvoiceResponse(BasicOnlineInvoiceResponse):
    transaction_id: str
