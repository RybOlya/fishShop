import datetime
from typing import Union
from typing import List
class FishInfo:
    def init(self, name= "oseledets", price_in_uah_per_kilo = 11.4, origin= "Norway", catch_date= datetime.date(2022,1,20),due_date= datetime.date(2022,1,23)) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.origin = origin
        self.catch_date = catch_date
        self.due_date = due_date

    def is_fresh(self) -> bool:
        today = datetime.date.today()
        days_after_catch = today - self.catch_date
        print("It's been ",days_after_catch.days, " days since the catch")
        return days_after_catch.days<=Fish.IS_NOT_FRESH
    def see_available(fish_list)->None:
        for fish in fish_list: 
           print(fish.name + " and price is " + str(fish.price_in_uah_per_kilo))
class Fish(FishInfo):
    def init(self, age_in_months = 3, weight_in_kg= 1.2) -> None:
        self.age_in_months = age_in_months
        self.weight_in_kg = weight_in_kg
class FishBox(FishInfo):
     def init(self, weight_of_fishbox = 9, package_date= datetime.date(2022,1,21), box_height = 0.2,box_width = 0.3, box_length = 0.7, is_alive = True) -> None:
        self.weight_of_fishbox = weight_of_fishbox
        self.package_date = package_date
        self.box_height = box_height
        self.box_width = box_width
        self.box_length = box_length
        self.is_alive = is_alive
class FishShop(FishBox, Fish):
    fish_box = FishBox()
    fish = Fish()
    frozen_fish_box = vars(List[fish_box])#vars(FishBox)
    fresh_fish = vars(List[fish])
    #frozen_fish_boxes = fish_box.dict
    def add_fish(self, fish_box)->None:
        print(vars(fish_box))
    def add_fish(self, fish)->None:
        print(vars(fish))
    def search(self, list, name):
        for i in range(len(list)):
            if list[i] == name:
                return True
        return False
    def sell_fish(self, name, weight_in_kg) -> Union[str,float,float]:
        total_price = self.price_in_uah_per_kilo * weight_in_kg
        if self.search(List[self.fish_box], name):
            if(self.weight_in_kg > weight_in_kg):
                self.weight_in_kg -= weight_in_kg
            else:
                print("No ", name," left in stock")
        return Union[name, weight_in_kg, total_price]
    
    def get_fish_names_sorted_by_price(unsorted_fist_list) -> List[Union[str,bool,float]]:
        sorted_fist_list = sorted(unsorted_fist_list, key=lambda FishInfo: FishInfo.price_in_uah_per_kilo)
        return sorted_fist_list
    def get_fresh_fish_names_sorted_by_price(sorted_fist_list) -> List[Union[str,float]]:
        sorted_fresh_fist_list = sorted(sorted_fist_list, key=lambda FishInfo: FishInfo.price_in_uah_per_kilo)
        return sorted_fresh_fist_list
    def get_frozen_fish_names_sorted_by_price(sorted_fist_list) -> List[Union[str,float]]:
        sorted_frozen_fist_list = sorted(sorted_fist_list, key=lambda FishInfo: FishInfo.price_in_uah_per_kilo)
        return sorted_frozen_fist_list


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
    def init(self) -> None:
        self.fish_preference = "tilapia"
        self.weight_preference = 0.7
        self.budget = 200
    def select_fish(self):
        pass
    def buy_fish(self):
        pass
talapia = FishInfo("talapia", 14.5, datetime.date(2022,1,20),"Norway",True,200)
hek = Fish("hek", 9.4, datetime.date(2022,1,26),"Finland",False,300)
salmon = Fish("salmon", 20.3, datetime.date(2022,1,25),"Norway",False,50)
fish_list = []
fish_list.append(talapia)
fish_list.append(hek)
fish_list.append(salmon)
for fish in fish_list:
    FishShop.cast_out_old_fish(fish)
#fish_list = FishShop.get_fish_names_sorted_by_price(fish_list)
fist_list = FishShop.get_fish_names_sorted_by_price(fish_list)
if fist_list[1] is True:
    FishShop.get_fresh_fish_names_sorted_by_price(fish_list)
else:
    FishShop.get_frozen_fish_names_sorted_by_price(fish_list)    
print("Sorted By price")
Fish.see_available(fish_list)
#osetr = FishShop.add_fish("", "osetr",7.9)
#print(talapia.is_fresh())