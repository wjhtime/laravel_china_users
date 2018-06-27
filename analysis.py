import pandas as pd
from pyecharts import Bar

RAW_FILE = './data/users.csv'

def followers():
    df = pd.read_csv(RAW_FILE)
    data_list = list(df['followers'])
    labels = ['1-10', '11-50', '51-100', '101-500', '501-1000', '>1000']
    size = []

    size.append(len([x for x in data_list if x >0 and x <=10]))
    size.append(len([x for x in data_list if x >=11 and x <=50]))
    size.append(len([x for x in data_list if x >=51 and x <=100]))
    size.append(len([x for x in data_list if x >=101 and x <=500]))
    size.append(len([x for x in data_list if x >=501 and x <=1000]))
    size.append(len([x for x in data_list if x >=1001]))

    bar = Bar("followers", "人数")
    bar.add("followers", labels, size, mark_line=["average"], mark_point=["max", "min"])
    bar.render('./images/followers.html')

def discuss():
    df = pd.read_csv(RAW_FILE)
    data_list = list(df['discuss'])
    labels = ['1-10', '11-50', '51-100', '101-500', '501-1000', '>1000']
    size = []

    size.append(len([x for x in data_list if x > 0 and x <= 10]))
    size.append(len([x for x in data_list if x >= 11 and x <= 50]))
    size.append(len([x for x in data_list if x >= 51 and x <= 100]))
    size.append(len([x for x in data_list if x >= 101 and x <= 500]))
    size.append(len([x for x in data_list if x >= 501 and x <= 1000]))
    size.append(len([x for x in data_list if x >= 1001]))

    bar = Bar("discuss", "人数")
    bar.add("discuss", labels, size, mark_line=["average"], mark_point=["max", "min"])
    bar.render('./images/discuss.html')

def article():
    df = pd.read_csv(RAW_FILE)
    data_list = list(df['article'])
    labels = ['1-5', '6-10', '11-20', '21-30', '>30']
    size = []

    size.append(len([x for x in data_list if x > 0 and x <= 5]))
    size.append(len([x for x in data_list if x >= 6 and x <= 10]))
    size.append(len([x for x in data_list if x >= 11 and x <= 20]))
    size.append(len([x for x in data_list if x >= 21 and x <= 30]))
    size.append(len([x for x in data_list if x >= 31]))

    bar = Bar("article", "人数")
    bar.add("article", labels, size, mark_line=["average"], mark_point=["max", "min"])
    bar.render('./images/article.html')

def main():
    followers()
    discuss()
    article()
    pass

if __name__ == '__main__':
    main()