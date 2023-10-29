cc_year = [2000, 2001, 2002, 2003, 2004, 2005]
cc_month = [1, 2, 3, 4, 5]
cc_date = [1, 2, 3, 4, 5]


def do_something():
    pass


def cut(test_para_list, cut_para, cutted):
    if cutted:
        return test_para_list[test_para_list.index(cut_para):]
    else:
        return test_para_list


cutted = True
cut_dict = {'year': 2003, 'month': 2, 'date': 3}
test_dict = {}
for y in cut(cc_year, cut_dict.get('year'), cutted):
    cutted = y == cut_dict.get('year')
    for m in cut(cc_month, cut_dict.get('month'), cutted):
        cutted = cutted and m == cut_dict.get('month')
        for d in cut(cc_date, cut_dict.get('date'), cutted):
            print(y, m, d)
