def recurrenceRabbit(months: int, rabbits: int) -> int:
  if months == 0 or months == 1: 
    return 1
  
  elif months == 2: 
    return rabbits
  
  elif months <= 4:
    return recurrenceRabbit(months-1,rabbits) + recurrenceRabbit(months-2,rabbits)

  else:
    return recurrenceRabbit(months-1,rabbits) + (recurrenceRabbit(months-2,rabbits) * rabbits)

def main():
  rabbits = recurrenceRabbit(28, 3)
  print(rabbits)

if __name__ == "__main__":
  main()