import datetime
from ctypes import Union
from typing import List
class Fish:
    IS_NOT_FRESH = 2
    def __init__(self, name= "oseledets", price_in_uah_per_kilo= 11.2, catch_date= datetime.date(2022,1,21) , origin= "Norway", body_only= True, weight_in_kg= 100) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.origin = origin
        self.body_only = body_only 
        self.weight_in_kg = weight_in_kg

    def is_fresh(self) -> bool:
        today = datetime.date.today()
        days_after_catch = today - self.catch_date
        print("It's been ",days_after_catch.days, " days since the catch")
        return days_after_catch.days<=Fish.IS_NOT_FRESH
    def see_available(fish_list)->None:
        for fish in fish_list: 
           print(fish.name + " and price is " + str(fish.price_in_uah_per_kilo))
class FishShop(Fish):
    def add_fish(self, fish_name: str, total_weight: float):
        #fish_name = input("Enter fish name: ")
        #self.fish_name = fish_name
        
        print("New fish added:\n Name: ",fish_name, "\n Total weight:",total_weight)
    
    def get_fish_names_sorted_by_price(unsorted_fist_list) -> list:
        sorted_fist_list = sorted(unsorted_fist_list, key=lambda Fish: Fish.price_in_uah_per_kilo)
        return sorted_fist_list
    
    
    def sell_fish(self, fish_name: str, weight: float) -> float:
        pass

    def cast_out_old_fish(self):
        if Fish.is_fresh(self) is False:
           print(self.name, " is cast out")
           del self
        else:
            print(self.name, " is fresh")
            print(self)
    pass

class Seller(FishShop):
    def display_fish_by_(self):
        pass

class Buyer:
    def __init__(self) -> None:
        self.fish_preference = "tilapia"
        self.weight_preference = 0.7
        self.budget = 200
    def select_fish(self):
        pass
    def buy_fish(self):
        pass
talapia = Fish("talapia", 14.5, datetime.date(2022,1,20),"Norway",True,200)
hek = Fish("hek", 9.4, datetime.date(2022,1,26),"Finland",False,300)
salmon = Fish("salmon", 20.3, datetime.date(2022,1,25),"Norway",False,50)
fish_list = []
fish_list.append(talapia)
fish_list.append(hek)
fish_list.append(salmon)
for fish in fish_list:
    FishShop.cast_out_old_fish(fish)
fish_list = FishShop.get_fish_names_sorted_by_price(fish_list)
print("Sorted By price")
Fish.see_available(fish_list)
#osetr = FishShop.add_fish("", "osetr",7.9)
#print(talapia.is_fresh())