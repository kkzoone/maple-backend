import sys, mariadb

#mariaDB 접속
try:
    conn = mariadb.connect(
        user='root',
        password='1234',
        host='localhost',
        port=3306,
        db='myrecipe'
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB PlatForm: {e}")
    sys.exit(1)
    
def test():
    cur = conn.cursor()
    
    #데이터 삽입
    #tree_id 1:케이크, 2:쿠키, 3:휘낭시에
    sql = '''INSERT INTO recipes (title, image, ingrediant, body, category_id)
        VALUES ("테스트1초코칩버터쿠키", "dust.png", '{"재료":"재료1"}', '{"준비":"준비"}', 
        (select id from categories where title = "초코칩" and parent_id = (select id from categories where title = "버터" and tree_id = 2) and tree_id = 2));'''
    cur.execute(sql)
    conn.commit()

if __name__ == '__main__':
    test()

#접속 종료
conn.close()