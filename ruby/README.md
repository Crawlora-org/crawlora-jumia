# Crawlora Jumia API client for Ruby (`crawlora-jumia`)

This Ruby gem calls Crawlora's hosted Jumia API at `https://api.crawlora.net/api/v1`. It exposes 8 endpoints covering country and category discovery, product search, and product details; it does not call or scrape Jumia directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-jumia"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/jumia"

client = Crawlora::Jumia::Client.new
result = client.request("jumia-search", JSON.parse("{\"country\": \"ci\", \"q\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 8 API operations.

```ruby
client = Crawlora::Jumia::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Jumia API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-jumia/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-jumia) for account setup, the API operation reference, and release history.
