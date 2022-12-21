#It aims to find repetitive parts in a DNA sequence and work on these repeats. 
# The code divides a DNA sequence into segments and counts how many times each segment is repeated. 
# It then calculates various properties of the repeats (for example, whether the segment is common, how many times the segment repeats in the DNA sequence) and stores these properties in a data frame.

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
    
    with open(output_file, 'w') as f:
        f.write('repeat,length,count,occurances\n')
        for row in data:
            f.write(f"{row['repeat']},{row['length']},{row['count']},{row['occurances']}\n")
    
    print(f'Saved repeat data to {output_file}')

dna = "ATGCGATCGTAGCTAGCTACGATCGATCGATCGATCGATCGATCGATCG"
analyze_repeats(dna, 5, 'repeats.csv')
