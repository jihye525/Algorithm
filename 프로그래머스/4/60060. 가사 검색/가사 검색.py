from collections import defaultdict

def solution(words, queries):
    answer = [0] * len(queries)
    queries_dict = dict()
    length_dict = defaultdict(list)
    start_dict = defaultdict(list)
    end_dict = defaultdict(list)

    for word in words:
        length_dict[len(word)].append(word)
        end_dict[(len(word), word[-1])].append(word)
        start_dict[(len(word), word[0])].append(word)

    for i, pattern in enumerate(queries):
        if pattern in queries_dict:
            answer[i] = queries_dict[pattern]
        else:
            if pattern.startswith("?") and pattern.endswith("?"):
                answer[i] = len(length_dict[len(pattern)])
            elif pattern.startswith("?"):
                for word in end_dict[(len(pattern), pattern[-1])]:
                    answer[i] += 1 if word.endswith(pattern.replace("?","")) else 0
            else:
                for word in start_dict[(len(pattern), pattern[0])]:
                    answer[i] += 1 if word.startswith(pattern.replace("?","")) else 0
            queries_dict[pattern] = answer[i]

    return answer