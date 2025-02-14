from enum import Enum

from pydantic import AwareDatetime, BaseModel, Field

from ocpi_pydantic.v221.base import OcpiDisplayText, OcpiGeoLocation, OcpiImage
from ocpi_pydantic.v221.locations.connector import OcpiConnector




class OcpiStatusEnum(str, Enum):
    '''
    OCPI 8.4.22. Status enum
    '''
    AVAILABLE = 'AVAILABLE' # The EVSE/Connector is able to start a new charging session.
    BLOCKED = 'BLOCKED' # The EVSE/Connector is not accessible because of a physical barrier, i.e. a car.
    CHARGING = 'CHARGING' # The EVSE/Connector is in use.
    INOPERATIVE = 'INOPERATIVE' # The EVSE/Connector is not yet active, or temporarily not available for use, but not broken or defect.
    OUTOFORDER = 'OUTOFORDER' # The EVSE/Connector is currently out of order, some part/components may be broken/defect.
    PLANNED = 'PLANNED' # The EVSE/Connector is planned, will be operating soon.
    REMOVED = 'REMOVED' # The EVSE/Connector was discontinued/removed.
    RESERVED = 'RESERVED' # The EVSE/Connector is reserved for a particular EV driver and is unavailable for other drivers.
    UNKNOWN = 'UNKNOWN' # No status information available (also used when offline).



class OcpiStatusSchedule(BaseModel):
    '''
    OCPI 8.4.23. StatusSchedule class

    即使有狀態排程，還是要即時更新實際的狀態。
    '''
    period_begin: AwareDatetime = Field(description='Begin of the scheduled period.')
    period_end: AwareDatetime | None = Field(None, description='End of the scheduled period, if known.')
    status: OcpiStatusEnum = Field(description='Status value during the scheduled period.')



class OcpiCapabilityEnum(str, Enum):
    '''
    OCPI 8.4.3. Capability enum
    '''
    CHARGING_PROFILE_CAPABLE = 'CHARGING_PROFILE_CAPABLE' # The EVSE supports charging profiles.
    CHARGING_PREFERENCES_CAPABLE = 'CHARGING_PREFERENCES_CAPABLE' # The EVSE supports charging profiles.
    CHIP_CARD_SUPPORT = 'CHIP_CARD_SUPPORT' # EVSE has a payment terminal that supports chip cards.
    CONTACTLESS_CARD_SUPPORT = 'CONTACTLESS_CARD_SUPPORT' # EVSE has a payment terminal that supports contactless cards.
    CREDIT_CARD_PAYABLE = 'CREDIT_CARD_PAYABLE' # EVSE has a payment terminal that makes it possible to pay for charging using a credit card.
    DEBIT_CARD_PAYABLE = 'DEBIT_CARD_PAYABLE' # EVSE has a payment terminal that makes it possible to pay for charging using a debit card.
    PED_TERMINAL = 'PED_TERMINAL' # EVSE has a payment terminal with a pin-code entry device.
    REMOTE_START_STOP_CAPABLE = 'REMOTE_START_STOP_CAPABLE' # The EVSE can remotely be started/stopped.
    RESERVABLE = 'RESERVABLE' # The EVSE can be reserved.
    RFID_READER = 'RFID_READER' # Charging at this EVSE can be authorized with an RFID token.
    START_SESSION_CONNECTOR_REQUIRED = 'START_SESSION_CONNECTOR_REQUIRED' # When a StartSession is sent to this EVSE, the MSP is required to add the optional connector_id field in the StartSession object.
    TOKEN_GROUP_CAPABLE = 'TOKEN_GROUP_CAPABLE' # This EVSE supports token groups, two or more tokens work as one, so that a session can be started with one token and stopped with another (handy when a card and key-fob are given to the EV-driver).
    UNLOCK_CAPABLE = 'UNLOCK_CAPABLE' # Connectors have mechanical lock that can be requested by the eMSP to be unlocked.



class OcpiParkingRestrictionEnum(str, Enum):
    '''
    OCPI 8.4.17. ParkingRestriction enum
    '''
    EV_ONLY = 'EV_ONLY' # Reserved parking spot for electric vehicles.
    PLUGGED = 'PLUGGED' # Parking is only allowed while plugged in (charging).
    DISABLED = 'DISABLED' # Reserved parking spot for disabled people with valid ID.
    CUSTOMERS = 'CUSTOMERS' # Parking spot for customers/guests only, for example in case of a hotel or shop.
    MOTORCYCLES = 'MOTORCYCLES' # Parking spot only suitable for (electric) motorcycles or scooters.



class OcpiEvse(BaseModel):
    '''
    8.3.2. EVSE Object
    '''
    uid: str = Field(description='Uniquely identifies the EVSE within the CPOs platform (and suboperator platforms).', max_length=36)
    evse_id: str | None = Field(None, description='Compliant with the following specification for EVSE ID from "eMI3 standard version V1.0" (http://emi3group.com/documents-links/) "Part 2: business objects."', max_length=48)
    status: OcpiStatusEnum = Field(description='Indicates the current status of the EVSE.')
    status_schedule: list[OcpiStatusSchedule] = Field([], description='Indicates a planned status update of the EVSE.')
    capabilities: list[OcpiCapabilityEnum] = Field([], description='List of functionalities that the EVSE is capable of.')
    connectors: list[OcpiConnector] = Field([], description='List of available connectors on the EVSE.')
    floor_level: str | None = Field(None, description='Level on which the Charge Point is located (in garage buildings) in the locally displayed numbering scheme.', max_length=4)
    coordinates: OcpiGeoLocation | None = Field(None, description='Coordinates of the EVSE.')
    physical_reference: str | None = Field(None, description='A number/string printed on the outside of the EVSE for visual identification.', max_length=16)
    directions: list[OcpiDisplayText] = Field([], description='Multi-language human-readable directions when more detailed information on how to reach the EVSE from the Location is required.')
    parking_restrictions: list[OcpiParkingRestrictionEnum] = Field([], description='The restrictions that apply to the parking spot.')
    images: list[OcpiImage] = Field([], description='Links to images related to the EVSE such as photos or logos.')
    last_updated: AwareDatetime = Field(description='Timestamp when this EVSE or one of its Connectors was last updated (or created).')
