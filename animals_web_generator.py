import json


def load_data():
    with open('animals_data.json', 'r') as file:
        data = json.load(file)
        return data

def display_data(data):
    for animal in data:
        name = animal['name']
        print(f"Name: {name}")

        if 'diet' in animal['characteristics'].keys():
            diet = animal['characteristics']['diet']
            print(f"Diet: {diet}")

        locations = animal['locations']
        locations = ", ".join(locations)
        print(f"Location: {locations}")

        if 'type' in animal['characteristics'].keys():
            animal_type = animal['characteristics']['type']
            print(f"Type: {animal_type}")

        print()

def main():
    data = load_data()
    display_data(data)


if __name__ == '__main__':
    main()