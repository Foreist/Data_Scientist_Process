def add(a, b):
    return a + b

data = (10, 20)


def introduce(name, greeting):
    return "{name}님, {greeting}".format(
        name=name,
        greeting=greeting,
    )
#
introduce_dict = {
    "name" : "김진수",
    "greeting" : "안녕하세요",
}

#print(add(*data))

#print(introduce(**introduce_dict))
#print(introduce_dict)

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]

result = [i+j for i in case_1 for j in case_2]
print(result)



