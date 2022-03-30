def return_10():
    return 10

def add(first_num, second_num):
    return first_num + second_num

def subtract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num):
    return first_num * second_num

def divide(first_num, second_num):
    return first_num / second_num

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    list = [string_1, string_2]
    return " ".join(list)

def add_string_as_number(string_1, string_2):
    string_1 = int(string_1)
    string_2 = int(string_2)
    return string_1 + string_2

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
def number_to_full_month_name(key):
    return months[key]

print(number_to_full_month_name(10))

months_short = {
    1: "Jan",
    4: "Apr",
    10: "Oct"
}
def number_to_short_month_name(key):
    return months_short[key]

import math
def volume_of_cube_calculator(cube_side):
   return int(math.pow(cube_side, 3))

def string_reverser(string):
    return string[::-1]

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return int(celsius)

