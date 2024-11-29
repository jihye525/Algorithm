import re

def solution(new_id):
    new_id = new_id.lower() # 1단계 대문자 -> 소문자
    new_id = re.sub("[^a-z0-9._-]", "", new_id) # 2단계 소문자 .-_를 제외한 모든 문자 제거
    new_id = re.sub("\.+", ".", new_id) # 3단계 '.'가 2번이상 반복될 때 '.'로 치환
    new_id = new_id.strip(".") # 4단계 문자열의 시작과 끝에 '.'가 있으면 제거
    if len(new_id) == 0: # 5단계 빈 문자열이라면 'a'룰 대입 + 7단계 문자열의 개수가 3이하면 3이상이 될 때까지 마지막 문자 반복
        new_id = 'aaa'
    else: # 6단계 아이디 길이가 16이상이면 16이상의 문자 제거 + 마지막 문자 '.'이면 제거
        new_id = new_id[:15]
        new_id = new_id.strip(".")
    if len(new_id) < 3: # 7단계 문자열의 개수가 3이하면 3이상이 될 때까지 마지막 문자 반복
        new_id = new_id + new_id[-1] * (3-len(new_id))

    return new_id