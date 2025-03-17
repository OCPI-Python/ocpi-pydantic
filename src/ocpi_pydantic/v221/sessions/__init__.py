from typing import ClassVar

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from ocpi_pydantic.v221.base import OcpiBaseResponse
from ocpi_pydantic.v221.cdrs import OcpiCdrToken, OcpiChargingPeriod
from ocpi_pydantic.v221.enum import OcpiAuthMethodEnum



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
    - `auth_method`:
        Method used for authentication. This might change during a
        session, for example when the session was started with a
        reservation: ReserveNow: `COMMAND`. When the driver arrives and
        starts charging using a Token that is whitelisted: `WHITELIST`.
    - `authorization_reference`:
        Reference to the authorization given by the eMSP. When the eMSP
        provided an `authorization_reference` in either: real-time
        authorization, StartSession or ReserveNow this field SHALL
        contain the same value. When different
        `authorization_reference` values have been given by the
        eMSP that are relevant to this Session, the last given value SHALL
        be used here.
    - `evse_uid`:
        EVSE.uid of the EVSE of this Location on which the charging
        session is/was happening. Allowed to be set to: `#NA` when this
        session is created for a reservation, but no EVSE yet assigned to
        the driver.
    - `connector_id`:
        Connector.id of the Connector of this Location where the charging
        session is/was happening. Allowed to be set to: `#NA` when this
        session is created for a reservation, but no connector yet assigned
        to the driver.
    '''

    country_code: str = Field(description="ISO-3166 alpha-2 country code of the CPO that 'owns' this Session.", min_length=2, max_length=2)
    party_id: str = Field(description="ID of the CPO that 'owns' this Session (following the ISO-15118 standard).", min_length=3, max_length=3)
    id: str = Field(description='The unique id that identifies the charging session in the CPO platform.', max_length=36)
    start_date_time: AwareDatetime = Field(description='The timestamp when the session became ACTIVE in the Charge Point.')
    end_date_time: AwareDatetime | None = Field(None, description='The timestamp when the session was completed/finished, charging might have finished before the session ends, for example: EV is full, but parking cost also has to be paid.')
    kwh: int = Field(description='How many kWh were charged.')
    cdr_token: OcpiCdrToken = Field(description='Token used to start this charging session, including all the relevant information to identify the unique token.')
    auth_method: OcpiAuthMethodEnum = Field(description='Method used for authentication.')
    authorization_reference: str | None = Field(None, description='Reference to the authorization given by the eMSP.', max_length=36)
    location_id: str = Field(description='Location.id of the Location object of this CPO, on which the charging session is/was happening.', max_length=36)
    evse_uid : str = Field(description='EVSE.uid of the EVSE of this Location on which the charging session is/was happening.', max_length=36)
    connector_id : str = Field(description='Connector.id of the Connector of this Location where the charging session is/was happening.', max_length=36)
    meter_id: str | None = Field(None, description='Optional identification of the kWh meter.', max_length=255)
    currency: str = Field(description='ISO 4217 code of the currency used for this session.', max_length=3)
    charging_periods: list[OcpiChargingPeriod] = Field([], description='An optional list of Charging Periods that can be used to calculate and verify the total cost.')

    _examples: ClassVar[list[dict]] = [
        {
            'url': 'https://example.com/ocpi/cpo/2.2/credentials',
        },
    ]
    model_config = ConfigDict(json_schema_extra={'examples': _examples})