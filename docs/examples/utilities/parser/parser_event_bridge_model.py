from datetime import datetime
from typing import Any, Dict, List

from aws_lambda_powertools.utilities.parser import BaseModel, Field


class EventBridgeModel(BaseModel):
    version: str
    id: str  # noqa: A003,VNE003
    source: str
    account: str
    time: datetime
    region: str
    resources: List[str]
    detail_type: str = Field(None, alias="detail-type")
    detail: Dict[str, Any]
