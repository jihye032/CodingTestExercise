# https://blog.naver.com/jihae032/222451182944

def solution(n, lost, reserve):
    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve) - set(lost)

    answer = n - len(set_lost)
    for i in set_lost:
        if i-1 in set_reserve :
            set_reserve.remove(i-1)
            answer += 1
        elif i+1 in set_reserve :
            answer += 1
            set_reserve.remove(i+1)

    return answer