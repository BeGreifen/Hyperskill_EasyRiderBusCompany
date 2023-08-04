# Write your code here
import json
import logging
import inspect


def logger(func):
    def wrap(*args, **kwargs):
        logging.info(
            f"{func.__name__} - line no: {inspect.getframeinfo(inspect.currentframe().f_back).lineno} with args: {args}, kwargs: {kwargs}")
        # Log the function name and arguments

        # Call the original function
        result = func(*args, **kwargs)

        # Log the return value
        logging.info(f"{func.__name__} returned: {result}")

        # Return the result
        return result

    return wrap


@logger
def check_doc_list(list_of_buses: list) -> dict:
    """
        Check a list of dictionaries representing buses and count missing elements or incorrectly formatted values.

        The function takes a list of dictionaries, where each dictionary represents a bus with specific keys
        such as 'bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', and 'a_time'. It iterates through
        each bus dictionary and counts the missing elements or incorrectly formatted values for certain keys.

        - For 'bus_id', 'stop_id', and 'next_stop' keys, the function checks if the values are of type int.
        - For 'stop_name', 'stop_type', and 'a_time' keys, the function checks if the values are of type str.
          Additionally, it counts an empty string for 'stop_name' and 'stop_type' keys as a missing element.
          For 'stop_type' key, it also counts any string longer than one character as an incorrectly formatted value.

        Args:
            list_of_buses (list): A list of dictionaries, where each dictionary represents a bus.

        Returns:
            dict: A dictionary containing the count of missing elements or incorrectly formatted values for each key.
                  The keys of the dictionary are: 'bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', and 'a_time'.
                  The values are integers representing the count of missing elements or incorrect values for each key.
        """
    result_dict: dict = {"bus_id": 0,
                         "stop_id": 0,
                         "stop_name": 0,
                         "next_stop": 0,
                         "stop_type": 0,
                         "a_time": 0}
    for bus in list_of_buses:
        for key, value in bus.items():
            if key in ("bus_id", "stop_id", "next_stop"):
                if not isinstance(value, int):
                    result_dict[key] += 1
            else:
                if not isinstance(value, str):
                    result_dict[key] += 1
                elif value == "" and key not in "stop_type":
                    result_dict[key] += 1
                elif key in "stop_type" and len(value)>1:
                    result_dict[key] += 1
    return result_dict


def main():
    """
        Main function to test the check_doc_list function with JSON-formatted input.

        The function takes JSON-formatted input representing a list of bus data. It then calls the check_doc_list
        function to validate and count the errors in the data. The function prints the overall number of errors
        and the count of errors for each key.

        Example Input (as JSON):
        [{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": 8.12},
         {"bus_id": 128, "stop_id": 3, "stop_name": "", "next_stop": 5, "stop_type": "", "a_time": "08:19"},
         {"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"}]

        Output:
        Type and required field validation: 2 errors
        bus_id: 0
        stop_id: 0
        stop_name: 1
        next_stop: 0
        stop_type: 1
        a_time: 0
        """
    bus_list = json.loads(input())
    res = check_doc_list(bus_list)
    sum_errors = sum(res.values())
    print(f"Type and required field validation: {sum_errors} errors")
    for key, value in res.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='app.log',  # Specify the file name for logging
                        filemode='w'  # Use 'w' mode to overwrite the log file on each run, or 'a' to append
                        )
    logging.info("**** solution started ****")
    main()
