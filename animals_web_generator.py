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

def generate_html_string(data):
    html_string = ""
    for animal in data:
        name = animal['name']
        html_string += f"Name: {name}\n"

        if 'diet' in animal['characteristics'].keys():
            diet = animal['characteristics']['diet']
            html_string += f"Diet: {diet}\n"

        locations = animal['locations']
        locations = ", ".join(locations)
        html_string += f"Location: {locations}\n"

        if 'type' in animal['characteristics'].keys():
            animal_type = animal['characteristics']['type']
            html_string += f"Type: {animal_type}\n\n"

    return html_string

def manipulate_html_file(html_string):
    with open('animals_template.html', 'r') as file:
        content = file.read()

    content = content.replace("__REPLACE_ANIMALS_INFO__", html_string)

    with open('animals_template.html', 'w') as file:
        file.write(content)

def main():
    data = load_data()
    html_string = generate_html_string(data)
    manipulate_html_file(html_string)


if __name__ == '__main__':
    main()