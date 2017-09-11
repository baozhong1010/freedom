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
        string = str(random.randint(100, 200))
        if _type == dict:
            print i,value,_type#输出最外层字典的各项     
            for j in data[i]:
                value2 = data[i][j]
                _type2 = type(value2)
                print j,value2,_type2#输出第二层字典里的各项
                if type(value2) == dict:
                    for j3 in value2:
                        value3 = value2[j3]
                        _type3 = type(value3)
                        print j3,value3,_type3#输出最里面三层字典的各项
                        if type(value3) == dict:  
                            for j4 in value3:
                                value4 = value3[j4]
                                _type4 = type(value4)
                                print j4,value4,_type4#输出最里面四层字典的各项
                                if type(value4) == dict:
                                    for j5 in value4:
                                        value5 = value4[j5]
                                        _type5 = type(value5)
                                        print j5,value5,_type5#输出最里面五层字典的各项
                                        if type(value5) == dict:
                                            for j6 in value5:
                                                value6 = value5[j6]
                                                _type6 = type(value6)
                                                print j6,value6,_type6#输出最里面六层字典的各项
                                                if type(value6) == dict:
                                                    for j7 in value6:
                                                        value7 = value6[j7]
                                                        _type7 = type(value7)
                                                        print j7,value7,_type7#输出最里面七层字典的各项
                                                        if type(value7) == dict:
                                                            for j8 in value7:
                                                                value8 = value7[j8]
                                                                _type8 = type(value8)
                                                                print j8,value8,_type8#输出最里面八层字典的各项
                                                                if type(value8) == dict:
                                                                    for j9 in value8:
                                                                        value9 = value8[j9]
                                                                        _type9 = type(value9)
                                                                        print j9,value9,_type9#输出最里面九层字典的各项
                                                                        if type(value9) == dict:
                                                                            for j10 in value9:
                                                                                value10 = value9[j10]
                                                                                _type10 = type(value10)
                                                                                print j10,value10,_type10#输出最里面十层字典的各项
                                                                                if type(value10) == dict:
                                                                                    for j11 in value10:
                                                                                        value11 = value10[j11]
                                                                                        _type11 = type(value11)
                                                                                        print j11,value11,_type11#输出最里面十一层字典的各项
                                                                                        if type(value11) == dict:
                                                                                            for j12 in value11:
                                                                                                value12 = value11[j12]
                                                                                                _type12 = type(value12)
                                                                                                print j12,value12,_type12#输出最里面十二层字典的各项
                                                                                                if type(value12) == dict:
                                                                                                    for j13 in value12:
                                                                                                        value13 = value12[j13]
                                                                                                        _type13 = type(value13)
                                                                                                        print j13,value13,_type13#输出最里面十三层字典的各项
                                                                                                        if type(value13) == dict:
                                                                                                            for j14 in value13:
                                                                                                                value14 = value13[j14]
                                                                                                                _type14 = type(value14)
                                                                                                                print j14,value14,_type14#输出最里面十四层字典的各项
                                                                                                                if type(value14) == dict:
                                                                                                                    for j15 in value14:
                                                                                                                        value15 = value14[j15]
                                                                                                                        _type15 = type(value15)
                                                                                                                        print j15,value15,_type15#输出最里面十五层字典的各项
                                                                                                                        if type(value15) == dict:
                                                                                                                            for j16 in value15:
                                                                                                                                value16 = value15[j16]
                                                                                                                                _type16 = type(value16)
                                                                                                                                print j16,value16,_type16#输出最里面十六层字典的各项
                                                                                                                                if type(value16) == dict:
                                                                                                                                    for j17 in value16:
                                                                                                                                        value17 = value16[j17]
                                                                                                                                        _type17 = type(value17)
                                                                                                                                        print j17,value17,_type17#输出最里面十七层字典的各项
                                        
                        
                        
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
        else:
            print i,value,_type
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




