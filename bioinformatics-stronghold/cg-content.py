def cgContentCounter(fasta_sequence: str) -> dict:
  identification, dna_sequence = fasta_sequence.split()
  
  c_content: int = dna_sequence.count("C")
  g_content: int = dna_sequence.count("G")
  cg_content: float = (c_content + g_content) / len(dna_sequence)
  
  return {
    identification : cg_content
  }

def dnaFastaParser(text: str) -> [str]:
  #! TODO: FIX FORMATING RECEPTION  
  fasta_sequences = text.split('>')
  return fasta_sequences[1:]

def mostCgContent(sequences: [dict]) -> str:
  sequences_values: [int]= [value for key, value in sequences.items()]
  most_cg_content_value: float = max(sequences.values())
  most_cg_content_key: str = [key for key, value in sequences.items() if value == most_cg_content_value][0]
  return f"{most_cg_content_key}\n{most_cg_content_value * 100:04f}"

def main():
  text = """>Rosalind_4871
TGCTTTCCTCGCTAAAACATCTTCGTCGCCCGTGGTCTGTTAGCCTCATAGGGGCGCTCATCATGCCGGCTCGATAACAATATGTGACTACCCCGATAGGCCGAAATTTTAGGATGAGGCTAGCGAACGAGTACCGTAAGTGGGTGAACCATCTTTGTTCGGTACCATACTGCACCTGTGTGCGCCTTGTTTATATAGATCAAGTGGGCGGCCATTGGTCGAGGGGCTTTGAACTAGTACCTGGCTACCTGCCACTGTGTGTTCATTGTCAATTGAAATCACAGATACAAGATATAGCCGCATCTTCCAGAGTGGATGAGGTCCGCGCTGTGTGATTCACGGGTGAGAAGAGTGCACGAGAGCACTGCACAGTGTTATTCATGCGAACACCATCGTTCACTTTGCACGACAAAAATTCGTTTGGGGATTCGAGTATAGTACTGGTAATCCGATGCGATTCTGATGCTGGGATGTGTTGTACAGGTGAGGCCGCTCGTGCTCTAGTACCCATGTACTTGCGCGTCCTAGTGGTCAAGTTGCCACTGGATATCTGAGTGTTACGGCACGACTCCTTTAGCTGTCTCTTAGAGTACGGCGACTTTGCTCTCAAAGGCTTTTCAGGCGCGTTCTGTGCTGCGAAGATTTCTGAATTTTAACTGAAGGCCCATGCCACTGAGATCTAATGTCTTAACAGAGCTCACCACGTTACAATTCCGGCATATTGGAGGTCCGCGTACATGCGGCTGTCCCGCGTTCAGTGAAGTCGCGAAGGGGTTCGGGTGGGTGTCTACCTTTGGCTGACTGGCTCATCAGCAGAATCCCGATGTACAGCCGTGCAC
>Rosalind_8547
TCGACTAATAATCGGCCTTACGTGCTCATTTCGCGTCGATACCTCAATAATTTCGCTAGTTCTCTCCTGCAAAGTTACGGTAACAGTATTAAATGAAGTATTTGGCCTCTGCATAAAGAATTTCGTTGGCACAAATGTGGGTAGCGGGGGTCGGTACAATCAACACCCAAAATAGCACTACTCTTGAAGTTTTAAATACGTCCCGGCTGTGCGCCGGCGATTCGTAACCACGGGTGAGAGTGCCGCTGTGTTGGCCGGTTGCGCATTAAATTCGCGTGTCTTAGCTGGTTCGCGATCTGCTAGATGGAGTAATTCGATAGTGAATGGCCTGCCCTTCACACTTATCATTCACTCGATCGACTTTGCTTAGTTTCTGCCTACGCAAAGCAGGCCCAAATCATTGTTCTAGGCAACACTCGTCGTGATCTCCCCCGGTGGAACGTACCTAATCATAGTGTATATTCTCACCGCCTGGTTTTGTTCATATGGACGACTAACGGTAAGACAGAGACTCAGAGCGTTCCATGTTTACGCTCCCAAGCGTCCTGAATTCGAGCTCCGGGAGATGCCCAAATCTCCTTGGTGCTCAATCAAATAACACACGATTTTCCGAATGGATGTCAATGGACTGGGATGATTTCTTACCGGCACACACTAACCGGCATTCGCTACTCAGACTCCGGCCTCAGGACAACATGAGTAATAGTATACGTGTTGCTACCGTGTTGAATTGGGTGAAAGTTCCTGTAGTGCGGTCCACTCGTCCTGCAGCTGCATGAAAGATTACCTGCCTCTCCTGTGCTTCGGTGCCTCCAAGCGAGACGTTGAAGCGATCGTTCGACCACGTGTCTATGTTGCAATCATGTGGCTAATACCATCCATATGGGTATTTATCGGCTGGGACACCTAAAACGAGGGCGCAAGACAGAAATACTTCCAAGGGCGGCGGGGGGGCCA
>Rosalind_6196
TAAACGACCGGTTCACCGACCTTAGGCACGGACGCCTATACATCGGAACACACGGCAACAGACAGTAGGCATGATGGCGTTAGTTCACTCTGTCCCTCTCAAACTCCTTGAAGGCTTGGTTGGCACCTAGTAACCCGGGACGCGATCGGATAGGTAGCACTACACACCCTCAAATCCGCACGTGACCGGGCGTACCTTAGTCATAAGGGAGTTGTCCAGATCAGAGGAAGGAAGCGTTGGGCAGGTTTCTTGAGTTTTTACAGCTTGCGTGGCTACCTTTAGGAGATATAGGGCGACGTATAACTCCATCCCCCCGAGGGCGGCTACATCGAATAGTCAGTCCTGAAAGAATTCCATATCTTCAATATCTTTTAGCACACTTCGCGTCCGTATCGTCCATACAGCGGAACAAATTCCACCAAGCTCTACCCGCGCCCACACCACTGGAAGGACGGATGGGACACACTTTCTACAGGTAGCTGATGGTAGCTCAGTAGAAAGACAAGGCGCAGATCACGGAGCAACAAAACACCGATGATGATAAGGTCACATGACACTAACCAACATCCTGTTCTGGATGAGTCTCGAGTCGCTCCCAGAAAAATGTGATGTTGAAGCGAAATGTTCTGAATCGTTACAACCCATCGAGTAATGACATTAGTGGCCAGGAATGCCTGCAAGATATGAGTCGTACCTGTGTCCGTCCACACATAATAAAGGCCACTTTTCTATTTCATGATCTAGCTGTGGAACCGATGCGCAAGGAACGCGTATGCTCGAATCGCTGCGTTATTCGAGGACTCTATGTCTATCCAGTACTCGACACTTTTACGGCCCTAGGGACAAGAATTTGTTCCTGCTAGATTCCAAGATATGGTCAGGC
>Rosalind_8689
ACGACATGCCATGCTGAGGCTGCCTCCCCGGCGACGATGCATATCCACCGTGGGATAATACCTGTCGGGCAGCGTCGGTACGTAATCACCTACATATACTATTTGATTTGAAGGTCTGGGTCCGTGGACGGGAAACAGGACCTCCCTTCAACGGTTTGTAGCTCAGGCGGAAGGATGCATCGGTTAAACGACCGGCAATCGGTCAACAAACTGTCAGACCCTGTGTATCATATACCCCGACACCTTATCTTGACACTACAATCCTCCCGCTTTCGTAGCCCTCGCTCATCGGGTTATTCATACAAGTAGCGGTCTTATGTGCGCCGTGGACATTATGGACACCGCAGGAACAATCCGCCACTGAGTCTAGGCTCTAGATCTAATGATGAGCACGATCATCGCTTGTTAAGCCAATGGGAAATGAGGGTATACCGAAGAATCGGCTTCACTACGGGTCTTATGGTCTTCGTCGCGCCACGTTGATGTCTATAACTAGGTTTCCATTACTGGGCCCATAAGACCACTGGCGACGTCTTAACACTATTCTTTATCTTGATAATAATTCCCGGGGATGTCTTGATGCGACATTACCATAGAAGGATCCGAGTGGTGAAAAAGGAACACCCAGTACCGATTGCAGGTTATTTTGACCGTTACTAGAATCTCCCCATTAGGACTAATTGAAACTACCGTCGAGACATCGGGACGCGAGTAATGGGGACTACAAGCCGGACCTAAACTTTCACAATGAAGGGCATTCCCCAAGGCACATGGGCAATGTTACCCTTGAGCTATATTCGGGGGGTTCTACTCTAGAGTCGCGATTAAGAGGCCCGGTCCCCTGGCATCTAACAGACGGGGTTGGTGCTCACGCTTAATAGGTCACCCGGTGAATTAACTTTACATCAATCGCGATCTATACCAATTAGCACCTATTCCCAGGAGGACTATGCCGATA
>Rosalind_1244
CTACTTAAGTGCATCATAGTTGCTTGGTGCTGGGACAGCCCACTACCTGCTTCCTTGAAGTTGACCAGGCACCGGCGATCCACGTCAGGCTTTCAGGAGGGCAGTGGACGCAGTCTCTCTATTTTACCTCCCATGGATTACCGCGAACGCGCCCGTTAGTATATTAAGTCGACACAATTAGTCGCATCTTTACTACACAGGAATGGAGAAGTATTCAGCCTCCAGGTATATACGCACGTACGTAACCATCGCATAGTTGTTCCGCTTAGATCGTTACCTAGCGTTAGCACATGCTGGCCCGTGTACTTCTTACCTTGGCGCGTGACGGGCCAGGTTGTCCGAAGTACCCTCCGCCAACGAGTTGGCACGATGGCAGATTGCCCGGGAGATGATATAGATTGCTAATATGACATGGTCAGAACTTATCGGCACTGCAAGGTAGAGAGGCGTCTCCAGATCTGGCACTCGAGAGCGTACATTTTCCCCAACGCTGTGATAAAAGACTATGTTCACCCGGCTAACTCCTTCGGATGATCGGAAGTTAGCAAGACTCAAAAAATATGGCGTTATTAATTTAGAAGTTGCACCTCAACAACAATATGATGATATCTGCGAAGGACCCCCAACACACGAACATCGTTAAAACAGCGGCCCACTTTTATTAGAGGGTGGTCGTCTTAGACAACGCCTTCACCTCTCCTTAGGTCGCAGCTAGAAGTCGGGTTACTTTGTATCTGCGCTGGTAAGATGATACGCACGACGCAATTACGACGGGGTGATCGCGTTGAGTAGAACTGGGCTAATGACGCTTATTTTCACAATAGGGTGGGTGGCAGATCGGTATTTCGTTAGTTGGGAATACAATCTGCAAGGAACGTATATCCGGGGCCTAACCTCGCCCCTAACGGCTTCAGGGGGCGCATAGGAGCCCTGATTCCATCAGCTTGTCGCTGGCGTGGGGGTTCCACGCTGGGAGGGGTAGGGAGA
>Rosalind_0092
GCGCTTCCATGTTACTACAGGTACCAGCTCTAGCAGACCGTACCTTGTATCAGAGGTGCGCGCCTAGGTTGATAGCCAGCTCCAAAATGTTAAAGATACATGACACGAATCCGCCTGGCCAAGCTCGAACTCACCGAAACAACTAACGCTTATTCCGGCCGAACGTGTTTTAGAGTGAGTGCTAGCCTGTTATCTGTGATTCTGCCTGTGGCCAGCACAACGAATGAGGGAACGTAGTATGGTTTGTCCCACTTTGAATACAATAGCAAAAAGCGCTCGCACAATGGCACAGGCCCTGTTTATCATCCCATACCCCTATTGGGTGTCTGCTGACTCCTGGAGCGACGCCCAGTAACGCTTATTGTGGGACGAACGACTAGTTCCCTTAGGCATCTTGGGAGGGTCCTGAACGGTGTCAACCGGGATTTCCGGTCTTAGAGGAACTATCCGAGAATGGCTCATCAGTGCTTCTTTTATTTATTTCACAGCTTCTCTCAGCCATTGTATCGCAAGTGGCCAAGCCATACCGTGCCACTTACTACCAGCTAAATCATAGACGGCGCCTCTAAACCCCGGATGACGCTGCGGCCGCCCTGAGACCATCGCATCTGGTTGTGTAGCGGAAAGCAACGGGTACAAGAACCCCTCGTGTTTGTCCATTAGGGTCGCCGCCGTAGACCAGACAACTTCAGAAAATGGCCATCTGGTTGAGCCGTGAGTGTAGCGGTGGCGCAGGGTTCATACATAATCATCCCACAGGTTGAACAACTGTTACTAAGCTATCGGTGACCCGACGTCTGCCATATTCCACGCCGCGATGATACGGAGACCAAGTCGCAATCCATCTGCATGGTGTGTAGATTGTGCATCTGTCGGCTGTTACACTATGTCAGGGGGACACAGGTAAGTAACATTTGGATGCGCGAATCCCGTCACCCAATCTATTGAGATACCCGCACGTTGGACAATTCAATTACCTGCACATTTGCC
>Rosalind_2348
ACCATCTAGCAATGGAAAAACCAGAACGTAGCAGAACGAACATGTGACTGCCAACTAATGTCCGTAAAGTTATTTCACTCCGTTGCCTGCGCGCGAGGAACGATGCGGTTCCGATCCGAACTAATTGTTTGATGATGCTGCGTAAAGGGGTTGGTCCCCAACACTGGGCCTCATGGGTGTTCCTGTCACCCACACTTAACCTTACCGGGTACTTGACGAAATGTTCTGCTAGGTCGCGGTGGACTTGTTCGGAAACCCTCGCGGGGAAATGCTAACTAACTATTGTTGGCATCATATGTATGCTCACTTAAACACTTTGTCTAAAGACGACAGTTCCAGCTGCTTAACCGATGTTTAATGGTTCATGTTACTTATATTGGTAGTTTCTAGGGGATTTTATTCAGATGGTCCCTATAACGGTCCCTAATTATAAATCGCATTGATAACACCAATCTCATTTTTTACACTCTGGGATAGGGCCCGATGTATGGTGTCTGTACTTACCCGGTTGTGAAGGCACGCGGCCTCCTGAGAACCCTGTTATAGCGCGGGTGTTCCACGCAATTTTAGTGACTATAAACACGGCTGAACTATGCTACCGTCCAAATTGTGCAGGGGGAGTTTTCTGCCTCAGTACCGTATCTAGGCTGCCTGCTGTCCAAAAACACCAAGGAGGCTTCGTGAGGTTAGACCGACGCGACAACCTCGCGGTTAGACTCTAAGGGTAGTAAATAACCGCACCTTCCCCCAAGGACTTTAGGTCATGGGTCGCCCTCGTGATCTATTGGGATAGAACAACTGCCTGAGT
>Rosalind_5166
CGGCTCATTAGCGTATATTACATGGTCGACAGAATTTTGTTTCACATCACACTGCTCAGATATAAAAAGGGCTTGGGTCCTGAGTCGTACCATCGATGAACCGTGCTTAATCTCGGTAATCGAAGCGACATTGGTGCGATGCAGGCACGACAAGTCTGGTGCATGCCGGCCTACGAACCAACTGTAAGGCAAGATTGACCTCGTCCGCTACCGCTTTGGCTAAGACGATTGAGGACTGTGGCTGTATCAGTGAGGGGACCTGGACAGAGCATCATCTTCGGGCCAATTGTGGAACGCAGGCCTGTGATAGTGGGCGTCTGTTACTGTTATGGACGTTGATTACGCTTGGATGCTGGGCAGTTTTTCCGGAGTAGAACGTTTCTACGAGGAGTCTCTACAGTCAAATGCAACGGCGCAGACCTGTGGCTTGATTTACAAGGAAAAACAAATTCCGACCAAGTAGGACAAGGGGTAGCCTGATCTATTAAATCTCTTCGGTTCACACAACCAACGCCTAATCCTCCCCACTGGGTAGTAGGTGCTAGCAACACATCGTAATACCCGGGTACCTACCGTCAGCTTCGCGGGCACTTATAGGCTTTACCGATCCAAGACTGGCTGCTGTTTGCAATGCTCCAAAATGGACCCGAAAACATTTTGTTGACTGTTAATGCTCTCATTACGGGTGTCGTCAATAATCTATAGGATACATAGCAAACTATTGTAGTCTCTGACGTATCTCTGCGTCCTTATTGCGAGCGTACACCCAGTGGCATCTTAAAAATGGTAGCTTTCACCCTACAGAAAGGCAAAATATGAGGTCTAATCCGACACTAAAGACTAGTCGAAAGAAGAGAGCAATTCTTGAACTTTCTACATGGCGCTTGGCTGGGGTAAAAACCGACCATTAAGTGATATCTCAGACCCTCGCAGATGGTTCGAGGTCTCCCTCGCTCTGCCCGTGGTGCTGAAATGAATTACTTTGCTAACGG
>Rosalind_5191
CCGAGTAGCGCGCTAGTAACCCATACACATTAAGTAGTTCACTGAAACGACCTTGAGGTTTTGTCCTGCAAAGTGTTTCCCAGCTGCGATTAGCGAAGCGTTCTAAGGACGAAGCCGTGTAGAGCACGTACCCATAGAAGCCAGCTCGGGATCAAATAGGTTAGCTACACATGTCTCCGTGCCCATACGCTTATGTGTCTTTCCATAGCGCAAATTCTACTCCGTGCCTTGATCAACAGTATCTTGGGTCCTGTTCTATTAACTGCATCCACAGCCAGCACGTAGCGGGACCCGCTGTGGCTAAAACCTACACTCACAATTCGCGGCGCGAATGCCTGCCGTTTATAGTGGAGGATGAATGATCCTATATCTAGCCGTTTCACACTGACGATATCAGCAAAGTGTCCTTACCGGCAAGCACCACATGGACCAAGCTTTCGACCAGGTAGAACTATAGTCCGTCGTTAGATAGATCAGATACCCGTGATTAACAAAGACGATGCTAATCGGTGGGTTGCTCCATGCGAAAACACTAGAAGAATATACGTGGTCCGAATAACGAGCGTTTAACTTCTACGCGCTTTTGGGGGCAGTGTGCCGTATCATACGCAGACCTGTGCCCTGGCCTACAGAATTTATGTACTCGGCATCTGCGCGGCCAAGCGGCACCAATCAAGTTCCAGAACGGGACTATGGATGCCTCACGAGCACGTACGTGCTCTCACACTCGGGTTGTGGACTTCCAAGAAAACGCTTCCAGCAATGCCCGTCGTCGTTGAAGCTCTGGAAGCATGGGAGGATAGATGCGGGCTGATCGCGCATGTTGACGGGTAACCGACGAAGTGCAATATAGTCGACACAGCGACCCGTCTGCAACTGGCGTTAAAGCCGACGATGGTCAGCCTGTAGCCTTAAGCCTTATGTTCCAGTGGTTGTGTTGAGCTCGGATCTACCCAT
>Rosalind_9618
TGATTATTGCCTTACTCAATATGGTGGTGGGGTGTTGGCTCCGAAAGCCGAACTGGGAAGGAGTTGATCGTCCGTCTGTCATGCGCTTCGATAGTGTGGCGTAATGGATTCGCTCCGGTTCGACCCCTTTTTTCTGCTGGACTTTTAAGCAAGATCTTACCCATTATTGCAACTTCGGAATCCTTTTGGCCGGCGTGACGGAATGAAGTACGTCAACTCCTACGCCACCTGATCCCCTTTAAGTCACACGAGCAGACGTATAAGCGTACTAGTAATCTCCACCAAAGAATATACGGGTAAAACTACCTGGAATCGTAAGGATTACGTGGTTATCAGCCATCTCCCTGACTTCTCTTAAGATCGCGAGGGACTCATGGCGTTTCAGTCGGGGCCTTGGGCAGCGCCCCACTAAGCCGTGCCGAGGGAGATATAGTGGTTCGTACCACCATTAAAGAAGAGTTAGACTGCCTGTAAAAGATCTCGCTGACATACGTCGGTCGCCCACGTCATGTAACCTCTCCACTTTCGTCTATTCCCTTTTCACCATATAGGAAAAGTTTCGGTAGTCACGTAGTTACAGCGTCCTCTCGTCGGTTTCATACGGAGCATAATAAACGTTTATTTTCCCTAGTGATGATTAACTGCAAGTCACTTTTCTTGTAACAAAAGAGTATTTGCTTTTTCTTGCACGTTTAAATAGAGTTCCTAGCGCGCCAACTGGCCTATCTTGATACAGTCTTCAATTGCACTCTCGGTGTCAAGGTAGGATCGTTCCTTAAGATGACCGGCACACCTAGATAATGCCCGTATGTAAAGCATATACGGCGGGTTGCCTACTAGGGGATAGGGTCGTGAAATACAGAACCGCAGCGTCTTCTGTGGTATCTAAGCCATGCCTATAACCG"""
  
  sequences: [str] = dnaFastaParser(text=text)
  
  cg_content_dict: {dict} = {}
  for sequence in sequences:
    for key, value in cgContentCounter(sequence).items():
      cg_content_dict[key] = value
  
  most_cg_content_sequence: str = mostCgContent(cg_content_dict)
  print(most_cg_content_sequence)

if __name__ == "__main__":
  main()
