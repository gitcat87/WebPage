import pymysql


host='192.168.0.66'
port=3306
user='root'
password='root123'
dbname='DHchoi'
charset='utf8'



def selectRow(idx):
    db = pymysql.connect(
        host=host, port=port,
        user=user, password=password,
        db=dbname, charset=charset
    )
    sql = f'select * from freeboard where idx = {idx}'
    
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchone()
    print(res)
    db.close()
    return res


def select(page):
    db = pymysql.connect(
        host=host,port=port,
        user=user,password=password,
        db=dbname,charset=charset
    )
    
    startrow = (page-1)*3
    # 1페이지면 startrow가 0
    # 2페이지면 startrow가 3
    # 3페이지면 startrow가 6
    
    sql = F'select * from freeboard order by idx desc limit {startrow},10'
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close()
    print(res)
    return res


def update(title,content,writer,idx):
    db = pymysql.connect(
        host=host,port=port,
        user=user,password=password,
        db=dbname,charset=charset
    )
    sql = f"""UPDATE freeboard
                SET title = '{title}',
                    content = '{content}',
                    writer = '{writer}'
                WHERE idx ={idx};"""
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
    print("update 수정해야함")

def insert(title,content,writer):
    db = pymysql.connect(
        host=host,port=port,
        user=user,password=password,
        db=dbname,charset=charset
    )
    sql = f"""INSERT INTO freeboard
            (title,content,writer,regdate)
            VALUES
            ('{title}','{content}','{writer}',NOW())"""
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
    print("insert해야함")

def delete(idx):
    db = pymysql.connect(
        host=host,port=port,
        user=user,password=password,
        db=dbname,charset=charset
    )
    sql = f"""DELETE
             FROM freeboard 
            WHERE idx= {idx}"""
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
    print("delete해야함",idx)