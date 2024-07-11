my_dict = {'Raven' : 'black', 'Swan' : 'white', 'Flamingo' : 'pink'}
print(my_dict)
print(my_dict['Swan'])
my_dict['Sparrow'] = 'brown'
print(my_dict['Sparrow'])
my_dict.update({'Eagle' : 'grey', 'Mockingbird' : 'white'})
print(my_dict)
bird = my_dict.pop('Sparrow')
print(bird)
print('these are all the birds whose names I remembered in English: ', my_dict)
print('and this is their number: ', len(my_dict), ', tweet-tweet >.<')

my_set = {True, 3.3, True, ('winter', 'summer'), 3.3, 8, 9}
print('Множество: ', my_set)
my_set.add(False)
my_set.add(65)
my_set.remove(('winter', 'summer'))
print('Обновленное множество: ', my_set)





