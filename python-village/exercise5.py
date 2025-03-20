"""
Problem

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
"""

path = '/home/diego/Downloads/rosalind_ini5(1).txt'

even_lines = []

with open(path,'r') as file:
    lines = [str(line).strip() for line in file]
    even_lines = [lines[i] for i in range(len(lines)) if i%2!=0]

file.close()
for line in even_lines: print(line)