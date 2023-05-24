#DICTIONARY

#associate array

#1ist->index, dictionary=>key
#accessing dictionary
data_dict = {
    "nama_item":"tas",
    "harga": 2000000,
    "brand": "charles and keith"
}

print(data_dict)
print(data_dict["nama_item"])
print(data_dict.get("nama_item"))
key_list = data_dict.keys()
print(key_list)

value_list = data_dict.values()
print(value_list)

item_list = data_dict.items()
print(item_list)

for key, value in item_list:
    print(key, "=", value)
#modifying items
data_dict["nama_item"] = "topi"
print(data_dict)

nama_item = data_dict.pop("nama_item")
print(nama_item)
print(data_dict)

new_item = {
    "item_name_new":"sepatu"
}

data_dict.update(new_item)
print(data_dict)

#1ooping through dictionary
print("====1ooping dict=====")
data = {

    "item":{
        "name": "tas",
        "color": "black"
    },
    "price":1000000,
    "brand": "ck"
}

for x in data:
    print(x)

dict2 = data.copy()
print(dict2)

#nested dictionary
print(data)
print(data["item"]["name"])