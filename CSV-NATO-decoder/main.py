import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_df = pandas.DataFrame(data)

new_dic = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(new_dic)

def generate_phonetic():
    user = input("Enter a word:\n").upper()
    try:
        nato_list = [new_dic[letter] for letter in user]
    except KeyError:
        print("Sorry only letters please")
        generate_phonetic()
    else:
        print(nato_list)

generate_phonetic()



