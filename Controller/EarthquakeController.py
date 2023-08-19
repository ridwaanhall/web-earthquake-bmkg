import requests

class ReadUrl:
    def read_json(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

class INA_TEWS:
    def news(self):
        reader = ReadUrl()
        json_data = reader.read_json('https://earthquaqe-bmkg-api.ridwaanhall.repl.co/new.json')
        return json_data

    def maps(self):
        reader = ReadUrl()
        json_data = reader.read_json('https://earthquaqe-bmkg-api-v1.ridwaanhall.repl.co/new.json')
        coordinates_str = json_data["info"]["point"]["coordinates"]
        headline = json_data['info']['headline']
        longitude, latitude = map(float, coordinates_str.split(','))
        return longitude, latitude, headline

    def live30event(self):
        reader = ReadUrl()
        json_data = reader.read_json('https://earthquaqe-bmkg-api.ridwaanhall.repl.co/live30event.json')
        return json_data


class BMKG_Data:
    def news(self):
        reader = ReadUrl()
        json_data = reader.read_json('https://earthquake-bmkg-api.ridwaanhall.repl.co/autogempa.json')
        return json_data

    def maps(self):
        reader = ReadUrl()
        json_data = reader.read_json('https://earthquaqe-bmkg-api-v1.ridwaanhall.repl.co/autogempa.json')
        coordinates_str = json_data["Infogempa"]["gempa"]["point"]["coordinates"]
        latitude, longitude = map(float, coordinates_str.split(','))
        return latitude, longitude