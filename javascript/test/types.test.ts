import { JumiaClient } from "../src/index.js";

const client = new JumiaClient({ apiKey: "test-key" });
void client.categories({"country": "ci"});
void client.request("jumia-categories", {"country": "ci"});
const streamResponse: Promise<Response> = client.request("jumia-categories", {"country": "ci"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("jumia-categories", {"country": "ci"}, { responseType: "stream" });
const directStream: Promise<Response> = client.categories({"country": "ci"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("jumia-categories", {"country": "ci", "category": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("jumia-categories", {"country": "ci"}, { responseType: "text" });
void rawText;


void client.countries();
void client.request("jumia-countries");
// @ts-expect-error The selected operation requires its documented params.
void client.categories();
