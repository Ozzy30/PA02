



def convert_to_standard(a1,a2,b1,b2):
    a = (a1,a2)
    b = (b1,b2)
    return a1,a2,b1,b2

def intersects(h,a1,a2,b1,b2):
    return None

def get_delta_x1(a1,b1):
    if b1>a1:
        if 0 < a1 < 6:
            return 6 - a1
        elif 0 < b1 < 6:
            return b1
        else:
            return 6
    else:
        if 0 < b1 < 6:
            return 6 - b1
        elif 0 < a1 < 6:
            return a1
        else:
            return 6
        

def get_delta_x2(h,a2,b2):
    if b2>a2:
        #Für a2
        if 0 < a2 < h:
            if b2 < h:
                return b2 - a2
            else:
                return h - a2
        #Für b2
        elif 0 < b2 < h:
            if a2 > 0:
                return b2 - a2 
            else:
                return b2
        #Für beides
        else:
            return h
    else:
        #Für b2
        if 0 < b2 < h:
            if a2 < h:
                return a2 - b2
            else:
                return h - b2
        #Für b2
        elif 0 < a2 < h:
            if b2 > 0:
                return a2 - b2 
            else:
                return a2
        #Für beide
        else:
            return h

def get_lattice_point_number(h,a1,a2,b1,b2):
    if h<0:
        return "Die Eingabe ist fehlerhaft."
    #Ecken
    boLe = (a1,a2)
    toLe = (a1,b2)
    boRi = (b1,a2)
    toRi = (b1,b2)
    #convert_to_standard(a1,a2,b1,b2)





    return None

#print(convert_to_standard(1,2,3,4))
print(get_delta_x1(4, 2))

#print(get_delta_x2(16, 7, 6))