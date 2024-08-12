scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

def count_scores(word, scores_list):
    score_count = 0
    for symb in str(word):
        if symb == 'Ё':
            score_count += 1
        else:
            for key, val in scores_list.items():
                if symb in val:
                    score_count += key
                    break
    return score_count
    
word = input().upper()
result = count_scores(word, scores_letters)
print(result)

'''
Примеры:
котлеты
12

синхрофазотрон
29
'''