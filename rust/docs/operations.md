# Crawlora Jumia Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `8`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| jumia | `jumia.categories` | `jumia-categories` | `GET /jumia/categories` | `country` (query String enum{ci, eg, ke, ma, ng, sn} required)<br>`category` (query String) | `ApiKeyAuth` | `JumiaCategoriesResponse` |  |
| jumia | `jumia.category` | `jumia-category` | `GET /jumia/category` | `country` (query String enum{ci, eg, ke, ma, ng, sn} required)<br>`category` (query String required)<br>`page` (query i64) | `ApiKeyAuth` | `JumiaCategoryResponse` |  |
| jumia | `jumia.countries` | `jumia-countries` | `GET /jumia/countries` | none | `ApiKeyAuth` | `JumiaCountriesResponse` |  |
| jumia | `jumia.product` | `jumia-product` | `GET /jumia/product` | `url` (query String required) | `ApiKeyAuth` | `JumiaProductResponse` |  |
| jumia | `jumia.reviews` | `jumia-reviews` | `GET /jumia/reviews` | `country` (query String enum{ci, eg, ke, ma, ng, sn} required)<br>`sku` (query String required)<br>`page` (query i64) | `ApiKeyAuth` | `JumiaReviewsResponse` |  |
| jumia | `jumia.search` | `jumia-search` | `GET /jumia/search` | `country` (query String enum{ci, eg, ke, ma, ng, sn} required)<br>`q` (query String required)<br>`page` (query i64) | `ApiKeyAuth` | `JumiaSearchResponse` |  |
| jumia | `jumia.sitemap_urls` | `jumia-sitemap-urls` | `GET /jumia/sitemap-urls` | `country` (query String enum{ci, eg, ke, ma, ng, sn} required)<br>`sitemap` (query String required)<br>`page` (query i64)<br>`page_size` (query i64) | `ApiKeyAuth` | `JumiaSitemapUrlsResponse` |  |
| jumia | `jumia.sitemaps` | `jumia-sitemaps` | `GET /jumia/sitemaps` | `country` (query String enum{ci, eg, ke, ma, ng, sn} required)<br>`type` (query String enum{products, brands, categories, mlps}) | `ApiKeyAuth` | `JumiaSitemapsResponse` |  |
