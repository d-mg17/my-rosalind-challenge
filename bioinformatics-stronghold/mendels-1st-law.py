def probabilityDominant(k: int, m: int, n: int) -> float:
  prob: float = 0.0
  total:int = (k + m + n)
  
  path1 = (n/total)*((n-1)/(total-1))
  path2 = (n/total)*(m/(total-1))*0.5
  path3 = (m/total)*(n/(total-1))*0.5
  path4 = (m/total)*((m-1)/(total-1))*0.25
  
  prob:float = 1 - (path1 + path2 + path3 + path4)
  
  return float(f"{prob:.5f}")

def main():
  
  numbers = "24 25 20"
  number_list = numbers.split(" ")
  
  k:int = int(number_list[0])
  m:int = int(number_list[1])
  n:int = int(number_list[2])
  
  dominant_probability = probabilityDominant(k,m,n)
  
  return print(dominant_probability)

if __name__ == "__main__":
  main()