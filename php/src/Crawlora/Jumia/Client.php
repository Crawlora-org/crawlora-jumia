<?php

declare(strict_types=1);

namespace Crawlora\Jumia;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'jumia';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 8;
    public const OPERATION_IDS = ["jumia-categories", "jumia-category", "jumia-countries", "jumia-product", "jumia-reviews", "jumia-search", "jumia-sitemap-urls", "jumia-sitemaps"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"jumia-categories": {"bodyParam": null, "bodyRequired": false, "id": "jumia-categories", "method": "GET", "params": [{"description": "Jumia country storefront", "enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string", "x-example": "ng"}, {"description": "Category slug whose sub-categories to list; omit for top-level departments", "in": "query", "name": "category", "type": "string", "x-example": "phones-tablets"}], "path": "/jumia/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string"}, {"in": "query", "name": "category", "type": "string"}], "security": ["ApiKeyAuth"]}, "jumia-category": {"bodyParam": null, "bodyRequired": false, "id": "jumia-category", "method": "GET", "params": [{"description": "Jumia country storefront", "enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string", "x-example": "ng"}, {"description": "Category slug from jumia-categories", "in": "query", "name": "category", "required": true, "type": "string", "x-example": "phones-tablets"}, {"default": 1, "description": "1-based result page, 1 to 50", "in": "query", "maximum": 50, "minimum": 1, "name": "page", "type": "integer"}], "path": "/jumia/category", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string"}, {"in": "query", "name": "category", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "jumia-countries": {"bodyParam": null, "bodyRequired": false, "id": "jumia-countries", "method": "GET", "params": [], "path": "/jumia/countries", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "jumia-product": {"bodyParam": null, "bodyRequired": false, "id": "jumia-product", "method": "GET", "params": [{"description": "Absolute Jumia product URL from a search or category result", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https://www.jumia.com.ng/samsung-galaxy-a07-6.7-4gb-ram128gbgb-rom-black-418619812.html"}], "path": "/jumia/product", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "jumia-reviews": {"bodyParam": null, "bodyRequired": false, "id": "jumia-reviews", "method": "GET", "params": [{"description": "Jumia country storefront", "enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string", "x-example": "ng"}, {"description": "Product sku", "in": "query", "name": "sku", "required": true, "type": "string", "x-example": "SA948MP6Z6LPDNAFAMZ"}, {"default": 1, "description": "1-based page of reviews, 10 per page", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/jumia/reviews", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string"}, {"in": "query", "name": "sku", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "jumia-search": {"bodyParam": null, "bodyRequired": false, "id": "jumia-search", "method": "GET", "params": [{"description": "Jumia country storefront", "enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string", "x-example": "ng"}, {"description": "Product search keyword", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "wireless earbuds"}, {"default": 1, "description": "1-based result page, 1 to 50", "in": "query", "maximum": 50, "minimum": 1, "name": "page", "type": "integer"}], "path": "/jumia/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string"}, {"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "jumia-sitemap-urls": {"bodyParam": null, "bodyRequired": false, "id": "jumia-sitemap-urls", "method": "GET", "params": [{"description": "Jumia country storefront", "enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string", "x-example": "ng"}, {"description": "Sitemap file name from jumia-sitemaps", "in": "query", "name": "sitemap", "required": true, "type": "string", "x-example": "products-sitemap-9.xml.gz"}, {"default": 1, "description": "1-based page of URLs", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"default": 1000, "description": "URLs per page", "in": "query", "maximum": 5000, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/jumia/sitemap-urls", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string"}, {"in": "query", "name": "sitemap", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "jumia-sitemaps": {"bodyParam": null, "bodyRequired": false, "id": "jumia-sitemaps", "method": "GET", "params": [{"description": "Jumia country storefront", "enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string", "x-example": "ng"}, {"description": "Only list one kind of sitemap", "enum": ["products", "brands", "categories", "mlps"], "in": "query", "name": "type", "type": "string"}], "path": "/jumia/sitemaps", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["ci", "eg", "ke", "ma", "ng", "sn"], "in": "query", "name": "country", "required": true, "type": "string"}, {"enum": ["products", "brands", "categories", "mlps"], "in": "query", "name": "type", "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-jumia-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("jumia-categories", $params, $responseType);
    }
    public function category(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("jumia-category", $params, $responseType);
    }
    public function countries(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("jumia-countries", $params, $responseType);
    }
    public function product(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("jumia-product", $params, $responseType);
    }
    public function reviews(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("jumia-reviews", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("jumia-search", $params, $responseType);
    }
    public function sitemap_urls(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("jumia-sitemap-urls", $params, $responseType);
    }
    public function sitemaps(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("jumia-sitemaps", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
