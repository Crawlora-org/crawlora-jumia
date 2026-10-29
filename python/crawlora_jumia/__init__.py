"""Typed Jumia client for the Crawlora hosted API."""

from .platform import JumiaClient, AsyncJumiaClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = JumiaClient
AsyncClient = AsyncJumiaClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Jumia'
PLATFORM = 'jumia'
CONTRACT_REVISION = 'sha256:ec487d49dce5bc76b62cd97844910f1b3def9fbc1e610492cc9432624f6ea6e4'

__all__ = [
    "JumiaClient", "AsyncJumiaClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
