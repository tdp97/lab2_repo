ivan = {
    "name" : "ivan",
    "age": 34,
    "children" : [{
        "name": "vasya",
        "age": 12,
    }, {
    "name": "petya",
    "age": 10,
    }],
}
darya = {
    "name": "darya",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],

}
emps = [ivan, darya]
for i in emps:
    for p in i ["children"]:
        if (p["age"])> 18:
            print(i["name"])
            break