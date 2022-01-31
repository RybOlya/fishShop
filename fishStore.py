import datetime
from typing import Union
from typing import List
class FishInfo(object):
    def __init__(self, name, price_in_uah_per_kilo, origin, catch_date,due_date) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.origin = origin
        self.catch_date = catch_date
        self.due_date = due_date
    def is_fresh(self) -> bool:
        today = datetime.date.today()
        days_after_catch = today - self.catch_date
        still_fresh = today <= self.due_date
        print("It's been ",days_after_catch.days, " days since the catch")
        return still_fresh
    # def see_available(fish_list)->None:
    #     for fish in fish_list: 
    #         print(fish.name + " and price is " + str(fish.price_in_uah_per_kilo))
    
class Fish(FishInfo):
    def __init__(self, name= "oseledets", price_in_uah_per_kilo = 11.4, origin= "Finland",
                 catch_date= datetime.date(2022,1,31), due_date= datetime.date(2022,2,3), 
                 age_in_months=3, weight_in_kg=0.1) -> None:

        FishInfo.__init__(self, name, price_in_uah_per_kilo , origin, catch_date,due_date)
        #super().__init__(name, price_in_uah_per_kilo , origin, catch_date,due_date)
        #super(Fish, self).__init__(name, price_in_uah_per_kilo , origin, catch_date,due_date)
        self.age_in_months = age_in_months
        self.weight_in_kg = weight_in_kg
class FishBox(FishInfo):
     def __init__(self,fish, weight_of_fishbox = 9, package_date= datetime.date(2022,1,31), box_height = 0.2,box_width = 0.3, box_length = 0.7, is_alive = True) -> None:
        self.fish = fish
        self.box_weight = weight_of_fishbox
        self.package_date = package_date
        self.box_height = box_height
        self.box_width = box_width
        self.box_length = box_length
        self.is_alive = is_alive
class FishShop(FishBox, Fish):
    #def __init__(self,frozen_fish_box)->None:
        #self.frozen_fish_box = frozen_fish_box
    frozen_fish_boxes = []
    #fresh_fish = vars(List[Fish])
    #frozen_fish_boxes = fish_box.dict
    def add_fish(frozen_fish_box)->None:
        FishShop.frozen_fish_boxes.append(frozen_fish_box)
    # def add_fish(self, fish)->None:
    #     print(vars(fish))
    def see_available()->None:
        for fish_in_shop in FishShop.frozen_fish_boxes: 
            print(fish_in_shop.fish.name," is in the store")
        print(type(FishShop.frozen_fish_boxes),type(fish_in_shop))
def search(list, name):
    for i in range(len(list)):
        if list[i] == name:
            return True
    return False
oseledets = Fish()
tilapia = Fish("tilapia", 14.5,"Norway", datetime.date(2022,1,30), datetime.date(2022,2,2),3,0.2)
hek = Fish("hek", 9.4,"Finland", datetime.date(2022,1,27), datetime.date(2022,1,30),5,0.3)
salmon = Fish("salmon", 20.3,"Norway", datetime.date(2022,1,29), datetime.date(2022,2,1),2,0.7)

oseledets_box = FishBox(oseledets)
tilapia_box = FishBox(tilapia, 8, datetime.date(2022,1,30), 0.3, 0.4, 0.8, True)
hek_box = FishBox(hek, 5, datetime.date(2022,1,28), 0.3, 0.4, 0.8, True)
salmon_box = FishBox(salmon, 9, datetime.date(2022,1,30), 0.3, 0.4, 0.8, True)

oseledets_in_store = FishShop.add_fish(oseledets_box)
tilapia_in_store = FishShop.add_fish(tilapia_box)
hek_in_store = FishShop.add_fish(hek_box)
salmon_in_store = FishShop.add_fish(salmon_box)
FishShop.see_available()
# print(oseledets_box.package_date)
# fish_list = []
# fish_list.append(oseledets)
# fish_list.append(tilapia)
# fish_list.append(hek)
# fish_list.append(salmon)
# for fish in fish_list:
#     print(Fish.is_fresh(fish))
# Fish.see_available(fish_list)
    #FishShop.cast_out_old_fish(fish)