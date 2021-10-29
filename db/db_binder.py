import sqlite3 as sql
import json
import datetime as dt


FLAG_CHANGE_SUCCESS = 1
FLAG_CHANGE_FAIL = 0

def initDB():
    conn = sql.connect('db/insuranceDB.db')

    with open('db/create_db.json') as json_file:
        cr_in = json.load(json_file)
    for i in cr_in:
        cursor = conn.cursor()
        script = cr_in[i]
        cursor.execute(script)
        conn.commit()
    return True

def allInsurances():

    conn = sql.connect('DB/insuranceDB.db')

    cursor = conn.cursor()
    req0 = "SELECT key, name, FLAG  FROM \"insurances\""
    cursor.execute(req0)
    ret = cursor.fetchall()
    res = dict()

    for insur in ret:
        res[insur[0]] = dict()
        res[insur[0]]["name"] = insur[1]
        res[insur[0]]["FLAG"]  = insur[2]

    return res


def searchInsuranceByKey(idInsurance):
    

    conn = sql.connect('DB/insuranceDB.db')
    
    cursor = conn.cursor()
    req0 = "SELECT name, FLAG  FROM \"insurances\" WHERE key LIKE \"{0}\" ".format(idInsurance)
    cursor.execute(req0)
    ret = cursor.fetchall()
    res = dict()

    if len(ret) > 0:
        res["name"] = ret[0][0]
        res["flag"] = ret[0][1]

    else:
        return -1

    return res


def createInsurance(idInsurance,n,f):

    conn = sql.connect('DB/insuranceDB.db')
    cursor = conn.cursor()
    req0 = "SELECT id FROM \"insurances\" WHERE key LIKE \"{0}\" ".format(idInsurance)
    cursor.execute(req0)
    ret = cursor.fetchall()

    if len(ret) > 0:
        return False
    else:
        req1 = "INSERT INTO \"insurances\" (key,name,FLAG ) VALUES (\"{0}\",\"{1}\",\"{2}\")".format(idInsurance,n,f)
        print(req1)
        cursor.execute(req1)
        conn.commit()
        return True



def updateFlag(idInsurance):
    
    conn = sql.connect('DB/insuranceDB.db')

    cursor = conn.cursor()
    req0 = "SELECT FLAG, name  FROM \"insurances\" WHERE key LIKE \"{0}\" ".format(idInsurance)
    cursor.execute(req0)
    ret = cursor.fetchall()

    res = dict()

    if len(ret) > 0:
        # Cas où il trouve
        res["name"] = ret[0][1]
        if(ret[0][0] == 1):

            req1 = "UPDATE \"insurances\" SET FLAG = 0 WHERE key LIKE \"{0}\"".format(idInsurance)
            cursor.execute(req1)
            conn.commit()

            res["change_success"] = FLAG_CHANGE_SUCCESS
            return res
        elif (ret[0][0] == 0):
            res["change_success"] = FLAG_CHANGE_SUCCESS
            req2 = "UPDATE \"insurances\" SET FLAG = 1 WHERE key LIKE \"{0}\"".format(idInsurance)
            cursor.execute(req2)
            conn.commit()
            return res
        else:
            return -1
    else:
        # Cas où il ne trouve pas
        return -1