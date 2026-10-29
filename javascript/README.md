# @crawlora-org/jumia — Jumia API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Jumia API.
It exposes 8 API endpoints for country and category discovery, product search, and product details through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-javascript-homepage). It does not run a browser or scrape Jumia locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Jumia or its owners.

## Install

```sh
npm install @crawlora-org/jumia
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { JumiaClient } from "@crawlora-org/jumia";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new JumiaClient({ apiKey });
const result1 = await client.countries({});
console.log(result1);
const result2 = await client.search({ country: "ng", q: "phone" });
console.log(result2);
```

The client also exports `Client` as an alias for `JumiaClient`. Operation
methods are available directly in camelCase and through the `jumia`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-jumia/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-jumia/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Jumia API endpoints

This package exposes each route below as a direct method and through the `jumia` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-jumia/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
