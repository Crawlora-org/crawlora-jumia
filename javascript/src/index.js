import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class JumiaClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-jumia-js/0.1.0" });
    this["categories"] = (...args) => this.request("jumia-categories", ...args);
    this["category"] = (...args) => this.request("jumia-category", ...args);
    this["countries"] = (...args) => this.request("jumia-countries", ...args);
    this["product"] = (...args) => this.request("jumia-product", ...args);
    this["reviews"] = (...args) => this.request("jumia-reviews", ...args);
    this["search"] = (...args) => this.request("jumia-search", ...args);
    this["sitemapUrls"] = (...args) => this.request("jumia-sitemap-urls", ...args);
    this["sitemaps"] = (...args) => this.request("jumia-sitemaps", ...args);
  }
}

export { JumiaClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default JumiaClient;
