"""
  Problem

Given: A string s
of length at most 200 letters and four integers a, b, c and d

.

Return: The slice of this string from indices a
through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
"""

def string_slice(s:str,a:int,b:int,c:int,d:int):
    slice1 = ''.join([str(x) for x in s[a:b+1]])
    slice2 = ''.join([str(x) for x in s[c:d+1]])
    return ' '.join([slice1,slice2])

example = string_slice("HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.",
22, 27, 97, 102)
# print(example)

test = string_slice("wXON67avbw0Bo2b9UovAqFX5FurciferE2VRFuVkIS47Se3jnGAweUmXennzsIkWdJpERolTIJrlopatiniXhHwyIAElts3deR3WvyU3UniEZNipZwRmuwOJYJutTYU7YG9HD3LK3heybobA6NVHR8WcmjOkvjV3J1eEVmo4K0aZ8Ou.",24, 31, 75, 82)
print(test)
