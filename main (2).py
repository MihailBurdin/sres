# задание№3
#def get_elem(d, k):
    #if k in d:
        #return d[k]
    #else:
        #return None
#my_dict = {'a': 1, 'b': 2, 'c': 3}
#key = 'b'
#result = get_elem(my_dict, key)
#print(result)  

#key = 'd'
#result = get_elem(my_dict, key)
#print(result) 
#задание№ 2
def list_insert(ref_list, start, num, rep):
    for _ in range(rep):
        ref_list.insert(start, num)
    return ref_list
my_list = [1, 2, 3, 4, 5]
start_position = 2
number = 9
repetitions = 3

result = list_insert(my_list, start_position, number, repetitions)
print(result)
#задание№1
def de_none(lst):
    return [x for x in lst if x is not None]
my_list = [1, None, 'hello', None, 5.5]
result = de_none(my_list)
print(result) 