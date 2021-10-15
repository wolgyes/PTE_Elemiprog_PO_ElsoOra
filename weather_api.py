import requests
APPID = "ed90f55a39c99f5d99b24736fb3700dc"

def legmelegebb_hidegebb_varos(tempv):
    tmp = tempv
    for varos, temp in tmp.items():
        tmp[varos] = temp_keres(varos)

    max = tmp["Pécs"]
    max_varos = "Pécs"
    minimum = tmp["Pécs"]
    minimum_varos = "Pécs"
    for varos, temp in tmp.items():
        if max < tmp[varos]:
            max = tmp[varos]
            max_varos = varos
        if minimum > tmp[varos]:
            minimum = tmp[varos]
            minimum_varos = varos

    print("A legmelegebb " + max_varos, str(max) + "C")
    print("A leghidegebb " + minimum_varos, str(minimum) + "C")

def temp_keres(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APPID}"
    r = requests.get(url)
    temp = r.json()["main"]["temp"]
    return kelvin_to_C(temp)

def kelvin_to_C(temp):
    return round(temp - 273.15)


if __name__ == '__main__':
    print("cica weather")