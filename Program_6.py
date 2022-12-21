#It aims to find repetitive parts in a DNA sequence and work on these repeats. 
#The code divides a DNA sequence into segments and counts how many times each segment is repeated. 
#It then calculates various properties of the repeats (for example, whether the segment is common, how many times the segment repeats in the DNA sequence) and stores these properties in a data frame. 
#Finally, it saves the dataframe to a file and shows the user the saved file path.

import pandas as pd

def analyze_repeats(dna_sequence, repeat_length, output_file):
    repeat_counts = {}
    for i in range(len(dna_sequence) - repeat_length + 1):
        repeat = dna_sequence[i:i+repeat_length]
        if repeat in repeat_counts:
            repeat_counts[repeat] += 1
        else:
            repeat_counts[repeat] = 1
    
    data = []
    for repeat, count in repeat_counts.items():
        occurances = dna_sequence.count(repeat)
        data.append({
            'repeat': repeat,
            'length': repeat_length,
            'count': count,
            'occurances': occurances
        })
    
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    
    print(f'Saved repeat data to {output_file}')

dna = "ATGCGATCGTAGCTAGCTACGATCGATCGATCGATCGATCGATCGATCG"
analyze_repeats(dna, 5, 'repeats.csv')
