# Jumia clients for Crawlora

Official Crawlora client packages for the hosted Jumia API. Access 8 API endpoints covering country and category discovery, product search, and product details from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Jumia locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Jumia or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/jumia`](javascript/README.md)
- Python: [`crawlora-jumia`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-jumia`](go.mod)
- Ruby: [`crawlora-jumia`](ruby/README.md)
- Java: [`net.crawlora:crawlora-jumia:0.1.0`](java/README.md)
- PHP: [`crawlora/jumia`](php/README.md)
- Rust: [`crawlora-jumia`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 8 selected public Jumia API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/jumia/categories` | `jumia-categories` | List Jumia categories |
| `GET` | `/jumia/category` | `jumia-category` | Browse a Jumia category |
| `GET` | `/jumia/countries` | `jumia-countries` | List supported Jumia country storefronts |
| `GET` | `/jumia/product` | `jumia-product` | Get a Jumia product |
| `GET` | `/jumia/reviews` | `jumia-reviews` | Get the reviews of a Jumia product |
| `GET` | `/jumia/search` | `jumia-search` | Search Jumia products |
| `GET` | `/jumia/sitemap-urls` | `jumia-sitemap-urls` | Read the URLs in a Jumia sitemap file |
| `GET` | `/jumia/sitemaps` | `jumia-sitemaps` | List the sitemap files of a Jumia storefront |

## License

MIT. See [LICENSE](LICENSE).
