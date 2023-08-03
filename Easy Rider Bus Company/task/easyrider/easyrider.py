# Write your code here
import json


def check_doc_list(doc: list) -> dict:
    result_dict: dict = {"bus_id": 0,
                         "stop_id": 0,
                         "stop_name": 0,
                         "next_stop": 0,
                         "stop_type": 0,
                         "a_time": 0}
    for elem in doc:
        for key, value in elem.items():
            if key in ("bus_id", "stop_id", "next_stop"):
                if not isinstance(value, int):
                    result_dict[key] += 1
            else:
                if not isinstance(value, str) or value == "":
                    result_dict[key] += 1
    return result_dict


def dummy_input() -> str:
    json_data = '''
    [
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": 8.12
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": "",
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": ""
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": "0",
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": "512",
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": 5,
        "a_time": "08:16"
    }
    ]'''
    return json_data


def main():
    doc_list = json.loads(dummy_input())
    # doc_list = json.loads(input())
    res = check_doc_list(doc_list)
    sum_errors = sum(res.values())
    print(f"Type and required field validation: {sum_errors} errors")
    for key, value in res.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
