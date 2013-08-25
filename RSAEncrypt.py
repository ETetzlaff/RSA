#	I would like to import the baseexp and modularexp as a class to use an object oriented approach to this
def baseexp(n,b):
    q = n
    k = 0
    a = []
    while q != 0:
        a.append(q % b)
        q = q // b
        k += 1
    return a

def modularexp(b, a, m):
    l1 = baseexp(a, 2)
    y = 1
    power = b % m
    for i in range(0, len(l1)):
        if l1[i] == 1:
            y = (y*power) % m
        power = (power*power) % m
    return y

def converttext(text):	             #converting string into list of integers
    text2 = ''    #TempString to store string in all lower case
    for i in range(0, len(text)):
        text2 += str.lower(text[i])
    
    key = "abcdefghijklmnopqrstuvwxyz ,.'" 
    coded = []
    for i in text2:
        for a in range(00, len(key)):
            if i == key[a]:
                coded.append("%02d" % a)
    tempstring = '' 
    strcoded = []   
    count = 0       
    for i in range(0, len(coded)):
        tempstring += str(coded[i])
        count += 1
        print tempstring
        if count == 2:
            count = 0
            strcoded.append(tempstring)
            tempstring = ''
  
    intcoded = []
    for i in range(0, len(strcoded)):
        intcoded.append(int(strcoded[i]))
    print intcoded
    return intcoded

def convertback(x):
    
    count = 0
    tempstring = ''
    intlist = []
    for i in x:
        count += 1
        tempstring += i
        if count == 4:
            intlist.append(int(tempstring))
            tempstring = ''
            count = 0
    print intlist    
    return intlist

    
        
def convertlisttotext(x):
    tempints = []
    for i in x:
        tempints.append(str("%04d" % i))
    
    ints = []
    tempstr = ''
    count = 0
    for i in tempints:
        for a in i:
            tempstr += a
            count += 1
            if count == 2:
                count = 0
                ints.append(int(tempstr))
                tempstr = ''
    key = "abcdefghijklmnopqrstuvwxyz ,.'"
    string2 = ''
    for i in ints:
        for a in range(0, len(key)):
            if i == a:
                string2 += key[a]
    print string2
    return string2
    
def rsaencrypt(text):
    numbers = converttext(text)
    values = []
    for i in numbers:
        values.append(modularexp(i, 17, 3233))
    print values
    tempstring = ''
    for i in values:
        tempstring += "%04d" % i
    print tempstring
    return tempstring
    
def rsadecrypt(text):
    intlist = convertback(text)
    
    values = []
    for i in intlist:
        values.append(modularexp(i, 2753, 3233))
    print values
    str = ''
    str = convertlisttotext(values)
    return str

encryptthis = "The Queen Can't Roll When Sand is in the Jar"
rsadecrypt(rsaencrypt(encryptthis))


