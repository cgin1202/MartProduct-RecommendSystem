# from pymongodb import dbconnection
import math
import operator

def getavg(data_table, num_items, x):
    result = 0
    count = 0
    for i in range(num_items):
        if data_table[x][i] == 0:
            continue
        result += data_table[x][i]    
        count += 1
    return(float(result/count))

def pearson(data_table, num_items, x, y):
    result = 0
    avg_x = getavg(data_table, num_items, x)
    avg_y = getavg(data_table, num_items, y)
    result_top = 0
    result_bottom_left = 0
    result_bottom_right = 0
    for i in range(num_items):
        if (not data_table[x].get(i)) or (not data_table[y].get(i)):
            continue
        IX = float(data_table[x][i]) - avg_x
        IY = float(data_table[y][i]) - avg_y
        result_top += IX * IY
        result_bottom_left += IX * IX
        result_bottom_right += IY * IY
    result += result_top
    result_bottom = math.sqrt(result_bottom_left) * math.sqrt(result_bottom_right)
    if(result_bottom == 0):
        return 0
    result /= result_bottom
    if(math.isnan(result)):
        return 0
    return result    

def get_rating(data_table, most_sim_users, reco_user, num_items, i):
    result = 0
    k_right = 0
    result_right = 0
    for u in most_sim_users:
        u_prime = u[0]
        if data_table[u_prime][i] is 0:
            continue
        k_right += abs(u[1])
        result_right += u[1] * (data_table[u_prime][i] - getavg(data_table, num_items, u_prime))
    if k_right == 0:
        return 0
    k = 1 / k_right
    result = getavg(data_table, num_items, reco_user) + k * result_right
    return result


def getcfratings(data_table, reco_user, num_items):
    num_sim_user_topk = 3
    num_item_rec_topk = 5
    sim_users={}
    for key, value in data_table.items():
        if(key is reco_user):
            continue
        pearson_value = pearson(data_table, num_items, reco_user, key)
        if(pearson_value is 0):
            continue
        sim_users[key] = pearson_value

    sim_users = sorted(sim_users.items(), key=lambda x:x[1], reverse=True)

    most_sim_users = []
    for i in range(num_sim_user_topk):
        most_sim_users.append(sim_users[i])

    ratings = []
    for i in range(num_items):
        if data_table[reco_user][i] is not 0:
            continue
        ratings.append((i, get_rating(data_table, most_sim_users, reco_user, num_items, i)))
    ratings = sorted(ratings, key=lambda x:x[1], reverse=True)

    most_ratings = []
    for i in range(num_item_rec_topk):
        most_ratings.append(ratings[i])
    result = {}
    result['sim_users'] = sim_users
    result['ratings'] = most_ratings
    return result

