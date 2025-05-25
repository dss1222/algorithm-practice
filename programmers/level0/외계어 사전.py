from itertools import permutations

def solution(spell, dic):
    answer = 2
    for i in permutations(spell, len(spell)):
        if ''.join(i) in dic:
            answer = 1
            break
    return answer

def solution2(spell, dic):
    spell_sorted = ''.join(sorted(spell))
    for word in dic:
        if ''.join(sorted(word)) == spell_sorted:
            return 1
    return 2