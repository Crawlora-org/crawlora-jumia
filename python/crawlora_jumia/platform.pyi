from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelJumiaSitemapsResponseDoc = TypedDict('ModelJumiaSitemapsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJumiaSitemapsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJumiaSitemapsResponse = TypedDict('ModelJumiaSitemapsResponse', {
    'count': NotRequired[int],
    'country': NotRequired[str],
    'fetched_at': NotRequired[str],
    'sitemaps': NotRequired[list[ModelJumiaSitemapFile]],
    'source_url': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelJumiaSitemapFile = TypedDict('ModelJumiaSitemapFile', {
    'language': NotRequired[str],
    'last_modified': NotRequired[str],
    'name': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelJumiaSitemapUrlsResponseDoc = TypedDict('ModelJumiaSitemapUrlsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJumiaSitemapUrlsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJumiaSitemapUrlsResponse = TypedDict('ModelJumiaSitemapUrlsResponse', {
    'count': NotRequired[int],
    'country': NotRequired[str],
    'fetched_at': NotRequired[str],
    'has_next': NotRequired[bool],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'sitemap': NotRequired[str],
    'source_url': NotRequired[str],
    'total_count': NotRequired[int],
    'urls': NotRequired[list[ModelJumiaSitemapUrl]],
}, total=False)

ModelJumiaSitemapUrl = TypedDict('ModelJumiaSitemapUrl', {
    'image': NotRequired[str],
    'last_modified': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelJumiaListingResponseDoc = TypedDict('ModelJumiaListingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJumiaListingResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJumiaListingResponse = TypedDict('ModelJumiaListingResponse', {
    'category': NotRequired[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'fetched_at': NotRequired[str],
    'has_next': NotRequired[bool],
    'page': NotRequired[int],
    'products': NotRequired[list[ModelJumiaListing]],
    'query': NotRequired[str],
    'source_url': NotRequired[str],
    'total_count': NotRequired[int],
}, total=False)

ModelJumiaListing = TypedDict('ModelJumiaListing', {
    'brand': NotRequired[str],
    'categories': NotRequired[list[str]],
    'currency': NotRequired[str],
    'discount_percent': NotRequired[int],
    'image': NotRequired[str],
    'jumia_express': NotRequired[bool],
    'name': NotRequired[str],
    'official_store': NotRequired[bool],
    'original_price': NotRequired[float],
    'out_of_stock': NotRequired[bool],
    'price': NotRequired[float],
    'price_max': NotRequired[float],
    'rating': NotRequired[float],
    'rating_count': NotRequired[int],
    'sku': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelJumiaReviewsResponseDoc = TypedDict('ModelJumiaReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJumiaReviewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJumiaReviewsResponse = TypedDict('ModelJumiaReviewsResponse', {
    'average_rating': NotRequired[float],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'fetched_at': NotRequired[str],
    'has_next': NotRequired[bool],
    'histogram': NotRequired[list[ModelJumiaRatingBucket]],
    'page': NotRequired[int],
    'rating_count': NotRequired[int],
    'review_count': NotRequired[int],
    'reviews': NotRequired[list[ModelJumiaReview]],
    'sku': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelJumiaReview = TypedDict('ModelJumiaReview', {
    'author': NotRequired[str],
    'date': NotRequired[str],
    'rating': NotRequired[int],
    'text': NotRequired[str],
    'title': NotRequired[str],
    'verified': NotRequired[bool],
}, total=False)

ModelJumiaRatingBucket = TypedDict('ModelJumiaRatingBucket', {
    'count': NotRequired[int],
    'stars': NotRequired[int],
}, total=False)

ModelJumiaProductResponseDoc = TypedDict('ModelJumiaProductResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJumiaProduct],
    'msg': NotRequired[str],
}, total=False)

ModelJumiaProduct = TypedDict('ModelJumiaProduct', {
    'availability': NotRequired[str],
    'brand': NotRequired[str],
    'categories': NotRequired[list[str]],
    'country': NotRequired[str],
    'currency': NotRequired[str],
    'description': NotRequired[str],
    'discount_percent': NotRequired[int],
    'fetched_at': NotRequired[str],
    'images': NotRequired[list[str]],
    'key_features': NotRequired[str],
    'name': NotRequired[str],
    'original_price': NotRequired[float],
    'price': NotRequired[float],
    'rating': NotRequired[float],
    'rating_count': NotRequired[int],
    'seller': NotRequired[ModelJumiaSeller],
    'sku': NotRequired[str],
    'specifications': NotRequired[list[ModelJumiaSpecification]],
    'url': NotRequired[str],
}, total=False)

ModelJumiaSpecification = TypedDict('ModelJumiaSpecification', {
    'name': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelJumiaSeller = TypedDict('ModelJumiaSeller', {
    'followers': NotRequired[int],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'score_percent': NotRequired[float],
    'shipping_speed': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelJumiaCountriesResponseDoc = TypedDict('ModelJumiaCountriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJumiaCountriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJumiaCountriesResponse = TypedDict('ModelJumiaCountriesResponse', {
    'count': NotRequired[int],
    'countries': NotRequired[list[ModelJumiaCountry]],
}, total=False)

ModelJumiaCountry = TypedDict('ModelJumiaCountry', {
    'code': NotRequired[str],
    'currency': NotRequired[str],
    'domain': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelJumiaCategoriesResponseDoc = TypedDict('ModelJumiaCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJumiaCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJumiaCategoriesResponse = TypedDict('ModelJumiaCategoriesResponse', {
    'categories': NotRequired[list[ModelJumiaCategoryNode]],
    'category': NotRequired[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelJumiaCategoryNode = TypedDict('ModelJumiaCategoryNode', {
    'children': NotRequired[list[ModelJumiaCategoryNode]],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

JumiaCategoriesResponse = ModelJumiaCategoriesResponseDoc
JumiaCategoriesParams = TypedDict('JumiaCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'category': NotRequired[str],
}, total=False)

JumiaCategoryResponse = ModelJumiaListingResponseDoc
JumiaCategoryParams = TypedDict('JumiaCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'category': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaCountriesResponse = ModelJumiaCountriesResponseDoc
JumiaCountriesParams = TypedDict('JumiaCountriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

JumiaProductResponse = ModelJumiaProductResponseDoc
JumiaProductParams = TypedDict('JumiaProductParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
}, total=False)

JumiaReviewsResponse = ModelJumiaReviewsResponseDoc
JumiaReviewsParams = TypedDict('JumiaReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'sku': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaSearchResponse = ModelJumiaListingResponseDoc
JumiaSearchParams = TypedDict('JumiaSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'q': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaSitemapUrlsResponse = ModelJumiaSitemapUrlsResponseDoc
JumiaSitemapUrlsParams = TypedDict('JumiaSitemapUrlsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'sitemap': Required[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

JumiaSitemapsResponse = ModelJumiaSitemapsResponseDoc
JumiaSitemapsParams = TypedDict('JumiaSitemapsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'type': NotRequired[Literal['products', 'brands', 'categories', 'mlps']],
}, total=False)

class JumiaGroup:
    @overload
    def categories(self, **params: Unpack[JumiaCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[JumiaCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[JumiaCategoriesDefaultParams]) -> JumiaCategoriesResponse: ...
    @overload
    def category(self, **params: Unpack[JumiaCategoryStreamParams]) -> BinaryIO: ...
    @overload
    def category(self, **params: Unpack[JumiaCategoryTextResponseParams]) -> str: ...
    @overload
    def category(self, **params: Unpack[JumiaCategoryDefaultParams]) -> JumiaCategoryResponse: ...
    @overload
    def countries(self, **params: Unpack[JumiaCountriesStreamParams]) -> BinaryIO: ...
    @overload
    def countries(self, **params: Unpack[JumiaCountriesTextResponseParams]) -> str: ...
    @overload
    def countries(self, **params: Unpack[JumiaCountriesDefaultParams]) -> JumiaCountriesResponse: ...
    @overload
    def product(self, **params: Unpack[JumiaProductStreamParams]) -> BinaryIO: ...
    @overload
    def product(self, **params: Unpack[JumiaProductTextResponseParams]) -> str: ...
    @overload
    def product(self, **params: Unpack[JumiaProductDefaultParams]) -> JumiaProductResponse: ...
    @overload
    def reviews(self, **params: Unpack[JumiaReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def reviews(self, **params: Unpack[JumiaReviewsTextResponseParams]) -> str: ...
    @overload
    def reviews(self, **params: Unpack[JumiaReviewsDefaultParams]) -> JumiaReviewsResponse: ...
    @overload
    def search(self, **params: Unpack[JumiaSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[JumiaSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[JumiaSearchDefaultParams]) -> JumiaSearchResponse: ...
    @overload
    def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsStreamParams]) -> BinaryIO: ...
    @overload
    def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsTextResponseParams]) -> str: ...
    @overload
    def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsDefaultParams]) -> JumiaSitemapUrlsResponse: ...
    @overload
    def sitemaps(self, **params: Unpack[JumiaSitemapsStreamParams]) -> BinaryIO: ...
    @overload
    def sitemaps(self, **params: Unpack[JumiaSitemapsTextResponseParams]) -> str: ...
    @overload
    def sitemaps(self, **params: Unpack[JumiaSitemapsDefaultParams]) -> JumiaSitemapsResponse: ...

OperationId = Literal[
    'jumia-categories',
    'jumia-category',
    'jumia-countries',
    'jumia-product',
    'jumia-reviews',
    'jumia-search',
    'jumia-sitemap-urls',
    'jumia-sitemaps',
]

class CrawloraClient:
    jumia: JumiaGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['jumia-categories'],
        params: JumiaCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['jumia-category'],
        params: JumiaCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaCategoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['jumia-countries'],
        params: JumiaCountriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaCountriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['jumia-product'],
        params: JumiaProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaProductResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['jumia-reviews'],
        params: JumiaReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['jumia-search'],
        params: JumiaSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['jumia-sitemap-urls'],
        params: JumiaSitemapUrlsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaSitemapUrlsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['jumia-sitemaps'],
        params: JumiaSitemapsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaSitemapsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['jumia-categories'],
        params: JumiaCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['jumia-category'],
        params: JumiaCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaCategoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['jumia-countries'],
        params: JumiaCountriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaCountriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['jumia-product'],
        params: JumiaProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaProductResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['jumia-reviews'],
        params: JumiaReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['jumia-search'],
        params: JumiaSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['jumia-sitemap-urls'],
        params: JumiaSitemapUrlsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaSitemapUrlsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['jumia-sitemaps'],
        params: JumiaSitemapsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JumiaSitemapsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class JumiaClient(CrawloraClient):
    def __enter__(self) -> JumiaClient: ...
    @overload
    def categories(self, **params: Unpack[JumiaCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[JumiaCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[JumiaCategoriesDefaultParams]) -> JumiaCategoriesResponse: ...
    @overload
    def category(self, **params: Unpack[JumiaCategoryStreamParams]) -> BinaryIO: ...
    @overload
    def category(self, **params: Unpack[JumiaCategoryTextResponseParams]) -> str: ...
    @overload
    def category(self, **params: Unpack[JumiaCategoryDefaultParams]) -> JumiaCategoryResponse: ...
    @overload
    def countries(self, **params: Unpack[JumiaCountriesStreamParams]) -> BinaryIO: ...
    @overload
    def countries(self, **params: Unpack[JumiaCountriesTextResponseParams]) -> str: ...
    @overload
    def countries(self, **params: Unpack[JumiaCountriesDefaultParams]) -> JumiaCountriesResponse: ...
    @overload
    def product(self, **params: Unpack[JumiaProductStreamParams]) -> BinaryIO: ...
    @overload
    def product(self, **params: Unpack[JumiaProductTextResponseParams]) -> str: ...
    @overload
    def product(self, **params: Unpack[JumiaProductDefaultParams]) -> JumiaProductResponse: ...
    @overload
    def reviews(self, **params: Unpack[JumiaReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def reviews(self, **params: Unpack[JumiaReviewsTextResponseParams]) -> str: ...
    @overload
    def reviews(self, **params: Unpack[JumiaReviewsDefaultParams]) -> JumiaReviewsResponse: ...
    @overload
    def search(self, **params: Unpack[JumiaSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[JumiaSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[JumiaSearchDefaultParams]) -> JumiaSearchResponse: ...
    @overload
    def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsStreamParams]) -> BinaryIO: ...
    @overload
    def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsTextResponseParams]) -> str: ...
    @overload
    def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsDefaultParams]) -> JumiaSitemapUrlsResponse: ...
    @overload
    def sitemaps(self, **params: Unpack[JumiaSitemapsStreamParams]) -> BinaryIO: ...
    @overload
    def sitemaps(self, **params: Unpack[JumiaSitemapsTextResponseParams]) -> str: ...
    @overload
    def sitemaps(self, **params: Unpack[JumiaSitemapsDefaultParams]) -> JumiaSitemapsResponse: ...

class AsyncJumiaClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncJumiaClient: ...
    jumia: _AsyncJumiaGroup
    @overload
    async def categories(self, **params: Unpack[JumiaCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[JumiaCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[JumiaCategoriesDefaultParams]) -> JumiaCategoriesResponse: ...
    @overload
    async def category(self, **params: Unpack[JumiaCategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def category(self, **params: Unpack[JumiaCategoryTextResponseParams]) -> str: ...
    @overload
    async def category(self, **params: Unpack[JumiaCategoryDefaultParams]) -> JumiaCategoryResponse: ...
    @overload
    async def countries(self, **params: Unpack[JumiaCountriesStreamParams]) -> BinaryIO: ...
    @overload
    async def countries(self, **params: Unpack[JumiaCountriesTextResponseParams]) -> str: ...
    @overload
    async def countries(self, **params: Unpack[JumiaCountriesDefaultParams]) -> JumiaCountriesResponse: ...
    @overload
    async def product(self, **params: Unpack[JumiaProductStreamParams]) -> BinaryIO: ...
    @overload
    async def product(self, **params: Unpack[JumiaProductTextResponseParams]) -> str: ...
    @overload
    async def product(self, **params: Unpack[JumiaProductDefaultParams]) -> JumiaProductResponse: ...
    @overload
    async def reviews(self, **params: Unpack[JumiaReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def reviews(self, **params: Unpack[JumiaReviewsTextResponseParams]) -> str: ...
    @overload
    async def reviews(self, **params: Unpack[JumiaReviewsDefaultParams]) -> JumiaReviewsResponse: ...
    @overload
    async def search(self, **params: Unpack[JumiaSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[JumiaSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[JumiaSearchDefaultParams]) -> JumiaSearchResponse: ...
    @overload
    async def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsStreamParams]) -> BinaryIO: ...
    @overload
    async def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsTextResponseParams]) -> str: ...
    @overload
    async def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsDefaultParams]) -> JumiaSitemapUrlsResponse: ...
    @overload
    async def sitemaps(self, **params: Unpack[JumiaSitemapsStreamParams]) -> BinaryIO: ...
    @overload
    async def sitemaps(self, **params: Unpack[JumiaSitemapsTextResponseParams]) -> str: ...
    @overload
    async def sitemaps(self, **params: Unpack[JumiaSitemapsDefaultParams]) -> JumiaSitemapsResponse: ...

class _AsyncJumiaGroup:
    @overload
    async def categories(self, **params: Unpack[JumiaCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[JumiaCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[JumiaCategoriesDefaultParams]) -> JumiaCategoriesResponse: ...
    @overload
    async def category(self, **params: Unpack[JumiaCategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def category(self, **params: Unpack[JumiaCategoryTextResponseParams]) -> str: ...
    @overload
    async def category(self, **params: Unpack[JumiaCategoryDefaultParams]) -> JumiaCategoryResponse: ...
    @overload
    async def countries(self, **params: Unpack[JumiaCountriesStreamParams]) -> BinaryIO: ...
    @overload
    async def countries(self, **params: Unpack[JumiaCountriesTextResponseParams]) -> str: ...
    @overload
    async def countries(self, **params: Unpack[JumiaCountriesDefaultParams]) -> JumiaCountriesResponse: ...
    @overload
    async def product(self, **params: Unpack[JumiaProductStreamParams]) -> BinaryIO: ...
    @overload
    async def product(self, **params: Unpack[JumiaProductTextResponseParams]) -> str: ...
    @overload
    async def product(self, **params: Unpack[JumiaProductDefaultParams]) -> JumiaProductResponse: ...
    @overload
    async def reviews(self, **params: Unpack[JumiaReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def reviews(self, **params: Unpack[JumiaReviewsTextResponseParams]) -> str: ...
    @overload
    async def reviews(self, **params: Unpack[JumiaReviewsDefaultParams]) -> JumiaReviewsResponse: ...
    @overload
    async def search(self, **params: Unpack[JumiaSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[JumiaSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[JumiaSearchDefaultParams]) -> JumiaSearchResponse: ...
    @overload
    async def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsStreamParams]) -> BinaryIO: ...
    @overload
    async def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsTextResponseParams]) -> str: ...
    @overload
    async def sitemap_urls(self, **params: Unpack[JumiaSitemapUrlsDefaultParams]) -> JumiaSitemapUrlsResponse: ...
    @overload
    async def sitemaps(self, **params: Unpack[JumiaSitemapsStreamParams]) -> BinaryIO: ...
    @overload
    async def sitemaps(self, **params: Unpack[JumiaSitemapsTextResponseParams]) -> str: ...
    @overload
    async def sitemaps(self, **params: Unpack[JumiaSitemapsDefaultParams]) -> JumiaSitemapsResponse: ...

JumiaCategoriesDefaultParams = TypedDict('JumiaCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'category': NotRequired[str],
}, total=False)

JumiaCategoriesTextResponseParams = TypedDict('JumiaCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'category': NotRequired[str],
}, total=False)

JumiaCategoriesStreamParams = TypedDict('JumiaCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'category': NotRequired[str],
}, total=False)

JumiaCategoryDefaultParams = TypedDict('JumiaCategoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'category': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaCategoryTextResponseParams = TypedDict('JumiaCategoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'category': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaCategoryStreamParams = TypedDict('JumiaCategoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'category': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaCountriesDefaultParams = TypedDict('JumiaCountriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

JumiaCountriesTextResponseParams = TypedDict('JumiaCountriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

JumiaCountriesStreamParams = TypedDict('JumiaCountriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

JumiaProductDefaultParams = TypedDict('JumiaProductDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': Required[str],
}, total=False)

JumiaProductTextResponseParams = TypedDict('JumiaProductTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': Required[str],
}, total=False)

JumiaProductStreamParams = TypedDict('JumiaProductStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': Required[str],
}, total=False)

JumiaReviewsDefaultParams = TypedDict('JumiaReviewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'sku': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaReviewsTextResponseParams = TypedDict('JumiaReviewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'sku': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaReviewsStreamParams = TypedDict('JumiaReviewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'sku': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaSearchDefaultParams = TypedDict('JumiaSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'q': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaSearchTextResponseParams = TypedDict('JumiaSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'q': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaSearchStreamParams = TypedDict('JumiaSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'q': Required[str],
    'page': NotRequired[int],
}, total=False)

JumiaSitemapUrlsDefaultParams = TypedDict('JumiaSitemapUrlsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'sitemap': Required[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

JumiaSitemapUrlsTextResponseParams = TypedDict('JumiaSitemapUrlsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'sitemap': Required[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

JumiaSitemapUrlsStreamParams = TypedDict('JumiaSitemapUrlsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'sitemap': Required[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

JumiaSitemapsDefaultParams = TypedDict('JumiaSitemapsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'type': NotRequired[Literal['products', 'brands', 'categories', 'mlps']],
}, total=False)

JumiaSitemapsTextResponseParams = TypedDict('JumiaSitemapsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'type': NotRequired[Literal['products', 'brands', 'categories', 'mlps']],
}, total=False)

JumiaSitemapsStreamParams = TypedDict('JumiaSitemapsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': Required[Literal['ci', 'eg', 'ke', 'ma', 'ng', 'sn']],
    'type': NotRequired[Literal['products', 'brands', 'categories', 'mlps']],
}, total=False)
