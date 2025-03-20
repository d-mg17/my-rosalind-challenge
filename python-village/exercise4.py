"""Problem

Given: Two positive integers a
and b (a<b<10000).

Return: The sum of all odd integers from a
through b, inclusively.
"""
def sumOfOdds(a:int,b:int):
  return sum([i for i in range(a,b+1) if i%2!=0])

example= sumOfOdds(100,200)
# print(example)

test= sumOfOdds(4687,9026)
print(test)