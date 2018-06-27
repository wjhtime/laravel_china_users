import pymysql
import time


headers = {
    'Host': 'www.laravel-china.org',
    'Referer': 'www.laravel-china.org',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}

cookies = {
    'laravel_session': 'session_id'
}

def save_mysql(row):
    db = pymysql.connect('localhost', 'root', 'root', 'python')
    cursor = db.cursor()
    sql = "insert into laravel_china_users(uid, `name`, label, followers, discuss, article) values('%s','%s','%s','%s', '%s', '%s')"
    cursor.execute(sql % (row['uid'], row['name'], row['label'], row['followers'], row['discuss'], row['article']))
    db.commit()
    db.close()


def sleep(num):
    if num % 5:
        time.sleep(1)