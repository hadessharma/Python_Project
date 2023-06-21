
with open(file='./nato-project/nato_phonetic_alphabet.csv', mode='r') as file:
    data = file.read().splitlines()
    

#TODO 1. Create a dictionary in this format:
student_dict = { array[0]:array[1] for array in ([i.split(',') for i in data]) if array[0] != 'letter'}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

inputword = input('Enter a word: ').upper()
output_list = [student_dict[letter] for letter in inputword]
print(output_list)