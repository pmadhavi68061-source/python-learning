# counts A, T, G, C bases in a DNA sequence
def count_bases(dna):
    dna=dna.upper() #converts small letters to capital

    #count each base using dictionary
    counts={
        'A': dna.count('A'),
        'T': dna.count('T'),
        'G': dna.count('G'),
        'C': dna.count('C')
    }
    return counts
def main():
    # Take DNA sequence input from user
    dna=input("Enter DNA sequence: ")

    #check if sequence input from user
    for base in dna.upper():
        if base not in "ATGC":
            print("Invalid character found: ",base)
            return
    
    # call the count function
    result=count_bases(dna)

    # Display results
    print("\n---Base Count Results---")
    for base, count in result.items():
        print(f"{base}: {count}")

    # Display total base count
    print(f"\nTotal bases: {sum(result.values())}")

# Run the program
main()

                                            