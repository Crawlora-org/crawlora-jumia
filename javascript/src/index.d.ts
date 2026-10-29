import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class JumiaClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categories(params: OperationParamsMap["jumia-categories"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  category(params: OperationParamsMap["jumia-category"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  countries(params?: OperationParamsMap["jumia-countries"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  product(params: OperationParamsMap["jumia-product"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  reviews(params: OperationParamsMap["jumia-reviews"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["jumia-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sitemapUrls(params: OperationParamsMap["jumia-sitemap-urls"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sitemaps(params: OperationParamsMap["jumia-sitemaps"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categories(params: OperationParamsMap["jumia-categories"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  category(params: OperationParamsMap["jumia-category"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  countries(params?: OperationParamsMap["jumia-countries"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  product(params: OperationParamsMap["jumia-product"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  reviews(params: OperationParamsMap["jumia-reviews"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["jumia-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sitemapUrls(params: OperationParamsMap["jumia-sitemap-urls"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sitemaps(params: OperationParamsMap["jumia-sitemaps"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  categories(...args: OperationRequestArgs<"jumia-categories">): Promise<OperationResponseMap["jumia-categories"]>;
  category(...args: OperationRequestArgs<"jumia-category">): Promise<OperationResponseMap["jumia-category"]>;
  countries(...args: OperationRequestArgs<"jumia-countries">): Promise<OperationResponseMap["jumia-countries"]>;
  product(...args: OperationRequestArgs<"jumia-product">): Promise<OperationResponseMap["jumia-product"]>;
  reviews(...args: OperationRequestArgs<"jumia-reviews">): Promise<OperationResponseMap["jumia-reviews"]>;
  search(...args: OperationRequestArgs<"jumia-search">): Promise<OperationResponseMap["jumia-search"]>;
  sitemapUrls(...args: OperationRequestArgs<"jumia-sitemap-urls">): Promise<OperationResponseMap["jumia-sitemap-urls"]>;
  sitemaps(...args: OperationRequestArgs<"jumia-sitemaps">): Promise<OperationResponseMap["jumia-sitemaps"]>;
}
export { JumiaClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default JumiaClient;
