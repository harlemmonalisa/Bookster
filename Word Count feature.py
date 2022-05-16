#word count

#To edit the txt file name accordingly
file = open('char_Jekaterina.txt', 'r')
read_data = file.read()
per_word = read_data.split()

print('Total Words:', len(per_word))