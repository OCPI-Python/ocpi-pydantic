from datetime import datetime, timezone
from typing import ClassVar, Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

from ocpi_pydantic.v221.enum import OcpiStatus



class OcpiDisplayText(BaseModel):
    '''
    OCPI 16.3. DisplayText class
    '''
    language: str = Field(description='Language Code ISO 639-1.', max_length=2)
    text: str = Field(description='Text to be displayed to a end user.', max_length=512)

    _example: ClassVar[dict] = {"language": "en", "text": "Standard Tariff"}
    model_config = ConfigDict(json_schema_extra={'examples': [_example]})



OcpiResponseDataGenericType = TypeVar('OcpiResponseDataGenericType')



class OcpiBaseResponse(BaseModel, Generic[OcpiResponseDataGenericType]):
    '''
    OCPI 4.1.7 Response format


    '''
    # data: list[BaseModel] | OcpiBaseResponseData | list[OcpiBaseResponseData] | str | BaseModel | None = None # 這裡是不要要泛型
    data: OcpiResponseDataGenericType | None = Field(None, description='Contains the actual response data object or list of objects from each request.')
    status_code: OcpiStatus = Field(description='OCPI status code.')
    status_message: str | None = Field(None, description='An optional status message which may help when debugging.')
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc).replace(microsecond=0), description='The time this message was generated.')

    _examples: ClassVar[dict] = [
        {'data': None, 'status_code': 1000, 'timestamp': '2015-06-30T21:59:59Z'},
        { # Tokens GET Response with one Token object. (CPO end-point) (one object)
            "data": {
                "country_code": "DE",
                "party_id": "TNM",
                "uid": "012345678",
                "type": "RFID",
                "contract_id": "FA54320",
                "visual_number": "DF000-2001-8999",
                "issuer": "TheNewMotion",
                "valid": True,
                "whitelist": "ALLOWED",
                "last_updated": "2015-06-29T22:39:09Z",
            },
            "status_code": 1000,
            "status_message": "Success",
            "timestamp": "2015-06-30T21:59:59Z",
        },
        { # Tokens GET Response with list of Token objects. (eMSP end-point) (list of objects)
            "data": [
                {
                    "country_code": "NL",
                    "party_id": "TNM",
                    "uid": "100012",
                    "type": "RFID",
                    "contract_id": "FA54320",
                    "visual_number": "DF000-2001-8999",
                    "issuer": "TheNewMotion",
                    "valid": True,
                    "whitelist": "ALWAYS",
                    "last_updated": "2015-06-21T22:39:05Z",
                },
                {
                    "country_code": "NL",
                    "party_id": "TNM",
                    "uid": "100013",
                    "type": "RFID",
                    "contract_id": "FA543A5",
                    "visual_number": "DF000-2001-9000",
                    "issuer": "TheNewMotion",
                    "valid": True,
                    "whitelist": "ALLOWED",
                    "last_updated": "2015-06-28T11:21:09Z",
                },
                {
                    "country_code": "NL",
                    "party_id": "TNM",
                    "uid": "100014",
                    "type": "RFID",
                    "contract_id": "FA543BB",
                    "visual_number": "DF000-2001-9010",
                    "issuer": "TheNewMotion",
                    "valid": True,
                    "whitelist": "ALLOWED",
                    "last_updated": "2015-05-29T10:12:26Z"
                }
            ],
            "status_code": 1000,
            "status_message": "Success",
            "timestamp": "2015-06-30T21:59:59Z",
        },
        { # Response with an error (contains no data field)
            "status_code": 2001,
            "status_message": "Missing required field: type",
            "timestamp": "2015-06-30T21:59:59Z",
        }
    ]
    model_config = ConfigDict(json_schema_extra={'examples': _examples})
