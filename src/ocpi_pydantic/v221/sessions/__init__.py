from typing import ClassVar

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from ocpi_pydantic.v221.base import OcpiBaseResponse



class OcpiSession(BaseModel):
    '''
    OCPI 9.3.1. Session Object

    - `start_date_time`:  
        The timestamp when the session became ACTIVE in the Charge
        Point.
        When the session is still PENDING, this field SHALL be set to the
        time the Session was created at the Charge Point. When a Session
        goes from PENDING to ACTIVE, this field SHALL be updated to the
        moment the Session went to ACTIVE in the Charge Point.
    '''

    country_code: str = Field(description="ISO-3166 alpha-2 country code of the CPO that 'owns' this Session.", min_length=2, max_length=2)
    party_id: str = Field(description="ID of the CPO that 'owns' this Session (following the ISO-15118 standard).", min_length=3, max_length=3)
    id: str = Field(description='The unique id that identifies the charging session in the CPO platform.', max_length=36)
    start_date_time: AwareDatetime = Field(description='The timestamp when the session became ACTIVE in the Charge Point.')
    end_date_time: AwareDatetime | None = Field(None, description='The timestamp when the session was completed/finished, charging might have finished before the session ends, for example: EV is full, but parking cost also has to be paid.')
    kwh: int = Field(description='How many kWh were charged.')
    cdr_token = Field(description='Token used to start this charging session, including all the relevant information to identify the unique token.')

    _examples: ClassVar[list[dict]] = [
        {
            'url': 'https://example.com/ocpi/cpo/2.2/credentials',
        },
    ]
    model_config = ConfigDict(json_schema_extra={'examples': _examples})