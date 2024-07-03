import xml.etree.ElementTree as ET

from .serialize_additional_query_params import serialize_additional_query_params
from .serialize_basic_online_invoice_request import serialize_basic_online_invoice_request
from .serialize_element import serialize_text_element, serialize_int_element
from .serialize_mandatory_query_params import serialize_mandatory_query_params
from .serialize_relational_query_params import serialize_relational_query_params
from .serialize_transaction_query_params import serialize_transaction_query_params
from ..v3_0 import dto, namespaces as ns


def serialize_query_transaction_status_request(data: dto.QueryTransactionStatusRequest) -> ET.Element:
    root = serialize_basic_online_invoice_request(data, 'QueryTransactionStatusRequest')

    serialize_text_element(root, 'transactionId', data.transaction_id, ns.API)
    serialize_text_element(root, 'returnOriginalRequest', "true" if data.return_original_request else "false", ns.API)

    return root
