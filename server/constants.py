from enum import Enum


class MessageType(Enum):
    UpdateDeviceStatus = 1,
    UpdateDevicePosition = 2,
    CreateDevice = 3,
    DeleteDevice = 4,
    GetDevices = 5,


class ErrorCode(Enum):
    Success = 1,
    InvalidMessageType = -1,
    InvalidDeviceParameters = -2,


devices = {
    0: 'simple_lamp',
    1: 'complex_lamp',
    2: 'ventilator',
    3: 'jalousie',
    4: 'door',
    5: 'battery'
}
