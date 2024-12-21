from collections import defaultdict

##Dict
sammy = {'username':'sammy_shark', 'online':True, 'followers':987}
jesse ={'username':'JOctopus', 'online':False, 'points':723}

print(sammy.values())
print(sammy.items())

for key, value in sammy.items():
    print(key, 'is the key for the value',value)


for common_key in sammy.keys() & jesse.keys():
    print(sammy[common_key], jesse[common_key])

jesse.update({'followers': 481})

del jesse['points']

print(jesse)

##Combine lists into dict

keys =['a', 'b', 'c']
values=[1, 2, 3]

dictionary = dict(zip(keys,values))

print(dictionary)

##Slice
a=['a', 'b', 'c', 'd','e','f','g']

print('Middle two: ', a[3:5])
print('All but ends', a[1:7])
print(a[::3])

##defaultdict
def create_author_count_mapping(cookbooks: list[cookbook]):
    counter = defaultdict(lambda: 0)
    for coocbook in cookbooks:
        counter[coocbook.author] +=1
    return counter

#Tuple
weekdays_tuple =('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

item = ('Butter', 'Jelly')
first, second = item #unpacking
print(first,' and ', second)

def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[1] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1] #swap

names = ['pretzel', 'carrots', 'arugula', 'bacon']
print(names)
bubble_sort(names)
print(names)                

##Iteration
text ='Some text'
index = 0

# while index < len(text):
#     print(text[index])
#     index += 1

for char in text:
    print(char)