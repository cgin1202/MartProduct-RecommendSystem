from pymongodb import dbconnection
import math
import operator
def getavg(data_table, num_items, x):
    result = 0
    count = 0
    #print(data_table[str(x)])
    for i in range(1,num_items+1):
        if not data_table[str(x)].get(str(i)):
            continue
        result += data_table[str(x)][str(i)]    
        count += 1
    return(float(result/count))
def pearson(data_table, num_items, x, y):
    result = 0
    avg_x = getavg(data_table, num_items, x)
    avg_y = getavg(data_table, num_items, y)
    result_top = 0
    result_bottom_left = 0
    result_bottom_right = 0
    for i in range(1, num_items+1):
        if (not data_table[str(x)].get(str(i))) or (not data_table[str(y)].get(str(i))):
            continue
        IX = float(data_table[str(x)][str(i)]) - avg_x
        IY = float(data_table[str(y)][str(i)]) - avg_y
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

def get_rating(data_table, U, reco_user, num_items, i):
    result = 0
    k_right = 0
    result_right = 0
    for u in U:
        u_prime = u[0]
        if not data_table[u_prime].get(str(i)):
            continue
        k_right += abs(u[1])
        result_right += u[1] * (data_table[u_prime][str(i)] - getavg(data_table, num_items, u_prime))
    if k_right == 0:
        return 0
    k = 1 / k_right
    result = getavg(data_table, num_items, reco_user) + k * result_right
    return result



def get_result(num_sim_user_topk, num_item_rec_topk, data_table, num_items, reco_user):
    sim_users={}
    for i in data_table:
        if(int(i) == reco_user):
            continue
        pearson_value = pearson(data_table, num_items, int(reco_user), int(i))
        #print(pearson_value)
        if(pearson_value == 0):
            continue
        sim_users[i] = pearson_value

    sim_users = sorted(sim_users.items(), key=lambda x:x[1], reverse=True)
    U = []
    for i in range(0, num_sim_user_topk):
        U.append(sim_users[i])
    #print(U)
    ratings = []
    for i in range(1, num_items+1):
        if data_table[str(reco_user)].get(str(i)):
            continue
        ratings.append((i, get_rating(data_table, U, reco_user, num_items, i)))
    #ratings.sort(reverse=True)

    ratings = sorted(ratings, key=lambda x:x[1], reverse=True)
    #print(ratings)
    for i in range(0, num_item_rec_topk):
        print(ratings[i][0])


def getcfratings(num_sim_user_topk, num_item_rec_topk, num_items):
    mydb = dbconnection()
    mycol = mydb["ratings"]
    num_users = mycol.count_documents({})
    data_table = {}
    for x in mycol.find():
        data = {}
        for y in x['item']:
            data[str(y)] = x['item'][y]
        data_table[str(x['id'])] = data 
    get_result(80, 20, data_table, 70, 2)
getcfratings(2,2, 70)
