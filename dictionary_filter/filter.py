def filter_words(input_file, output_file):
    with open(input_file, 'r') as f:
        words = f.readlines()
    
    filtered_words = [
        word for word in words
        if word.strip().islower() and "'" not in word and len(word.strip()) > 3
    ]
    
    with open(output_file, 'w') as f:
        f.writelines(filtered_words)


filter_words('en_US_60_SB.txt', 'SB_en_US.txt')




