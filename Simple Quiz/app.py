import string

alphabet = [i for i in string.ascii_lowercase]

questions = ['Siapa nama presiden pertama Indonesia?', "Berapa hasil dari 2 + 2?", "Apa Kepanjangan dari SIM?"]
answers = [['Ir. Soeharto', 'Drs Moh Hatta', 'Soeharto', 'Gus Dur'],
           ['6', '5', '4', '8'],
           ['Surat Izin Mengemudi', 'Surat Ini Mudah', 'Surat Indah Mall', 'Syarat izin Menikah']
           ]

answers_key = [0, 2, 0]
user_answers = []
for ind, question in enumerate(questions):
    print(f"{ind + 1}. {question}")
    for ind, answer in enumerate(answers[ind]):
        print(f"{alphabet[ind]}. {answer}")

    user_answer = input("Apa Jawaban Anda  (a, b, c, atau d): ")
    user_answers.append(alphabet.index(user_answer.lower()))
    print("=" * 20)

score = 0
for i in range(len(answers_key)):
    if answers_key[i] == user_answers[i]:
        score += 1

score = score / len(answers_key) * 100

print("NIlai Anda adalah :", round(score, 2))