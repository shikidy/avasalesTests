import requests
import json


def start_search(date_start: str = "2023-06-01", date_end: str = "2023-06-01", adult_count: int = 1) -> int:
    
    url = "https://tickets-api.aviasales.ru/search/v2/start"

    payload = json.dumps({
      "search_params": {
        "directions": [
          {
            "origin": "KZN",
            "destination": "MOW",
            "date": date_start
          },
          {
            "origin": "MOW",
            "destination": "KZN",
            "date": date_end
          }
        ],
        "passengers": {
          "adults": adult_count,
          "children": 0,
          "infants": 0
        },
        "trip_class": "Y"
      },
      "client_features": {
        "direct_flights": True,
        "brand_ticket": True,
        "top_filters": True,
        "badges": True,
        "tour_tickets": True,
        "assisted": True
      },
      "marker": "google",
      "market_code": "ru",
      "citizenship": "RU",
      "currency_code": "rub",
      "languages": {
        "ru": 1
      },
      "debug": {
        "experiment_groups": {
          "serp-exp-newProposalModal": "on",
          "ex-exp-seleneForm": "off",
          "ex-exp-monthsInCalendar": "off",
          "serp-exp-transferUpsale": "on",
          "avs-exp-downgradedGates": "on",
          "ex-exp-mainContentPrices": "showPrices",
          "serp-exp-travelRestrictions": "on",
          "avs-exp-foreignCards": "on",
          "serp-exp-softFilters": "on",
          "avs-exp-comparisonWidget": "on",
          "guides-exp-feed": "on",
          "serp-exp-pinFlight": "on",
          "serp-exp-versusDrawer": "on",
          "usc-exp-menuSupportSection": "on",
          "guides-exp-trapHeader": "expanded_top",
          "serp-exp-ticketProductBanner": "on",
          "avs-exp-aa": "on",
          "usc-exp-emailSubscriptionForm": "footer_form",
          "prem-exp-newMarketsMain": "off",
          "serp-exp-yandexHotels": "off",
          "serp-exp-baggageUpsale": "on",
          "serp-exp-scoring": "on",
          "serp-exp-modalDirectFlights": "off",
          "serp-exp-hotels": "on_prod_without_entry_points",
          "serp-exp-marketingOperatingCarrier": "on"
        }
      },
      "brand": "AS"
    })
    headers = {
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
      'content-type': 'application/json',
      'referer': 'https://www.aviasales.ru/',
      'x-client-type': 'web',
    
      'x-origin-cookie': '_awt=d6646639663b5fc32d66d36685b63568362d3586-f3aa5039633433e63396617f033c614666983b83; '
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.status_code

assert start_search() == 200, "Test: site works"
print("Test 1 passed")
assert start_search(date_start="2022-06-01") == 400, "Test: search date in past"
print("Test 2 passed. TestCase 2")
assert start_search(adult_count=10) == 400, "Test: adult must be <10"
print("Test 3 passed. TestCase 3")
assert start_search(adult_count=0) == 400, "Test: adult must be >0"
print("Test 4 passed. TestCase 3")

print("All tests passed")

