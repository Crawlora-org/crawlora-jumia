"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class JumiaClient(CrawloraClient):
    """Synchronous Jumia API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-jumia-python/0.1.0')
        super().__init__(*args, **kwargs)

    def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('jumia-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def category(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('jumia-category', params, response_type=response_type, timeout=timeout, headers=headers)

    def countries(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('jumia-countries', params, response_type=response_type, timeout=timeout, headers=headers)

    def product(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('jumia-product', params, response_type=response_type, timeout=timeout, headers=headers)

    def reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('jumia-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('jumia-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def sitemap_urls(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('jumia-sitemap-urls', params, response_type=response_type, timeout=timeout, headers=headers)

    def sitemaps(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('jumia-sitemaps', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncJumiaClient(AsyncCrawloraClient):
    """Asynchronous Jumia API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-jumia-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('jumia-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def category(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('jumia-category', params, response_type=response_type, timeout=timeout, headers=headers)

    async def countries(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('jumia-countries', params, response_type=response_type, timeout=timeout, headers=headers)

    async def product(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('jumia-product', params, response_type=response_type, timeout=timeout, headers=headers)

    async def reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('jumia-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('jumia-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sitemap_urls(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('jumia-sitemap-urls', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sitemaps(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('jumia-sitemaps', params, response_type=response_type, timeout=timeout, headers=headers)
