def print_kwargs(**kwargs) :
    for k, v in kwargs.items() :
        if (k == "name") :
            print("이름은 : " + v)


print_kwargs(name = "강병관", age = "15")