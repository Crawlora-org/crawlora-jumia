# Jumia API endpoint reference and client usage

This reference lists all 8 public Jumia API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/jumia`, `crawlora-jumia`, and `crawlora-jumia` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Jumia locally; Crawlora is independent from and not endorsed by Jumia or its owners.

The package tracks the public API contract revision `sha256:ec487d49dce5bc76b62cd97844910f1b3def9fbc1e610492cc9432624f6ea6e4` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `jumia`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `categories` | `categories` | `jumia.categories` | `GET /jumia/categories` | `country` (query, required; values: `ci`, `eg`, `ke`, `ma`, `ng`, `sn`), `category` (query, optional) | List Jumia categories |
| `category` | `category` | `jumia.category` | `GET /jumia/category` | `country` (query, required; values: `ci`, `eg`, `ke`, `ma`, `ng`, `sn`), `category` (query, required), `page` (query, optional) | Browse a Jumia category |
| `countries` | `countries` | `jumia.countries` | `GET /jumia/countries` | — | List supported Jumia country storefronts |
| `product` | `product` | `jumia.product` | `GET /jumia/product` | `url` (query, required) | Get a Jumia product |
| `reviews` | `reviews` | `jumia.reviews` | `GET /jumia/reviews` | `country` (query, required; values: `ci`, `eg`, `ke`, `ma`, `ng`, `sn`), `sku` (query, required), `page` (query, optional) | Get the reviews of a Jumia product |
| `search` | `search` | `jumia.search` | `GET /jumia/search` | `country` (query, required; values: `ci`, `eg`, `ke`, `ma`, `ng`, `sn`), `q` (query, required), `page` (query, optional) | Search Jumia products |
| `sitemaps` | `sitemaps` | `jumia.sitemaps` | `GET /jumia/sitemaps` | `country` (query, required; values: `ci`, `eg`, `ke`, `ma`, `ng`, `sn`), `type` (query, optional; values: `products`, `brands`, `categories`, `mlps`) | List the sitemap files of a Jumia storefront |
| `sitemapUrls` | `sitemap_urls` | `jumia.sitemap_urls` | `GET /jumia/sitemap-urls` | `country` (query, required; values: `ci`, `eg`, `ke`, `ma`, `ng`, `sn`), `sitemap` (query, required), `page` (query, optional), `page_size` (query, optional) | Read the URLs in a Jumia sitemap file |

## Client forms

- JavaScript: import `JumiaClient` (also exported as `Client`) from `@crawlora-org/jumia`; use `new JumiaClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `JumiaClient` (also exported as `Client`) from `crawlora_jumia`; use `with JumiaClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncJumiaClient`, used with `async with` and `await`.
- Rust: add `crawlora-jumia` with Cargo; import `Client` and the generated operation parameter struct, then call `client.jumia.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-jumia/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
