import datetime
import os

FILENAME = "calendar.txt"
'''

IMPORTANT NOTE: Do NOT change any of the function names or their signatures
(the parameters they take).
Your functions must behave exactly as described. Please check correctness by
running DocTests  included in function headers. You may not use any print or
input statements in your code.

Manage a calendar database.

A calendar is a dictionary keyed by date ("YYYY-MM-DD") with value being a list
of strings, the events on the specified date.

'''


# -----------------------------------------------------------------------------
# Please implement the following calendar commands
# -----------------------------------------------------------------------------

def command_help():
    """
    () -> str
    This function is already implemented. Please do not change it.
    Returns a help message for the system. That is...
    """

    help_me = """
    Help for Calendar. The calendar commands are

    add DATE START END DETAILS               add the event DETAILS at the specified DATE with specific START and END time
    show                                     show all events in the calendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from
                                   the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user data follows command:

    command: add 2018-10-12 18 19 dinner with jane
    success

    command: show
        2018-10-12 : 
            start : 08:00, 
			end : 09:00,
			title : Eye doctor
			
            start : 12:30,
			end : 13:00,
			title : lunch with sid
            
			start : 18:00,
			end : 19:00, 
			title : dinner with jane
        2018-10-29 : 
            start : 10:00,
			end : 11:00,
			title : Change oil in blue car
			
            start : 12:00,
			end : 14:00,
			title : Fix tree near front walkway
			
            start : 18:00,
			end : 19:00,
			title : Get salad stuff, leuttice, red peppers, green peppers
        2018-11-06 : 
            start : 18:00,
			end : 22:00,
			title : Sid's birthday

    command: delete 2018-10-29 10
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2018-12-21
    2016-01-02

    START and END has a format HH where HH is an hour in 24h format, for example
    09
    21

    Event DETAILS consist of alphabetic characters,
    no tabs or newlines allowed.
    """
    return help_me


def command_add(date, start_time, end_time, title, calendar):
    """
    (str, int, int, str, dict) -> boolean
    Add title to the list at calendar[date]
    Create date if it was not there
    Adds the date if start_time is less or equal to the end_time

    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer from 0-23 representing the start time
    end_time: An integer from 0-23 representing the start time
    title: A string describing the event
    calendar: The calendar database
    return: boolean of whether the even was successfully added

    >>> calendar = {}
    >>> command_add(" ", 11, 12, "Python class", calendar)
    True

    >>> command_add(" ", 13, 14, "CCNA class", calendar)
    True

    >>> calendar.clear()
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True

    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True

    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True

    >>> command_add("2018-03-11", 10, 9, "go out with friends after test", calendar)
    False
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True

    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], \
    "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True


    """

    # YOUR CODE GOES HERE
    if start_time > end_time:
        return False
    if start_time not in range(0, 25) or end_time not in range(0, 25):
        return False
    if calendar:
        # if not empty
        if len(date.strip()) == 0:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        if date not in calendar:
            # new date
            calendar[date] = [{"start": start_time, "end": end_time, "title": title}]
        else:
            # exist date
            for dates in sorted(list(calendar.keys()), reverse=True):
                if date == dates:
                    tasks = list(calendar[date])
                    tasks.append({"start": start_time, "end": end_time, "title": title})
                    tasks = sorted(tasks, key=lambda k: k['start'], reverse=False)
                    calendar[date] = tasks
        save_calendar(calendar)
        return True

    else:
        # if empty
        calendar[date] = [{"start": start_time, "end": end_time, "title": title}]
        save_calendar(calendar)
        return True


def command_show(calendar):
    """
    (dict) -> str
    Returns the list of events for calendar sorted in decreasing date order
    and increasing time order within the date
    as a string, see examples below for a sample formatting
    calendar: the database of events

    Example:
    >>> calendar = {}
    >>> command_add("2018-01-15", 11, 13, "Eye doctor", calendar)
    True
    >>> command_add("2018-01-15", 8, 9, "lunch with sid", calendar)
    True
    >>> command_add("2018-02-10", 12, 23, "Change oil in blue car", calendar)
    True
    >>> command_add("2018-02-10", 20, 22, "dinner with Jane", calendar)
    True
    >>> command_add("2017-12-22", 5, 8, "Fix tree near front walkway", calendar)
    True
    >>> command_add("2017-12-22", 13, 15, "Get salad stuff", calendar)
    True
    >>> command_add("2018-05-06", 19, 23, "Sid's birthday", calendar)
    True
    >>> command_show(calendar)
    "\\n2018-05-06 : \\n    start : 19:00,\\n    end : 23:00,\\n    title : Sid's birthday\\n2018-02-10 : \\n    start : 12:00,\\n    end : 23:00,\\n    title : Change oil in blue car\\n\\n    start : 20:00,\\n    end : 22:00,\\n    title : dinner with Jane\\n2018-01-15 : \\n    start : 08:00,\\n    end : 09:00,\\n    title : lunch with sid\\n\\n    start : 11:00,\\n    end : 13:00,\\n    title : Eye doctor\\n2017-12-22 : \\n    start : 05:00,\\n    end : 08:00,\\n    title : Fix tree near front walkway\\n\\n    start : 13:00,\\n    end : 15:00,\\n    title : Get salad stuff"
    """
    if calendar:
        str_return = ""
        for dict_day in sorted(list(calendar.keys()), reverse=True):
            list_tasks = calendar[dict_day]
            str_return += "\n" + dict_day + " : "
            if len(list_tasks) > 1:
                def my_func(e):
                    return e['start']
                list_tasks.sort(reverse=False, key=my_func)
            for dict_task in list_tasks:
                start = dict_task["start"]
                end = dict_task["end"]
                title = dict_task["title"]
                str_return += "\n    start : " +\
                              datetime.datetime(2018, 6, 1, start).strftime("%H:%M") + \
                              ",\n    end : " +\
                              datetime.datetime(2018, 6, 1, end).strftime("%H:%M") + ",\n" + \
                              "    title : " + title
                if len(list_tasks) > 1 and dict_task != list_tasks[-1]:  # only middle change line appended
                    str_return += "\n"
        return str_return
    else:
        return ""


def command_delete(date, start_time, calendar):
    """
    (str, int, dict) -> str
    Delete the entry at calendar[date][start_time]
    If calendar[date] is empty, remove this date from the calendar.
    If the entry does not exist, do nothing
    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer indicating the start of the event in calendar[date] to delete
    calendar: The calendar database
    return: a string indicating any errors, True for no errors

    Example:


    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": \
    [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], "2018-02-28": [{"start": 11, "end": 12, \
    "title": "Python class"}]}
    True
    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2018-03-11", 3, calendar)
    'There is no event with start time of 3 on date 2018-03-11 in the calendar'
    >>> command_delete("2018-02-28", 11, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}]}
    True
    >>> command_delete("2018-03-11", 14, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}]}
    True
    >>> command_delete("2018-03-13", 13, calendar)
    True
    >>> calendar == {}
    True
    """

    # YOUR CODE GOES HERE
    if date in calendar:
        list_task = calendar.get(date)
        found = False
        for dict_task in list_task:
            if start_time == dict_task["start"]:
                found = True
                list_task.remove(dict_task)
                if len(list_task) == 0:
                    calendar.pop(date)
                save_calendar(calendar)
                return True
        if not found:
            return "There is no event with start time of {} on date {} in the calendar".format(start_time, date)
    else:
        return date + " is not a date in the calendar"

# -----------------------------------------------------------------------------
# Functions dealing with calendar persistence
# -----------------------------------------------------------------------------

"""
The calendar is read and written to disk.

...

date_i is "YYYY-MM-DD"'
description can not have tab or new line characters in them.

"""


def save_calendar(calendar):
    """
    (dict) -> bool
    Save calendar to 'calendar.txt', overwriting it if it already exists. The calendar events do not have
    to be saved in any particular order

    The format of calendar.txt is the following:

    date_1:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\\n
    date_2:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\\n
    date_n:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\\n

    Example: The following calendar...


        2018-03-13 : 
                start : 13:00,
                end : 13:00,
                title : Have fun
        2018-03-11 : 
                start : 10:00,
                end : 12:00,
                title : Another event on this date

                start : 14:00,
                end : 16:00,
                title : CSCA08 test 2
        2018-02-28 : 
                start : 11:00,
                end : 12:00,
                title : Python class

     appears in calendar.txt as ...

    2018-03-13:13-13 Have fun
    2018-03-11:10-12 Another event on this date    14-16 CSCA08 test 2
    2018-02-28:11-12 Python class

    calendar: dictionary containing a calendar
    return: True if the calendar was saved.


    >>> calendar = {"2019-01-11": \
                                [\
                                {"start": 3, "end": 4, "title": "Have fun3"}, \
                                {"start": 5, "end": 6, "title": "Have fun4"}, \
                                {"start": 7, "end": 8, "title": "Have fun5"}\
                                 ],\
                    "2018-03-11": \
                                [\
                                 {"start": 10, "end": 11, "title": "test 2"},\
                                 {"start": 12, "end": 13, "title": "test 3"}\
                                 ],\
                    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}],\
                    }
    >>> save_calendar(calendar)
    True
    """
    my_output = ""

    for date in sorted(list(calendar.keys()), reverse=True):
        tasks = list(calendar[date])
        my_string = ""
        for task in tasks:
            my_string += str(datetime.datetime(2018, 6, 1, task['start']).strftime("%H")) \
                         + "-" + str(datetime.datetime(2018, 6, 1, task['end']).strftime("%H")) \
                         + " " + task['title']
            my_string += '\t'
        my_day = date + ":" + my_string.rstrip("\t.") + "\n"
        my_output += my_day
    filename = "calendar.txt"
    if os.path.exists(filename):
        f = open(filename, "w")
        f.write(my_output)
        f.close()
        return True
    else:
        return False




def load_calendar():
    '''
    () -> dict
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above.

    return: calendar.
    >>> load_calendar()
    True

    calendar = {
        "2019-01-11": \
            [ \
                {"start": 3, "end": 4, "title": "Have fun3"}, \
                {"start": 5, "end": 6, "title": "Have fun4"} \
                ], \
        "2018-03-11": \
            [ \
                {"start": 14, "end": 16, "title": "CSCA08 test 2"} \
                ], \
        "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}] \
        }

    '''
    if not os.path.exists(FILENAME):
        open(FILENAME, "a").close
    f = open(FILENAME, "r")
    calendar = {}
    if not f.read(1):
        # empty txt
        f.seek(0)
        f.close
        return calendar
    else:
        f.seek(0)
        days = f.read().strip().split("\n")
        for day in days:
            date = day.split(":")[0]
            str_tasks = day.split(":")[1]
            list_task = str_tasks.split("\t")
            calendar[date] = []
            list_tasks_for_dict = []
            for str_task in list_task:
                list_time_title = str_task.split()
                str_time = list_time_title.pop(0)
                int_start = int(str_time.split("-")[0])
                int_end = int(str_time.split("-")[1])
                str_title = ""
                for x in list_time_title:
                    str_title += x + " "
                list_tasks_for_dict.append({"start": int_start, "end": int_end, "title": str_title.rstrip()})
            calendar[date] = list_tasks_for_dict
        f.close

    return calendar


# -----------------------------------------------------------------------------
# Functions dealing with parsing commands
# -----------------------------------------------------------------------------


def is_command(command):
    '''
    (str) -> bool
    Return whether command is a valid command
    Valid commands are any of the options below
    "add", "delete", "quit", "help", "show"
    You are not allowed to use regular expressions in your implementation.
    command: string
    return: True if command is one of ["add", "delete", "quit", "help", "show"]
    false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''

    # YOUR CODE GOES HERE
    # pass
    command_dict = ("add", "delete", "quit", "help", "show")
    if command in command_dict:
        return True
    else:
        return False

def is_calendar_date(date):
    '''
    (str) -> bool
    Return whether date looks like a calendar date
    date: a string
    return: True, if date has the form "YYYY-MM-DD" and False otherwise
    You are not allowed to use regular expressions in your implementation.
    Also you are not allowed to use isdigit() or the datetime module functions.

    Example:

    >>> is_calendar_date("215-110-10") # invalid year
    False
    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    >>> is_calendar_date("2015-04-31") # True even though April has only 30 days.
    True

    '''
    # Algorithm: Check length, then pull pieces apart and check them. Use only
    # basic string
    # manipulation, comparisons, and type conversion. Please do not use any
    # powerful date functions
    # you may find in python libraries.
    # 2015-10-12
    # 0123456789

    # YOUR CODE GOES HERE
    # pass
    if len(date) < 10 or date[4] != "-" or date[7] != "-":
        return False

    year = date[0:4]
    month = date[5:7]
    day = date[8:10]

    if not is_natural_number(year) \
            or not is_natural_number(month) \
            or not is_natural_number(day) or int(month) not in range(1, 13)\
            or int(day) not in range(1, 32):
        return False
    else:
        return True


def is_natural_number(str):
    '''
    (str) -> bool
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    param str: string
    Do not use string functions
    return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''
    # Algorithm:
    # Check that the string has length > 0
    # Check that all characters are in ["0123456789"]

    # YOUR CODE GOES HERE
    # pass
    natural_number = "0123456789"
    if len(str) == 0:
        return False
    for x in str:
        if x not in natural_number:
            return False

    return True


def parse_command(line):
    '''
    (str) -> list
    Parse command and arguments from the line. Return a list
    [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid.
    Return ["help"] otherwise.
    The valid commands are

    1) add DATE START_TIME END_TIME DETAILS
    2) show
    3) delete DATE START_TIME
    4) quit
    5) help

    line: a string command
    return: A list consiting of [command, arg1, arg2, ...].
    Return ["error", ERROR_DETAILS], if line can not be parsed.
    ERROR_DETAILS displays how to use the

    Example:
    >>> parse_command("add 2015-10-21 10 11 budget meeting")
    ['add', '2015-10-21', 10, 11, 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22 7 7 Tims with Sally.")
    ['add', '2015-10-22', 7, 7, 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 7 7 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22 11")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event start time']
    >>> parse_command("delete 2015-10-22 14")
    ['delete', '2015-10-22', 14]
    >>> parse_command("quit")
    ['quit']

    '''
    # HINT: You can first split, then join back the parts of
    # the final argument.
    # YOUR CODE GOES HERE
    # pass
    result = []
    if len(line) == 0 or line == "help":
        result.append("help")
    else:
        result = line.split(" ")
        if result[0].lower() == "add":
            if len(result) in range(1, 3):
                result.clear()
                result.append("error")
                result.append("add DATE START_TIME END_TIME DETAILS")
            if len(result) == 3:
                result.clear()
                result.append("error")
                result.append("add DATE START_TIME END_TIME DETAILS")
            if len(result) == 4 :
                if not is_natural_number(result[2]):
                    result.clear()
                    result.append("help")
                    return result
                else:
                    result.clear()
                    result.append("error")
                    result.append("add DATE START_TIME END_TIME DETAILS")
                    return result
            if len(result) > 4:
                base = []
                temp_str = ""
                base.append(result[0])
                if is_calendar_date(result[1]):
                    base.append(result[1])
                    for x in range(0, len(result)):
                        if 1 < x < 4:
                            base.append(int(result[x]))
                        if x > 3:
                            if len(result) <= 4:
                                temp_str += result[x]
                            if len(result) > 4:
                                temp_str += result[x]
                                temp_str += " "
                    temp_str = temp_str.strip()
                    result.clear()
                    result = base.copy()
                    result.append(temp_str)
                else:
                    result.clear()
                    result.append("error")
                    result.append("not a valid calendar date")

        if len(result) == 2 and result[0].lower() == "show":
            result.clear()
            result.append("error")
            result.append("show")

        if len(result) == 3 and result[0].lower() == "not":
            result.clear()
            result.append("help")

        if result[0] == "delete" or result[0].lower() == "del":
            if len(result) == 1:
                result.clear()
                result.append("error")
                result.append("delete DATE START_TIME")
            if len(result) == 2:
                result.clear()
                result.append("error")
                result.append("delete DATE START_TIME")
            if len(result) == 3:
                if not is_calendar_date(result[1]):
                    result.clear()
                    result.append("error")
                    result.append("not a valid calendar date")
            if len(result) == 3:
                if not is_natural_number(result[2]):
                    result.clear()
                    result.append("error")
                    result.append("not a valid event start time")
                else:
                    result[2] = int(result[2])

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
