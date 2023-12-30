import requests
API_key = "15ba7226e758a452f3d686e47533baa3"


def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    responce = requests.get(url)
    data = responce.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data




if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
    print(get_image(filtered_data=get_data(place="Tokyo", forecast_days=2)))
