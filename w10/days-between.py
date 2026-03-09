# 1. Name:
#      Tristan Zatylny
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This program calculates the number of days between two dates.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was making the asserts. It was relatively simple, though.
#      I used AI to help make the test cases work in one run of the program.
# 5. How long did it take for you to complete the assignment?
#      2 hours

def run_test_cases():
    test_cases = [
        {
            "name": "year less than 1753 (start year 1752)",
            "args": (2, 1, 1752, 2, 2, 1752),
            "expected": None,
            "expect_assert": True,
        },
        {
            "name": "year not an integer (start year is banana)",
            "args": (1, 9, "banana", 1, 19, 2001),
            "expected": None,
            "expect_assert": True,
        },
        {
            "name": "month less than 1 (start month is 0)",
            "args": (0, 9, 2001, 1, 19, 2001),
            "expected": None,
            "expect_assert": True,
        },
        {
            "name": "month greater than 12 (start month is 13)",
            "args": (13, 9, 2001, 1, 19, 2001),
            "expected": None,
            "expect_assert": True,
        },
        {
            "name": "day less than 1 (start day is 0)",
            "args": (1, 0, 2001, 1, 19, 2001),
            "expected": None,
            "expect_assert": True,
        },
        {
            "name": "day greater than month days (Feb 29, 2003)",
            "args": (2, 29, 2003, 3, 1, 2003),
            "expected": None,
            "expect_assert": True,
        },
        {
            "name": "end date before start date",
            "args": (1, 9, 2001, 1, 8, 2001),
            "expected": None,
            "expect_assert": True,
        },
        {
            "name": "start and end on same day",
            "args": (1, 9, 2001, 1, 9, 2001),
            "expected": 0,
            "expect_assert": False,
        },
        {
            "name": "start and end in same month/year",
            "args": (1, 9, 2001, 1, 19, 2001),
            "expected": 10,
            "expect_assert": False,
        },
        {
            "name": "start and end in same year",
            "args": (1, 9, 2001, 4, 19, 2001),
            "expected": 100,
            "expect_assert": False,
        },
        {
            "name": "start and end in different year",
            "args": (1, 9, 2001, 10, 6, 2003),
            "expected": 1000,
            "expect_assert": False,
        },
        {
            "name": "take leap years into account",
            "args": (1, 9, 2001, 5, 27, 2028),
            "expected": 10000,
            "expect_assert": False,
        },
    ]

    for i, case in enumerate(test_cases, start=1):
        try:
            result = main(*case["args"])
            if case["expect_assert"]:
                print(f"Test {i} ({case['name']}): FAIL (expected AssertionError, got {result})")
            elif result == case["expected"]:
                print(f"Test {i} ({case['name']}): PASS (expected {case['expected']}, got {result})")
            else:
                print(f"Test {i} ({case['name']}): FAIL (expected {case['expected']}, got {result})")
        except AssertionError as err:
            if case["expect_assert"]:
                print(f"Test {i} ({case['name']}): PASS (assert fired: {err})")
            else:
                print(f"Test {i} ({case['name']}): FAIL (unexpected assert: {err})")

def start():
    testing = input("Do test cases (y/n)? ").lower()

    if testing == "y":
        run_test_cases()

    else:
        done = False
        while not done:
            try:
                start_year = int(input("Start year: "))
                start_month = int(input("Start month: "))
                start_day = int(input("Start day: "))
                end_year = int(input("End year: "))
                end_month = int(input("End month: "))
                end_day = int(input("End day: "))

                # Make sure values are acceptable to run
                if ((start_year > 1752) and (end_year > 1752) and (start_month > 0) and (start_month < 13) and (end_month > 0) and (end_month < 13) and (start_day > 0) and (start_day < get_days(start_month, start_year)) and (end_day > 0) and (end_day < get_days(end_month, end_year)) and assert_chronological_dates(start_month, start_day, start_year, end_month, end_day, end_year)):
                    done = True
                else:
                    raise TypeError
            # I think it should be a TypeError but it's a ValueError so whatever
            except ValueError as e:
                print(f"Dates must be integer values.\nMessage: {e}\n")
            # Use the exception I raised earlier
            except TypeError:
                print(f"Dates must be in chronological order; years must be after 1752; days must be between 1 and max days of the month; months must be between 1 and 12.\n")
        
        days_between = main(start_month, start_day, start_year, end_month, end_day, end_year)

        print(f"There are {days_between} days between {start_month:02d}/{start_day:02d}/{start_year} and {end_month:02d}/{end_day:02d}/{end_year}")

def is_leap_year(year):
    # asserts
    assert isinstance(year, int), "year is not an integer"
    # year after 1752
    assert year > 1752, f"invalid year, year must be after 1752, got {year}"

    # quad-century - yes
    if year % 400 == 0:
        return True
    # non-quad century - no
    elif year % 100 == 0:
        return False
    # div by 4 - yes
    elif year % 4 == 0:
        return True
    # no
    return False

def get_days(month, year):
    # Asserts
    # are numbers
    assert isinstance(month, int), "month is not an integer"
    assert isinstance(year, int), "year is not an integer"
    # non-negative or zero
    assert month > 0 and month < 13, f"invalid month, expected a number 1-12, got {month}"
    assert year > 0, f"invalid year, cannot be negative nor zero, got {year}"

    match month:
        case 1:
            return 31
        case 2:
            if is_leap_year(year):
                return 29
            return 28
        case 3:
            return 31
        case 4:
            return 30
        case 5:
            return 31
        case 6:
            return 30
        case 7:
            return 31
        case 8:
            return 31
        case 9:
            return 30
        case 10:
            return 31
        case 11:
            return 30
        case 12:
            return 31
        case default:
            assert False, f"reached default case, match was {month}"

def assert_chronological_dates(start_month, start_day, start_year, end_month, end_day, end_year):
    # Assert everything is a number greater than 0
    assert isinstance(start_month, int), "start month is not an integer"
    assert isinstance(start_day, int), "start day is not an integer"
    assert isinstance(start_year, int), "start year is not an integer"
    assert isinstance(end_month, int), "end month is not an integer"
    assert isinstance(end_day, int), "end day is not an integer"
    assert isinstance(end_year, int), "end year is not an integer"
    assert start_month > 0 and start_month < 13, f"invalid month, expected a number 1-12, got {start_month}"
    assert start_day > 0 and start_day <= get_days(start_month, start_year), f"invalid day, expected a number 1-{get_days(start_month, start_year)}, got {start_day}"
    assert start_year > 0, f"invalid year, cannot be negative nor zero, got {start_year}"
    assert end_month > 0 and end_month < 13, f"invalid month, expected a number 1-12, got {end_month}"
    assert end_day > 0 and end_day <= get_days(end_month, end_year), f"invalid day, expected a number 1-{get_days(end_month, end_year)}, got {end_day}"
    assert end_year > 0, f"invalid year, cannot be negative nor zero, got {end_year}"

    # Start year is before end year
    if start_year < end_year:
        return True
    # Start year is same
    elif start_year == end_year:
        # Check months
        if start_month < end_month:
            return True
        # Months are same
        elif start_month == end_month:
            # Check days
            if start_day < end_day or start_day == end_day:
                return True
    # Failed one of these
    return False


def main(start_month, start_day, start_year, end_month, end_day, end_year):
    # Asserts
    assert isinstance(start_month, int), "start month is not an integer"
    assert isinstance(start_day, int), "start day is not an integer"
    assert isinstance(start_year, int), "start year is not an integer"
    assert isinstance(end_month, int), "end month is not an integer"
    assert isinstance(end_day, int), "end day is not an integer"
    assert isinstance(end_year, int), "end year is not an integer"
    assert start_month > 0 and start_month < 13, f"invalid month, expected a number 1-12, got {start_month}"
    assert start_day > 0 and start_day <= get_days(start_month, start_year), f"invalid day, expected a number 1-{get_days(start_month, start_year)}, got {start_day}"
    assert start_year > 0, f"invalid year, cannot be negative nor zero, got {start_year}"
    assert end_month > 0 and end_month < 13, f"invalid month, expected a number 1-12, got {end_month}"
    assert end_day > 0 and end_day <= get_days(end_month, end_year), f"invalid day, expected a number 1-{get_days(end_month, end_year)}, got {end_day}"
    assert end_year > 0, f"invalid year, cannot be negative nor zero, got {end_year}"
    # End date is after start date
    assert assert_chronological_dates(start_month, start_day, start_year, end_month, end_day, end_year), "dates are not in chronological order"
    
    
    # Same month and year
    if start_month == end_month and start_year == end_year:
        return end_day - start_day
    # Different month
    else:
        total = end_day
        total += get_days(start_month, start_year) - start_day

        # same year
        if start_year == end_year:
            # days for months between start and end
            for month in range(start_month + 1, end_month):
                total += get_days(month, start_year)
            return total
        # different years
        else:
            # days between start date and end of year
            if start_month != 12:
                for month in range(start_month + 1, 13):
                    total += get_days(month, start_year) 
            # make sure end date isn't in January for this
            if end_month != 1:
                # days between start of year and end month
                for month in range(1, end_month):
                    total += get_days(month, end_year)
            # make sure year gap is more than 1 for this
            if (end_year - start_year) > 1:
                # days in years between start and end
                for year in range(start_year + 1, end_year):
                    if is_leap_year(year):
                        total += 366
                    else:
                        total += 365
            # done
            return total
        
start()