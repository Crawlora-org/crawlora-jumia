# Crawlora Jumia API client for PHP (`crawlora/jumia`)

This PHP package calls Crawlora's hosted Jumia API at `https://api.crawlora.net/api/v1`. It exposes 8 endpoints covering country and category discovery, product search, and product details. It does not call or scrape Jumia directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/jumia
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Jumia\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("jumia-search", ['country' => 'ci', 'q' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 8 API operations.

## Supported Jumia API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-jumia/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-jumia). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-jumia/blob/main/docs/usage.md).
