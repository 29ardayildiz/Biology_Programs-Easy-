#It aims to find the repeating parts of a DNA sequence. 
#The code divides a DNA sequence into segments and counts how many times each segment is repeated. 
#As a result, it returns a dictionary, in which the number of repetitions for each part is shown.
#Searches for 5 nucleotide repeats inside the dna variable and returns the results as a dictionary

def count_repeats(dna_sequence, repeat_length):
    repeat_counts = {}
    for i in range(len(dna_sequence) - repeat_length + 1):
        repeat = dna_sequence[i:i+repeat_length]
        if repeat in repeat_counts:
            repeat_counts[repeat] += 1
        else:
            repeat_counts[repeat] = 1
    return repeat_counts

dna = "ATGCGATCGTAGCTAGCTACGATCGATCGATCGATCGATCGATCGATCG"
print(count_repeats(dna, 5))