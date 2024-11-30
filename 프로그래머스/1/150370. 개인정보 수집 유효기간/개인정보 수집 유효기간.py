def solution(today, terms, privacies):
    answer = []
    t_y, t_m, t_d = map(int, today.split("."))
    terms_dic = dict()
    for t in terms:
        p, m = t.split()
        terms_dic[p] = int(m)

    for i in range(len(privacies)):
        date, policy = privacies[i].split()
        yyyy, mm, dd = map(int, date.split("."))

        e_m = mm + terms_dic[policy]
        yyyy += (e_m - 1) // 12
        mm = ((e_m - 1) % 12) + 1

        if yyyy < t_y or (yyyy == t_y and mm < t_m) or (yyyy == t_y and mm == t_m and dd <= t_d):
            answer.append(i+1)

    return answer