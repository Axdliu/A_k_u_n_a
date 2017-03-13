# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 16:37:26 2017

@author: User
"""

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        
people_list = [
    Person("Bob Bobson", 26),
    Person("Joe Joeyjoe", 35),
    Person("Joe Testington", 21)
]


# returns a dictionary of first names and a list of all ages that have that name
def get_ages(people_list):
    result = {}
    for person in people_list:
        for letter in person.name:
            if letter == ' ':
                first_name = person.name[:person.name.index(letter)]
                if first_name in result.keys():
                    result[first_name] = [person.age] + result[first_name]                          
                else:
                    result[first_name] = [person.age] 
    return result

result = get_ages(people_list)
print result

# result is { "Bob": [26], "Joe": [21, 35]}
               