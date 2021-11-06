import json


def parse_dict(content):
    new_dict = {}

    for key in content:
        # print(key, type(content[key]))

        if content[key] is None or content[key] == "undefined":
            continue
        elif type(content[key]) is dict:
            edited = parse_dict(content[key])
            new_dict[key] = edited
        elif type(content[key]) is list:
            # print("Imma list", content[key])

            new_list = []
            for list_item in content[key]:
                # print(type(list_item), list_item)
                if type(list_item) is dict:
                    # print("I'm in here")
                    edited = parse_dict(list_item)
                    # print(edited)
                    new_list.append(edited)
                else:
                    new_list.append(list_item)
            new_dict[key] = new_list
        else:
            new_dict[key] = string_to_num(content[key])

    return new_dict


def string_to_num(input):
    if type(input) is str:
        if '.' in input:
            return float(input)
        elif str(input).isdigit():
            return int(input)
        elif '-' in input:
            return int(input)

    return input


def main():

    with open("input.json") as file:
        content = json.load(file)

    result_dict = parse_dict(content)
    # print(result_dict)

    result_json = json.dumps(result_dict, indent=4)
    print(result_json)

    with open("output.json", 'w') as file:
        file.write(result_json)


if __name__ == "__main__":
    main()
