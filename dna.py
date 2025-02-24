import csv
import sys


def main():
    # Verificar se passou os argumentos
    if len(sys.argv) != 3:
        print('''Missing command-line argument
Use: python dna.py large.csv sequence.txt''')
        sys.exit()

    # Ler arquivo bd
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        database = list(reader)

    # Ler arquivo de sequência de DNA em uma variável
    with open(sys.argv[2]) as file:
        sequence = file.read()

    # Ignorar campo de nome
    strs = reader.fieldnames[1:]

    # Encontrar a correspondência mais longa de cada STR na sequência de DNA
    str_counts = {}
    for str_seq in strs:
        str_counts[str_seq] = longest_match(sequence, str_seq)

    # comparacao de dados por perfis correspondentes
    for person in database:
        match = True
        for str_seq in strs:
            if int(person[str_seq]) != str_counts[str_seq]:
                match = False
                break
        if match:
            print(person['name'])
            return

    # Se não encontrar ninguém
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Inicializar variáveis
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Verificar cada caractere na sequência para encontrar a maior execução consecutiva da subsequência
    for i in range(sequence_length):

        # Inicializar contagem de execuções consecutivas
        count = 0

        while True:

            # Ajustar início e fim da substring
            start = i + count * subsequence_length
            end = start + subsequence_length

            # Se houver uma correspondência na substring
            if sequence[start:end] == subsequence:
                count += 1

            # Se não houver correspondência na substring
            else:
                break

        # Atualizar o maior número de correspondências consecutivas encontradas
        longest_run = max(longest_run, count)

    # Após verificar as execuções em cada caractere da sequência, retornar a maior execução encontrada
    return longest_run


main()
