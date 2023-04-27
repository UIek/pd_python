from random import randint

my_list = [23, 30, 45, 90, 71, 73, 92, 55, 13, -55, 2, -79,
 94, -83, 40, -9, 82, 41, -81, -84, -100, -84, 2, 56, -93, 83, 
 69, 31, -95, 71, 36, 75, -100, 98, -48, -98, 41, -61, 86, 28, 
 -16, 94, 88, -100, 55, -66, 88, -72, 94, 11, 66, -63, -81, 58, 
 -23, -78, 86, -100, 57, -86, -37, -31, 70, -51, 60, -41, 30, 6, 
 -5, 36, 92, -73, 40, -93, -74, 21, -15, 39, 60, 95, 81, -71, 3, 35, 
 -9, -9, 75, 40, -81, 20, -39, -34, -29, 99, 46, 95, -80, -81, -44, -91]


def nieujemne(my_list):
    new_list = []
    for i in my_list:
        if i >= 0:
            new_list.append(i)
    return(len(new_list))





def parzyste(my_list):
    sum = 0
    for i in my_list:
        if i % 2 == 0:
            sum += i
    return(sum)



def nieparzyste(my_list):
    sum = 0
    for i in my_list:
        if i % 2 != 0:
            sum += i
    return(sum)



def podzielne_przez_5_i_7(my_list):
    sum = 0
    for i in my_list:
        if i % 5 == 0 and i % 7 == 0:
            sum += i
    return(sum)



def xxx(my_list):
    while True:
        te_same = 0
        inp = (input())
        if inp == "stop":
            break
        for i in my_list:
            if i == int(inp):
                te_same += 1
    return(te_same)


def igfaubv():
    lista = []
    start = int(input())
    stop = int(input())
    step = int(input())
    for i in range(start,stop,step):
        lista.append(i)
    return(lista)



