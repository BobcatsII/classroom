#!/usr/bin/python
# -*- coding: utf-8 -*-

from operator import itemgetter

with open("report.txt","r") as f:
    list_total = f.readlines()
    rows = len(list_total)
    element = list_total[0].split(' ')
    lst = len(element)
    avg = []
    for index in xrange(1, lst):
        tmp = sum([int(item.split()[index]) for item in list_total]) / rows
        avg.append(tmp)
    avg.append(sum(avg))
    avg.append(avg[-1] / (lst - 1))
    avg.insert(0, '平均')
    a_score_list = []
    for one_score in list_total:
        score_list = one_score.split()
        score_list.append(sum(int(i) for i in score_list[1:]))
        t_score_list = score_list
        t_score_list.append(int(t_score_list[-1]) / (len(t_score_list)-2))
        a_score_list.append(t_score_list)
    sort_list = sorted(a_score_list, key=itemgetter(10),  reverse=True)
    sort_list.insert(0, avg)
    num = 0
    for rank in sort_list:
        rank.insert(0, num)
        num += 1
        for nopass in rank[2:-2]:
            if int(nopass) < 60:
                rank[rank.index(nopass)] = '不及格'
    sort_list.insert(0, ['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分'])


with open("new_file.txt", 'w') as g:
    for line in sort_list:
       row = len(line)
       for x in xrange(0, row):
           line[x] = str(line[x])
       new_file = ' '.join(line) + '\n'
       g.writelines(new_file)
