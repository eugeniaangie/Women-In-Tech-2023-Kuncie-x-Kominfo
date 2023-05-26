print(5*"=", "belajar list n dictionaries", 5*"=")
#case: web ecommerce, mencari data is_paid
data_dummy = [{
        "nama_item" : "sepatu",
        "harga" : 2000000,
        "brand" : "ventela",
        "is_paid": True
    },
    {
        "nama_item" : "tas",
        "harga" : 2000000,
        "brand" : "ck",
        "is_paid": False
    },
    {
        "nama_item" : "celana",
        "harga" : 500,
        "brand" : "cenem",
        "is_paid": True
    }]

total_harga = sum(item['harga'] for item in data_dummy)
print(total_harga)

# print(data_dummy)

print(f"nama item data pertama: {data_dummy[0]['nama_item']}")

list_data_paid = []
for data in data_dummy:
    if data['is_paid']==True:
        list_data_paid.append(data)
    else:
        data.update({"apakah barang sudah dibayar": "belum"})
        print(data)
        
        
# print(list_data_paid)