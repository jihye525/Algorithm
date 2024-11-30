def to_days(y, m, d):
    return (y * 12 * 28) + (m * 28) + d


def solution(today, terms, privacies):
    answer = []
    t_y, t_m, t_d = map(int, today.split("."))
    today_days = to_days(t_y, t_m, t_d)

    terms_dic = dict()
    for t in terms:
        p, m = t.split()
        terms_dic[p] = int(m)

    for i in range(len(privacies)):
        date, policy = privacies[i].split()
        yyyy, mm, dd = map(int, date.split("."))

        if to_days(yyyy, mm + terms_dic[policy], dd) <= today_days:
            answer.append(i + 1)

    return answer
