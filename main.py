def corresponding_parenthesis(text):

    result = text
    direita = 0
    esquerda = 0
    parenteses = 0

    for letter in result:
        if letter == "(":
            esquerda += 1
        else:
            direita += 1

    if direita >= esquerda:
        parenteses = (direita - esquerda)
        result = [")"*parenteses]
    else:
        parenteses = (esquerda - direita)
        result = ["("*parenteses]

    result = "".join(result)
    return result


def remove_more_than_two_repetitions(text):
    text = [letter for letter in text]
