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
class Fish(FishInfo):
    def __init__(self, name= "oseledets", price_in_uah_per_kilo = 11.4, origin= "Finland",
                 catch_date= datetime.date(2022,1,31), due_date= datetime.date(2022,2,3), 
                 age_in_months=3, weight_in_kg=0.1) -> None:
        FishInfo.__init__(self, name, price_in_uah_per_kilo , origin, catch_date,due_date)
        self.age_in_months = age_in_months
        self.weight_in_kg = weight_in_kg

class FishBox(FishInfo):
    fish = FishInfo(name= "oseledets", price_in_uah_per_kilo = 11.4, origin= "Finland",
                 catch_date= datetime.date(2022,1,31), due_date= datetime.date(2022,2,3))
    fish.price_in_uah_per_kilo
    def __init__(self, fish = FishInfo(name= "oseledets", price_in_uah_per_kilo = 11.4, origin= "Finland",
                 catch_date= datetime.date(2022,1,31), due_date= datetime.date(2022,2,3)),
                 weight_of_fishbox = 9, package_date= datetime.date(2022,1,21), box_height = 0.2,
                 box_width = 0.3, box_length = 0.7, is_alive = True) -> None:
        self.fish = fish
        self.box_weight = weight_of_fishbox
        self.package_date = package_date
        self.box_height = box_height
        self.box_width = box_width
        self.box_length = box_length
        self.is_alive = is_alive
class FishShop(FishBox, Fish):
    all_fish =[]
    frozen_fish_boxes = []
    fresh_fish = []
    def add_fish(new_fish_box)->None:
        FishShop.all_fish.append(new_fish_box)
        print(new_fish_box.box_weight, "kg of ", new_fish_box.fish.name, " was added")
    def sort_price(fish_box):
        return fish_box.fish.price_in_uah_per_kilo
    def get_fish_names_sorted_by_price(fish_list) -> List[Union[str,bool,float]]:
        sorted_fish = sorted(fish_list, key  = FishShop.sort_price)       
        frozen_fish = [f for f in sorted_fish if f.is_alive == False]
        for fish in frozen_fish:
            FishShop.frozen_fish_boxes.append(fish)
            FishShop.get_frozen_fish_names_sorted_by_price(frozen_fish)
           
        alive_fish = [f for f in sorted_fish if f.is_alive == True]
        for fish in alive_fish:
            FishShop.fresh_fish.append(fish)
            FishShop.get_fresh_fish_names_sorted_by_price(alive_fish)
        FishShop.see_available()
        return (list[fish.fish.name, fish.is_alive, fish.fish.price_in_uah_per_kilo])
    def get_frozen_fish_names_sorted_by_price(fish_list) -> List[Union[str,float]]:
        sorted_fish = sorted(FishShop.frozen_fish_boxes, key  = FishShop.sort_price)
        FishShop.frozen_fish_boxes = sorted_fish
        for fish in sorted_fish:
            print(fish.fish.name, fish.fish.price_in_uah_per_kilo)
        return (list[fish.fish.name, fish.fish.price_in_uah_per_kilo])
    def get_fresh_fish_names_sorted_by_price(fish_list) -> List[Union[str,float]]:
        sorted_fish = sorted(FishShop.fresh_fish, key = FishShop.sort_price)
        FishShop.fresh_fish = sorted_fish
        for fish in sorted_fish:
            print(fish.fish.name, fish.fish.price_in_uah_per_kilo)
        return (list[fish.fish.name, fish.fish.price_in_uah_per_kilo])

    def sell_fish(want_name, want_weight) -> Union[str,float,float]:
        want_fish = [f for f in fish_list if f.fish.name == want_name]
        for fish in want_fish:
            if(fish.box_weight > want_weight):
                total_price = fish.fish.price_in_uah_per_kilo * want_weight
                print("%.2f" % total_price)
                fish.box_weight -= want_weight
            else:
                print("No ", want_name," left in stock")
        return [want_name, want_weight, total_price]
    
    def see_available()->None:
        for fish_in_shop in FishShop.all_fish: 
            print(fish_in_shop.fish.name," is in the store")

oseledets = Fish()
tilapia = Fish("tilapia", 14.5,"Norway", datetime.date(2022,1,30), datetime.date(2022,2,2),3,0.2)
hek = Fish("hek", 9.4,"Finland", datetime.date(2022,1,27), datetime.date(2022,1,30),5,0.3)
salmon = Fish("salmon", 20.3,"Norway", datetime.date(2022,1,29), datetime.date(2022,2,1),2,0.7)

oseledets_box = FishBox()
tilapia_box = FishBox(tilapia, 8, datetime.date(2022,1,30), 0.4, 0.3, 0.9, False)
hek_box = FishBox(hek, 5, datetime.date(2022,1,28), 0.2, 0.5, 0.8, False)
salmon_box = FishBox(salmon, 9, datetime.date(2022,1,30), 0.3, 0.4, 0.7, True)

oseledets_in_store = FishShop.add_fish(oseledets_box)
tilapia_in_store = FishShop.add_fish(tilapia_box)
hek_in_store = FishShop.add_fish(hek_box)
salmon_in_store = FishShop.add_fish(salmon_box)

fish_list = [oseledets_box, tilapia_box,hek_box,salmon_box]

find_fish = [f for f in fish_list if f.box_length == 0.7]
for fish in find_fish:
    print(fish.fish.name)
FishShop.get_fish_names_sorted_by_price(fish_list)
sorted_fish = sorted(fish_list, key  = FishShop.sort_price)
sold = FishShop.sell_fish("hek",0.2)