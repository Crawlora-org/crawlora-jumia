import { JumiaClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new JumiaClient({ apiKey });

  const countries = await client.countries({  });
  console.log("countries", countries);
  const search = await client.search({ country: "ng", q: "phone" });
  console.log("search", search);
