
capitals={
    "USA":'Mexico',
    "Year":1999,
    "VietNam":"Hanoi",
    "isBoolean":True,
}

capitals.update({'USA':'Canada'});
capitals.pop('Year');

capitals.clear();

# print(capitals['hanoi']) // Error Syntax
# print(capitals.get('Hanoi'))// None;
# print(capitals.keys());
# print(capitals.values());
# print(capitals.items());

for key,value in capitals.items():
    print(key,value);