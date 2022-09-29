from ipaddress import IPv4Address
from typing import Dict

from monkeyevents.types import NetworkPort, PortStatus

from . import AbstractAgentEvent


class TCPScanEvent(AbstractAgentEvent):
    """
    An event that occurs when the Agent performs a TCP scan on a host

    Attributes:
        :param ports: The scanned ports and their status (open/closed)
    """

    target: IPv4Address
    ports: Dict[NetworkPort, PortStatus]
