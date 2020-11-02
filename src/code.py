#ponemos el abecedario para despues coger sus carácteres
abecedario = "abcdefghijklmnopqrstuvwxyz"
#instanciamos el diccionario que contendrá los valores de cada caracter
abc_value = {}
#creamos el diccionario completo
for i in range(len(abecedario)):
    abc_value[abecedario[i]] = i+1
def alphabet_position(text):
    text = text.lower()
    #aquí el texto procesado que nos pasan como parámetro
    processed_text = []
    #procesamos el texto
    for i in range(len(text)):
        #si es un carácter no válido me lo ignoras
        try:
            processed_text.append(str(abc_value[text[i]]))
        except KeyError:
            continue
    #me he fijado que join es mas rapido y ligero que una simple concatenacion entre strings.
    answer = " ".join(processed_text)
    return answer

#if __name__ == "__main__":
#    assert alphabet_position("The sunset sets at twelve o' clock") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
#    assert alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
