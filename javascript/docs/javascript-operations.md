# Crawlora Jumia JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `8`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| jumia | `jumia.categories` | `jumia-categories` | `GET /jumia/categories` | `country` (query "ci" \| "eg" \| "ke" \| "ma" \| "ng" \| "sn" required)<br>`category` (query string) | `ApiKeyAuth` | `JumiaCategoriesResponse` |  |
| jumia | `jumia.category` | `jumia-category` | `GET /jumia/category` | `country` (query "ci" \| "eg" \| "ke" \| "ma" \| "ng" \| "sn" required)<br>`category` (query string required)<br>`page` (query number) | `ApiKeyAuth` | `JumiaCategoryResponse` |  |
| jumia | `jumia.countries` | `jumia-countries` | `GET /jumia/countries` | none | `ApiKeyAuth` | `JumiaCountriesResponse` |  |
| jumia | `jumia.product` | `jumia-product` | `GET /jumia/product` | `url` (query string required) | `ApiKeyAuth` | `JumiaProductResponse` |  |
| jumia | `jumia.reviews` | `jumia-reviews` | `GET /jumia/reviews` | `country` (query "ci" \| "eg" \| "ke" \| "ma" \| "ng" \| "sn" required)<br>`sku` (query string required)<br>`page` (query number) | `ApiKeyAuth` | `JumiaReviewsResponse` |  |
| jumia | `jumia.search` | `jumia-search` | `GET /jumia/search` | `country` (query "ci" \| "eg" \| "ke" \| "ma" \| "ng" \| "sn" required)<br>`q` (query string required)<br>`page` (query number) | `ApiKeyAuth` | `JumiaSearchResponse` |  |
| jumia | `jumia.sitemapUrls` | `jumia-sitemap-urls` | `GET /jumia/sitemap-urls` | `country` (query "ci" \| "eg" \| "ke" \| "ma" \| "ng" \| "sn" required)<br>`sitemap` (query string required)<br>`page` (query number)<br>`page_size` (query number) | `ApiKeyAuth` | `JumiaSitemapUrlsResponse` |  |
| jumia | `jumia.sitemaps` | `jumia-sitemaps` | `GET /jumia/sitemaps` | `country` (query "ci" \| "eg" \| "ke" \| "ma" \| "ng" \| "sn" required)<br>`type` (query "products" \| "brands" \| "categories" \| "mlps") | `ApiKeyAuth` | `JumiaSitemapsResponse` |  |
