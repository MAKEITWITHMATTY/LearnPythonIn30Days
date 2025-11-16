def make_profile(name, *, age, country):
    print(name, age, country)

make_profile("Matty", age=32, country="UK")   # must use keywords!
make_profile("Matty", 32, "UK")   # NOT allowed
