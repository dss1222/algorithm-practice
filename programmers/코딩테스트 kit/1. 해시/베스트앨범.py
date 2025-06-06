def solution(genres, plays):
    answer = []
    playDic = {}  # {장르 : 총 재생 횟수}
    dic = {}      # {장르 : [(플레이 횟수, 고유번호)]}
    
    # 해시 만들기
    for i in range(len(genres)):
        playDic[genres[i]] = playDic.get(genres[i], 0) + plays[i]
        dic[genres[i]] = dic.get(genres[i], []) + [(plays[i], i)]
    
    # 재생 횟수 내림차순으로 장르별 정렬
    genreSort = sorted(playDic.items(), key = lambda x: x[1], reverse = True)
    
    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, totalPlay) in genreSort:
        dic[genre] = sorted(dic[genre], key = lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in dic[genre][:2]]
    
    return answer

# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

from collections import defaultdict

def solution2(genres, plays):
    answer = []
    album_dict = defaultdict(int)
    play_dict = {}

    for i in range(len(genres)):
        album_dict[genres[i]] += plays[i]
        play_dict[genres[i]] = play_dict.get(genres[i], []) + [(plays[i], i)]

    sorted_album_dict = sorted(album_dict.items(), key=lambda x: x[1], reverse=True)

    for genre, total_play in sorted_album_dict:
        play_dict[genre] = sorted(play_dict[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in play_dict[genre][:2]]

    return answer

print(solution2(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

