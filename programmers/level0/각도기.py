#http://vod.klli.kr/player/player_m.asp?groupcode=kllo.kr&lec_idx=285&partNum=010000&userid=suk842661&gisuYear=2025&gisuNum=15&injection=except
def solution(angle):
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle < 180:
        return 3
    elif angle == 180:
        return 4