def output() -> None:
    try:
        inputword = input('Enter a word: ').upper()
        output_list = [student_dict[letter] for letter in inputword]
        print(output_list)
    except KeyError:
        print('Sorry! Only letters and alphabets please!')
        output()
        
        
with open(file='./nato-project/nato_phonetic_alphabet.csv', mode='r') as file:
    data = file.read().splitlines()
    
student_dict = { array[0]:array[1] for array in ([i.split(',') for i in data]) if array[0] != 'letter'}

output()