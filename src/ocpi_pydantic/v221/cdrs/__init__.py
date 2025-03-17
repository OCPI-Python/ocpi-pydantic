from pydantic import BaseModel, Field

from ocpi_pydantic.v221.base import OcpiBaseResponse
from ocpi_pydantic.v221.enum import OcpiTokenTypeEnum



class OcpiCdrToken(BaseModel):
    '''
    OCPI 10.4.5. CdrToken class

    - `uid`:  
        Unique ID by which this Token can be identified.
        This is the field used by the CPO’s system (RFID reader on the Charge Point) to
        identify this token.
        Currently, in most cases: type=RFID, this is the RFID hidden ID as read by the
        RFID reader, but that is not a requirement.
        If this is a type=APP_USER Token, it will be a unique, by the eMSP, generated
        ID.
    - `contract_id`:
        Uniquely identifies the EV driver contract token within the eMSP’s platform (and
        suboperator platforms). Recommended to follow the specification for eMA ID
        from "eMI3 standard version V1.0" (http://emi3group.com/documents-links/)
        "Part 2: business objects."
    '''

    country_code: str = Field(description="ISO-3166 alpha-2 country code of the MSP that 'owns' this Token.", min_length=2, max_length=2)
    party_id: str = Field(description="ID of the eMSP that 'owns' this Token (following the ISO-15118 standard).", min_length=3, max_length=3)
    uid: str = Field(description='Unique ID by which this Token can be identified.', max_length=36)
    type: OcpiTokenTypeEnum = Field(description='Type of the token')
    contract_id: str = Field(description='Uniquely identifies the EV driver contract token within the eMSP’s platform (and suboperator platforms).')