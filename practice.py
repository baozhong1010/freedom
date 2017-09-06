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



d2 = {0: 'aaaa', 1: 'bbbb', 'asdf': 123456, 'fdsa': {'aaa': 111, 'bbb': 222, 'ccc': {'aaaa': 1111, 'bbbb': 2222}}, 'a list': [1, 2, 3, 4]}

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
                    value3 = value[m]
                    _type3 = type(value3)
                    print value3, _type3
            else:
                print i,value,_type
        
mess(d2)


