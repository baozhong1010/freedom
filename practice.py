import random
'''
d={'math': {'math': 88, 'chinese': 70, 'english': 80}, 'chinese': 70, 'english': 80}
def values(data):
    for i in data:
        value = data[i]
        _type = type(value)
        print i,value,_type

values(d)
'''





'''
d={'math': {'math': 88, 'chinese': 70, 'english': 80}, 'chinese': 70, 'english': 80}
def mess(data,objkey):
    for i in data:
        value = data[i]
        _type = type(value)
        if i == objkey:
            for j in data[objkey]:
                value1 = value[j]
                _type1 = type(value1)
                print j,value1,_type1

        print i,value,_type
mess(d,'math')
'''


# plain dict
d = {'aaa': 111, 'bbb': 222, 'ccc': 333}

# dict containing list
d2 = {0: 'aaaa', 1: 'bbbb', 'fdsa': {'aaa': 111, 'bbb': 222, 'ccc': {'aaaa': 1111, 'bbbb': 2222}}, 'a list': [1, 2, 3, 4]}

# list with another key name
d3 = {0: 'aaaa', 1: 'bbbb', 'fdsa': {'aaa': 111, 'bbb': 222, 'ccc': {'aaaa': 1111, 'bbbb': 2222}}, 'b list': [1, 2, 3, 4]}

# list containing various items
d4 = {0: 'aaaa', 1: 'bbbb', 'fdsa': {'aaa': 111, 'bbb': 222, 'ccc': {'aaaa': 1111, 'bbbb': 2222}}, 'c list': [1, 'q', -1, 'fdsfds']}

# list with a random key name
d5 = {0: 'aaaa', 1: 'bbbb', 'fdsa': {'aaa': 111, 'bbb': 222, 'ccc': {'aaaa': 1111, 'bbbb': 2222}}, str(random.randint(100, 200)): [1, 2, 3, 4]}

# list containing dict
d6 = {0: 'aaaa', 1: [{'aaa': 111, 'bbb': 222}, 'fdsfds', 3, 4]}

# very deep dict
d7 = {}
d_temp = d7
for i in range(15):
    key = str(random.randint(1, 9))
    if i == 14:
        d_temp[key] = {'final': 'value'}
    else:
        d_temp[key] = {}
        d_temp = d_temp[key]

# empty dict
d8 = {}

def mess(data):
    for i in data:
        value = data[i]
        _type = type(value)
        if _type == dict:
            print i,value,_type
            for j in data['fdsa']:
                value1 = value[j]
                _type1 = type(value1)
                key = data['fdsa']
                if _type1 == dict:
                    for k in key['ccc']:
                        value2 = value1[k]
                        _type2 = type(value2)
                        print k,value2,_type2
                else:
                    print j,value1,_type1
        else:
            if _type == list:
                for m in data['a list']:
                    value3 = value[m-1]
                    _type3 = type(value3)
                    print value3, _type3
            else:
                print i,value,_type

mess(d2)

