from aws_lambda_powertools.utilities.jmespath_utils import extract_data_from_envelope
from aws_lambda_powertools.utilities.typing import LambdaContext


def handler(event: dict, context: LambdaContext):
    payload = extract_data_from_envelope(data=event, envelope="powertools_json(body)")
    customer = payload.get("customerId")  # now deserialized
    ...
