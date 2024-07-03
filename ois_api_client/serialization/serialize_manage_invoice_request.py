import xml.etree.ElementTree as ET

from .serialize_basic_online_invoice_request import serialize_basic_online_invoice_request
from .serialize_element import serialize_text_element, serialize_int_element
from ..v3_0 import dto, namespaces as ns
# from ..v3_0.dto.QueryInvoiceDataRequest import QueryInvoiceDataRequest
# from ..v3_0.namespaces import NAMESPACE_API


def serialize_query_invoice_data_request_type(parent: ET.Element, data: dto.ManageInvoiceRequest) -> ET.Element:
    serialize_text_element(parent, 'exchangeToken', data.exchange_token, ns.API)

    result = ET.SubElement(parent, 'invoiceOperations')
    serialize_text_element(result, 'compressedContent', "true" if data.invoice_operations.compressed_content else "false", ns.API)
    
    operations = serialize_text_element(result, 'invoiceOperation', '', ns.API)
    serialize_int_element(operations, 'index', data.invoice_operations.invoice_operation[0].index, ns.API)
    serialize_text_element(operations, 'invoiceOperation', data.invoice_operations.invoice_operation[0].invoice_operation.value, ns.API)
    serialize_text_element(operations, 'invoiceData', data.invoice_operations.invoice_operation[0].invoice_data, ns.API)


    return parent


def serialize_manage_invoice_request(data: dto.ManageInvoiceRequest) -> ET.Element:
    root = serialize_basic_online_invoice_request(data, 'ManageInvoiceRequest')
    serialize_query_invoice_data_request_type(root, data)
    return root
