def palindrom(phrase):
    cleaned_phrase = phrase.replace(" ", "").lower()
    ## Убираем пробелы и приводим к нижнему регистру
    return cleaned_phrase == cleaned_phrase[::-1]
    # Сравниваем строку с её обратным вариантом
input_phrase= input()
if palindrom(input_phrase):
    print("Palindrom")
else:
    print("Not polindrom")

