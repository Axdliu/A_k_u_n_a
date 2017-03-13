# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 17:49:43 2017

@author: User
"""



class Counter:
    @staticmethod
    def serve_drink(name):
        print("ENJOY THE DRINK %s!" % name.upper())

class Bouncer:
    @staticmethod
    def kick_out(name):
        print("GET OUTTA HERE %s!" % name.upper())
        
class Phone:
    @staticmethod
    def call_boss(drink_count):
        print("WHAT A GREAT NIGHT. WE SERVED %d DRINKS." %(drink_count))

class AutoBar:
    
    def __init__(self):
        self.details = {}
        self.blacklist = []
        self.drinks = 0
    
    def person_enters(self, name):
        if name in self.blacklist:
            Bouncer.kick_out(name)
        else:
            self.details[name] = 0
        
    def person_wants_drink(self, name):
        if name in self.details.keys():
            if self.details[name] == 10:
                Bouncer.kick_out(name)
                self.blacklist.append(name)
                self.drinks += self.details.pop(name)
                # print self.drinks
            else:
                Counter.serve_drink(name)
                self.details[name] += 1

        else:
            self.drinks += 1
            # print self.drinks
                    
    def person_leaves(self, name):
        self.drinks += self.details.pop(name)
        # print self.drinks
        
    def bar_closing_time(self):
        # print self.details
        client_sorted = dict(sorted(self.details.items(), key=lambda x: x[0]))        
        for name in client_sorted.keys():
            Bouncer.kick_out(name)
            self.drinks += client_sorted.pop(name)
            # print self.drinks            
        drinks_sold = self.drinks
        Phone.call_boss(drinks_sold)    


if __name__ == '__main__':        

    J10 = AutoBar()
    
    J10.person_enters('Cat')
    J10.person_enters('Dog')
    J10.person_enters('Ant')
    J10.person_enters('Pig')
    
    J10.person_wants_drink('Eel')
    J10.person_wants_drink('Dog')
    
    for i in range(5):
        J10.person_wants_drink('Cat')
        J10.person_wants_drink('Ant')
    
    for i in range(5):
        J10.person_wants_drink('Cat')
        J10.person_wants_drink('Pig')
    
    J10.person_wants_drink('Cat')    
        
    J10.person_enters('Cat')   
    
    J10.person_wants_drink('Dog')
    J10.person_leaves('Ant')
    
    J10.bar_closing_time()
    
    
    


    
