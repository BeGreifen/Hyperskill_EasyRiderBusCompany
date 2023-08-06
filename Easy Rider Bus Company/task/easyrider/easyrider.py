# Write your code here
import logging
import inspect
import json
import re


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


# @logger
def check_military_time(str_time: str) -> bool:
    """
    Check if the input string represents a valid military time format (24-hour format).

    Parameters:
        str_time (str): The input string representing the time in the format 'hh:mm'.

    Returns:
        bool: True if the input string is a valid military time format, otherwise False.

    Military Time Format (24-hour format):
    - The time should have two digits for hours, followed by a colon ':', and then two digits for minutes.
    - The first digit of hours should be 0 or 1.
    - Hours less than 10 should have a leading zero, e.g., '08:34'.
    - The delimiter between hours and minutes should be a colon ':'.
    - The minutes should be between 00 and 59.

    Examples:
        check_military_time("08:34")  # True
        check_military_time("14:45")  # True
        check_military_time("3:15")   # False (invalid hour)
        check_military_time("18:60")  # False (invalid minute)
        check_military_time("09-20")  # False (invalid delimiter)
    """
    # Define the regex pattern for military time format
    pattern = r'^[01]\d:[0-5]\d$'

    # Use re.match() to check if the input string matches the pattern
    match = re.match(pattern, str_time)

    # Return True if there's a match, otherwise False
    return match is not None


# @logger
def check_stop_name_in_list(stop_name:str) -> bool:
    """
    Check if the given stop_name exists in a predefined list of valid stop names.

    Parameters:
        stop_name (str): The stop name to be checked for validity.

    Returns:
        bool: True if the stop_name exists in the predefined list, otherwise False.

    Predefined List of Valid Stop Names:
    - The function checks if the given stop_name is present in a predefined set of valid stop names.
    - The list_stop_names set contains strings representing valid stop names, including their suffixes.

    Examples:
        check_stop_name_in_list("Sesame Street")   # True
        check_stop_name_in_list("Fifth Avenue")    # True
        check_stop_name_in_list("Sunset Boulevard")# True
        check_stop_name_in_list("Elm Street")      # True
        check_stop_name_in_list("Broadway Avenue") # False (not in the predefined list)
        check_stop_name_in_list("Pilotow Street")  # True
    """
    list_stop_names = {"Sesame Street", "Fifth Avenue", "Sunset Boulevard", "Elm Street",
                       "Bourbon Street", "Prospekt Avenue", "Pilotow Street"}
    return stop_name in list_stop_names


# @logger
def check_stop_name(stop_name: str) -> bool:
    """
    Check if the given stop_name has a valid suffix and a valid prefix.

    Parameters:
        stop_name (str): The stop name to be checked for validity.

    Returns:
        bool: True if the stop_name has a valid suffix and a valid prefix, otherwise False.

    Valid Suffix and Prefix:
    - The function uses regular expressions to check if the stop_name has a valid suffix and a valid prefix.
    - The valid_suffix_pattern checks for a space followed by one of the valid suffix options ('Road', 'Avenue', 'Boulevard', 'Street') at the end of the stop_name.
    - The valid_prefix_pattern checks for a string that starts with an uppercase letter and is followed by one or more letters or spaces.

    Examples:
        check_stop_name("Sesame Street")   # True
        check_stop_name("Fifth Avenue")    # True
        check_stop_name("Fifth Av.")       # False (invalid suffix)
        check_stop_name("Elm")            # False (missing valid suffix)
        check_stop_name("street Sesame")  # False (invalid prefix)
    """
    # Define the regex patterns for valid suffix and valid prefix
    valid_suffix_pattern = r' (Road|Avenue|Boulevard|Street)$'
    valid_prefix_pattern = r'^[A-Z][a-zA-Z\s]+'

    # Check for a valid suffix using re.search()
    has_valid_suffix = bool(re.search(valid_suffix_pattern, stop_name))

    # Check for a valid prefix using re.match()
    has_valid_prefix = bool(re.match(valid_prefix_pattern, stop_name))

    # Return True if both valid suffix and valid prefix are present, otherwise False
    return has_valid_suffix and has_valid_prefix


# @logger
def check_stop_type(stop_type:str) -> bool:
    """
    Check if the given stop_type is a valid stop type.

    Parameters:
        stop_type (str): The stop type to be checked for validity.

    Returns:
        bool: True if the stop_type is a valid stop type, otherwise False.

    Valid Stop Types:
    - The function checks if the given stop_type is present in a predefined set of valid stop types.
    - The list_stop_types set contains valid stop types, including the empty string '', 'S' (Station),
      'O' (Outbound), and 'F' (Flag Stop).

    Examples:
        check_stop_type("")  # True (empty string is a valid stop type)
        check_stop_type("S") # True ('S' is a valid stop type)
        check_stop_type("O") # True ('O' is a valid stop type)
        check_stop_type("F") # True ('F' is a valid stop type)
        check_stop_type("P") # False ('P' is not a valid stop type)
    """
    list_stop_types = {"", "S", "O", "F"}
    return stop_type in list_stop_types


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
                elif key in "stop_type" and len(value) > 1:
                    result_dict[key] += 1
                elif key in "stop_type" and not check_stop_type(value):
                    result_dict[key] += 1
                elif key in "a_time" and not check_military_time(value):
                    result_dict[key] += 1
                elif key in "stop_name" and not check_stop_name(value):
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

        Output: (only report stop_name, stop_type, a_time)
        Type and required field validation: 2 errors
        stop_name: 1
        stop_type: 1
        a_time: 0
        """
    bus_list = json.loads(input())
    res = check_doc_list(bus_list)
    sum_errors = sum(res.values())
    print(f"Type and required field validation: {sum_errors} errors")
    for key, value in res.items():
        if key in ("stop_name","stop_type","a_time"):
            print(f"{key}: {value}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='app.log',  # Specify the file name for logging
                        filemode='w'  # Use 'w' mode to overwrite the log file on each run, or 'a' to append
                        )
    logging.info("**** solution started ****")
    main()
