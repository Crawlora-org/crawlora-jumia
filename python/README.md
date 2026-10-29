# crawlora-jumia — Jumia API client for Python

Python client for Crawlora's hosted Jumia API. It exposes 8 API endpoints covering country and category discovery, product search, and product details. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-python-homepage); the package does not run a browser or scrape
Jumia locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Jumia or its owners.

## Install

```sh
python -m pip install crawlora-jumia
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_jumia import JumiaClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with JumiaClient(api_key=api_key) as client:
    result_1 = client.countries()
    print(result_1)
    result_2 = client.search(country='ng', q='phone')
    print(result_2)
```

The package also exports `Client` as an alias for `JumiaClient`. Operation
methods are available directly in snake_case and through the `jumia`
group. The async package client is `AsyncJumiaClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-jumia/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-jumia/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_jumia import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.countries()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-jumia/blob/main/examples/python.py) for a complete usage example.

## Supported Jumia API endpoints

This package exposes every route below through direct snake_case methods and the `jumia` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-jumia/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
