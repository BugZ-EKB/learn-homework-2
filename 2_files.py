"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main(text_file):
    with (open(text_file, 'r', encoding='utf-8') as ref,
          open('referat2.txt', 'w', encoding='utf-8') as ref_2):
        ref_str = ref.read()
        print(f'Длина строки {len(ref_str)} символов')

        ref_word = ref_str.replace('\n', ' ')
        ref_word_list = ref_word.split(" ")
        print(f'В файле {len(ref_word_list)} слов')

        ref_str = ref_str.replace('.', '!')
        ref_2.write(ref_str)

if __name__ == "__main__":
    main('referat.txt')
