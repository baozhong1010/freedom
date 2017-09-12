import hashlib
import random
import time
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

# another nested dict
d9 = {0: 'aaaa', 1: 'bbbb', 'asdf': {'aaa': 111, 'bbb': 222}}

# another nested dict - 2
d10 = {
    hashlib.sha1(str(time.time()).encode('ascii')).hexdigest(): {
        hashlib.sha1(str(time.time()).encode('ascii')).hexdigest(): {
            hashlib.sha1(str(time.time()).encode('ascii')).hexdigest(): {
                hashlib.sha1(str(time.time()).encode('ascii')).hexdigest(): hashlib.sha1(str(time.time()).encode('ascii')).hexdigest(),
            }
        }
    }
}

# dict with time key
d11 = {
    '%23.22f' % time.time(): 'value value value',
}

# nested dict with time key
d12 = {
    '%23.22f' % time.time(): {
        '%23.22f' % time.time(): 'value value value',
    }
}

# batch generate 10 nested dicts: d13 - d22
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for i in range(13, 23):
    globals()['d%d' % i] = {
        ''.join([random.choice(alphabet), random.choice(alphabet), random.choice(alphabet), random.choice(alphabet)]): {
            ''.join([random.choice(alphabet), random.choice(alphabet), random.choice(alphabet), random.choice(alphabet)]): 'value',
        },
    }


# nested dict: d23 - d32: asd0 - asd9
d23 = {}
_dict = d23
for i in range(23, 33):
    globals()['d%d' % i] = {
        'asd%d' % (i - 23): {'key': 'value'},
    }





def mess(data):
    for i in data:
        value = data[i]
        _type = type(value)
        print i,value,_type
        if _type == dict:
            return mess(data)#所有value是dict的循环输出其key，value，value的类型                                             
                        
        #所有列表的输出
        elif _type == list:
            for m in data[i]:
                if isinstance(m,str):
                    print m,type(m)
                elif isinstance(m,dict):
                    for n in m:
                        print n,m[n],type(m[n])
                else:
                    print m,type(m)
    
print '-'*20
mess(d2)
print '-'*20
mess(d3)
print '-'*20
mess(d4)
print '-'*20
mess(d5)
print '-'*20
mess(d6)
print '-'*20
mess(d7)
print '-'*20
mess(d8)
print '-'*20
mess(d9)
print '-'*20
mess(d10)
print '-'*20
mess(d11)
print '-'*20
mess(d12)
print '-'*20
mess(d23)

mess(d24)

mess(d25)

mess(d26)

mess(d27)

mess(d28)

mess(d29)

mess(d30)

mess(d31)

mess(d32)




