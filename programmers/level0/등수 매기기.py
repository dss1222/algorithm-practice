def solution(score):
    avg = [sum(s)/2 for s in score]
    sorted_avg = sorted(avg, reverse=True)
    
    result = []
    for a in avg:
        result.append(sorted_avg.index(a) + 1)
        
    return result