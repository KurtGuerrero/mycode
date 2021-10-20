#!/usr/bin/env python3
""" Day3 challange """


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


for x in farms:
    n= (x.get("name"))
    print(x)
    print(n)
    #print(f"Name="{n})
    print(x.get("agriculture"))
    if x == "NE Farm":
        print(x)
        print(agriculture)
    print(type(x.get("name")))
    #else print("skip")
