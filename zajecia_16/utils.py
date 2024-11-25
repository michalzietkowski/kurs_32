import requests

def retrieve_data_from_api(country_name):
    url_address = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
    response = requests.get(url_address)
    if response.status_code == 200:
        print("Udalo sie pobrac dane")
        return parse_data_from_api(response.json())
    else:
        print(response.json())
        print("Nie udało się pobrać danych z API")

def parse_data_from_api(response_text):
    return {
        "nazwa": response_text[0].get("name").get("common"),
        "stolica": response_text[0].get("capital"),
        "region": response_text[0].get("region"),
        "podregion": response_text[0].get("subregion"),
        "populacja": response_text[0].get("population"),
        "jezyki_urzedowe": response_text[0].get("languages"),
        "flaga": response_text[0].get("flag")
    }
