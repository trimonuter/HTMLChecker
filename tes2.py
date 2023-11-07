# transitions = {
#     'q': {
#         'a': 'hello',
#         'b': 'hi'
#     }
# }

# a = 'q'
# b = 'c'

# if a in transitions:
#     if b in transitions[a]:
#         print(transitions['q']['c'])
#     else:
#         print("Key not found")
        
a = {
    'b': 1,
    'c': 2,
    'd': 9,
    'e': 17
}

l = ['b', 'c', 'd', 'e']
for x in l:
    print(a[x])