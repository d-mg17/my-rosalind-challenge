"""
Problem

Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, 
where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
"""

def wordCounter(s:str) -> str:
  """Counts the occurrences of each word in a given string

  Args:
      s (str): given string

  Returns:
      str: List of words and occurances
  """
  counter = dict()
  words = s.split(" ")
    
  for word in words:
    if word in counter.keys():
      counter[word] += 1
    else:
      counter[word] = 1
  
  result = ""
  for item in counter.items():
    word = item[0]
    count = item[1]
    result += f"{word} {count}\n"
  
  return result

example = wordCounter("We tried list and we tried dicts also we tried Zen")
# print(example)

test = wordCounter("When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be")

print(test)