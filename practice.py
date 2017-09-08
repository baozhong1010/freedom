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
'''
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
'''

# nested dict: d23 - d32: asd0 - asd9
for i in range(23, 33):
    globals()['d%d' % i] = {
        'asd%d' % (i - 23): {'key': 'value'},
    }
    print 'd%d' % i,'asd%d' % (i - 23),globals()['d%d' % i]['asd%d' % (i - 23)],type(globals()['d%d' % i]['asd%d' % (i - 23)])








    
'''
def mess(data):
    for i in data:
        value = data[i]
        _type = type(value)
        string = str(random.randint(100, 200))

        if _type == dict:
            print i,value,_type
            if i == 'fdsa':
                key1 = data['fdsa']
                for j in key1:
                    value1 = value[j]
                    _type1 = type(value1)
                    if _type1 == dict:
                        for k in key1['ccc']:
                            value2 = value1[k]
                            _type2 = type(value2)
                            print k,value2,_type2
                    else:
                        print j,value1,_type1
            elif i == 'asdf':
                key2 = data['asdf']
                for y in key2:
                    print y,key2[y],type(key2[y])

        elif _type == list:
                if i == 'a list':
                    for m in data['a list']:
                        print m,type(m)
                elif i == 'b list':
                    for n in data['b list']:
                        print n,type(n)
                elif i == 'c list':
                    for l in data['c list']:
                        if isinstance(l,str):
                            print l,type(l)
                        else:
                            print l,type(l)
                elif i == string:
                    for x in data['string']:
                        print x,type(x)
                elif isinstance(value,list):
                    for a in value:
                        if isinstance(a,dict):
                            for b in a:
                                print b,a[b],type(a[b])
                        elif isinstance(a,str):
                            print a,type(a)
                        else:
                            print a,type(a)


        else:
            print i,value,_type
mess(d2)
print '-'*20
#mess(d3)
print '-'*20
#mess(d4)
print '-'*20
#mess(d5)
print '-'*20
#mess(d6)
print '-'*20
mess(d7)
print '-'*20
#mess(d8)
print '-'*20
#mess(d9)
'''





