def solution(friends, gifts):
    num = len(friends)
    gift_list = [[0] * num for _ in range(num)]
    gift_score = [0] * num
    future_gift = [0] * num
    
    for x in gifts:
        give = friends.index(x.split(" ")[0])
        given = friends.index(x.split(" ")[1])
        gift_list[give][given] += 1
        
        gift_score[give] += 1
        gift_score[given] -= 1
        
    for x in range(num):
        for y in range(num):
            if gift_list[x][y] > gift_list[y][x]:
                future_gift[x] += 1
            elif gift_list[x][y] == gift_list[y][x]:
                if gift_score[x] > gift_score[y]:
                    future_gift[x] += 1
       

    return max(future_gift)