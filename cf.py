from pymongodb import dbconnection
import math
def getavg(data_table, num_items, x):
    result = 0
    count = 0
    print(data_table[str(x)])
    for i in range(1,num_items+1):
        if not data_table[str(x)].get(str(i)):
            continue
        result += data_table[str(x)][str(i)]    
        count += 1
    return(result/count)
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
        IX = data_table[str(x)][str(i)] - avg_x
        IY = data_table[str(y)][str(i)] - avg_y
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


def get_result(data_table, num_items, reco_user):
    sim_users={}
    for i in data_table:
        if(i == reco_user):
            continue
        pearson_value = pearson(data_table, num_items, reco_user, i)
        print(pearson_value)
        if(pearson_value == 0):
            continue
        sim_users[i] = pearson_value
    print(sim_users)


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
    #print(data_table)    
    get_result(data_table, 70, 1000)
getcfratings(2,2, 70)