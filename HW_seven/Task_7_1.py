#  Винни-Пух попросил Вас посмотреть,
# есть ли в его стихах ритм. Поскольку разобраться в его кричалках 
# не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и 
# “Пам парам”, если с ритмом все не в порядке.
krichalka = 'пара-ра-рам рам-пам-папам па-ра-па-да'
words = krichalka.split(" ") # формируем список из слов
print(words) 
def count_vowels(word): # создаем функцию по подсчету гласных в словах
    vowels = 'аеёиоуыэюя'
    count = 0
    for i in word: # проходим по буквам слова
        if i in vowels: # если буква находится в списке "vowels" считаем ее
            count += 1
    return count
vowel_count = list(map(count_vowels, words)) # формируем список из подсчитанных гласных
print(vowel_count)
if len(set(vowel_count)) == 1: # из списка 'vowel_count' создаем множество и проверяем его длинну
                                # если длина множесва =1, печатаем  условно-"да"
    print('Парам пам-пам')
else:
    print('Пам парам') # иначе "нет"