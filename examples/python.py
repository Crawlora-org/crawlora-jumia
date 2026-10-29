import os

from crawlora_jumia import JumiaClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with JumiaClient(api_key=api_key) as client:
    countries = client.countries()
    print('countries', countries)
    search = client.search(country='ng', q='phone')
    print('search', search)
