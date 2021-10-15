import weather_api
import json


if __name__ == '__main__':
    with open("varosok.json", "r") as file:
        varosok = json.load(file)

    weather_api.legmelegebb_hidegebb_varos(varosok)

    with open("varosok.json", "w") as file:
        file.write(json.dumps(varosok, indent=4, sort_keys=True))



