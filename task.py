import os
import re

def prime_numbers(low, high):
    prime_list = []
    if (type(low) == int or type(low) == float) and (type(high) == int or type(high) == float) and low >= 2 and high >= low:
        seive = [i for i in range(int(high) + 1)]
        i = 2
        seive[1] = 0
        while i <= high:
            if seive[i] != 0:
                j = i + i
                while j <= high:
                    seive[j] = 0
                    j = j + i
            i = i + 1
        prime_list = [pr for pr in seive if pr != 0 and pr >= low]
    return prime_list



def text_stat(filename):
    d = {}
    if type(filename) != str:
        d['error'] = 'Incorrect argument type'
        return d
    if not os.path.exists(filename):
        d['error'] = 'File does not exist'
        return d
    with open(filename, 'r', encoding='utf-8') as inf:
        text = []
        for string in inf:
            text.append(string.lower().split())
    text = [x for x in text if x != []]
    d['paragraph_amount'] = len(text)
    d['bilingual_word_amount'] = 0
    words = 0
    for paragraph in text:
        for word in paragraph:
            if word == '–':
                continue
            words += 1
            next_word = True
            if bool(re.search('[a-zA-Z]', word)) and bool(re.search('[а-яА-Я]', word)):
                d['bilingual_word_amount'] += 1
            for letter in word:
                if letter.isalpha():
                    if letter not in d:
                        d[letter] = (1, 1)
                        next_word = False
                    elif next_word:
                        d[letter] = (d.get(letter)[0] + 1, d.get(letter)[1] + 1)
                        next_word = False
                    else:
                        d[letter] = (d.get(letter)[0] + 1, d.get(letter)[1])
    d['word_amount'] = words
    return d


def roman_numerals_to_int(roman_numeral):
    if not type(roman_numeral) == str:
        return
    roman_numeral.upper()
    d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    n = 0
    count = 1
    cur = ''
    rn_len = len(roman_numeral)
    i = 0
    while i < rn_len:
        if roman_numeral[i] not in d:
            return
        if cur == roman_numeral[i]:
            count += 1
        else:
            count = 1
        if count > 3:
            return
        cur = roman_numeral[i]
        if i < rn_len - 1 and d.get(roman_numeral[i]) < d.get(roman_numeral[i + 1]):
            s = roman_numeral[i] + roman_numeral[i + 1]
            i += 1
            if s in d:
                n += d.get(s)
            else:
                return
        else:
            n += d.get(roman_numeral[i])
        i += 1
    return n
