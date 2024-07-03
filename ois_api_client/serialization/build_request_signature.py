from datetime import datetime, timezone
from typing import List
from hashlib import sha3_512


def build_request_signature(
        request_id: str, 
        timestamp: datetime, 
        signature_key: str,
        hash_list: List[str] = None,
        operation: str = None,
        invoice_base64: str = None
    ) -> str:
    formatted_time = timestamp.astimezone(tz=timezone.utc).strftime('%Y%m%d%H%M%S')
    signature = f'{request_id}{formatted_time}{signature_key}'

    if operation and invoice_base64:
        additional_signature = f'{operation}{invoice_base64}'
        ut8_encoded = additional_signature.encode('UTF-8', 'strict')
        signature += sha3_512(ut8_encoded).hexdigest().upper()

    ut8_encoded = signature.encode('UTF-8', 'strict')
    result = sha3_512(ut8_encoded).hexdigest()
    return result.upper()
