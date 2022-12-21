#counts the order of adenine, guanine, cytosine and thymine of a DNA sequence and returns the results as a dictionary.

def count_nucleotides(dna_sequence):
    nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in dna_sequence:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1
    return nucleotide_counts

dna = "ATGCGATCGTAGCTAGCTACGATCGATCGATCGATCGATCGATCGATCG"
print(count_nucleotides(dna))