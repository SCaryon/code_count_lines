import os,sys,time
def get_year(now):
    filemt= time.localtime(os.stat(now).st_mtime) # 获取文件创建时间
    ModifiedTime=time.strftime("%Y-%m-%d",filemt)
    y=ModifiedTime[:4]
    return y
def count(path,suffix,ignore,statistics,years):
    cnt=0
    for fn in os.listdir(path):
        now = path+fn # 文件路径
        # print(fn)
        if os.path.isdir(now):
            # print(now+'\\')
            if now+'\\' in ignore:
                # print('ignore=',now+'\\')
                continue
            tmp,years=count(now+'\\',suffix,ignore,statistics,years)
            cnt = cnt + tmp
        else:
            filename,type=os.path.splitext(now)
            if type in suffix:
                # print(filename,type)
                try:
                    num = len(open(now, 'r').readlines())# 当前文件的行数
                    y=get_year(now) # 获取文件创建时间(年)
                    # print(now,y)
                    years[y] = years[y]+num
                    statistics[type] = statistics.get(type,0) + num
                except UnicodeDecodeError:# 判断二进制文件
                    pass
                else:
                    cnt = cnt + num
    # if cnt != 0:
    #     print(path,statistics)
    return cnt,years
if __name__ == '__main__':
    ignore=['D:\\code\\python\\pygame\\pygame-samples-master\\',
            'D:\\code\\python\\Lo-runner-master\\',
            'D:\\code\\Django\\venv\\',
            'D:\\code\\eclipse-workspace\\',
            ]
    suffix=['.cpp','.c','.py','.java']
    years={'2016':0,'2017':0,'2018':0}
    src = 'D:\\code\\'
    statistics=dict()
    ans,years = count(src,suffix,ignore,statistics,years)
    print(src,'下总代码行数为：',ans)
    print('语言统计情况：')
    for key in statistics.keys():
        print(key,':',statistics[key])
    print('年份统计情况：')
    for key in years.keys():
        print(key,':',years[key])