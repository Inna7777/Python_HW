#  В настольной игре Скрабл (Scrabble) каждая буква 
# имеет определенную ценность. В случае с английским алфавитом очки 
# распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; 
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; 
# J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, 
# которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

language = int(input('Введите- 0, если будете писать на  английском языке. Если на русском Введите- 1:'))
text =  input("введите слово ").upper()
sum = 0
dict_en = {1: 'AEIOULNSTR', 
            2 : 'DG', 
            3 : 'BCMP',
            4 : 'FHVWY',
            5 : 'K',
            8 : 'JX',
            10 : 'QZ',}
dict_ru = {1: 'АВЕИНОРСТ',
        2: 'ДКЛМПУ',
        3: 'БГЁЬЯ',
        4: 'ЙЫ',
        5: 'ЖЗХЦЧ',
        8: 'ШЭЮ',
        10: 'ФЩЪ'}
if language == 0:
    for i in text:    
        for k, v in dict_en.items():
            if i in v:
                sum += k
elif language == 1:
    for i in text:    
        for k, v in dict_ru.items():
            if i in v:
                sum += k
if sum == 0:
    print('Вы ввели слово неправильно ')
else:
     print(sum)