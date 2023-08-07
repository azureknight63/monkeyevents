from .abstract_agent_event import AbstractAgentEvent, AgentEventTag, EVENT_TAG_REGEX
from .agent_event_registry import AgentEventRegistry
from .credentials_stolen_events import CredentialsStolenEvent
from .ping_scan_event import PingScanEvent
from .tcp_scan_event import TCPScanEvent
from .exploitation_event import ExploitationEvent
from .propagation_event import PropagationEvent
from .password_restoration_event import PasswordRestorationEvent
from .agent_shutdown_event import AgentShutdownEvent
from .file_encryption_event import FileEncryptionEvent
from .os_discovery_event import OSDiscoveryEvent
from .hostname_discovery_event import HostnameDiscoveryEvent
from .register import register_common_agent_events
from .cpu_consumption_event import CPUConsumptionEvent
