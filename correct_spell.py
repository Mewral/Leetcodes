import flashtext
from flashtext import KeywordProcessor
import time

def retAll_1(rem, lst):
    idx = 0
    while idx < len(lst) :
        everyword = lst[idx]
        ans = kp.extract_keywords(everyword)
        if len(ans) > 0:
            idx += 1
        else:
            if idx == len(lst) - 1:
                break
            qwe = everyword
            start = idx
            end = idx
            for t in range(idx + 1, len(lst)-1):
                qwe += lst[t]
                zxc = kp.extract_keywords(qwe)
                if len(zxc) > 0:
                    end = t
                    rem.append(str(start)+"-"+str(end))
                    idx = t + 1
                    break
                if t == len(lst) - 2:
                    qwe += lst[-1]
                    asd = kp.extract_keywords(qwe)
                    if len(asd) > 0:
                        end = t + 1
                        rem.append(str(start) + "-" + str(end))
                        idx = len(lst)
                    else:
                        idx = end + 1

# 全匹配再筛选
# def retall_2():



kp = KeywordProcessor()
kp.add_keyword_from_file("./data/english_dict.txt", encoding="utf-8")

# line = "Iamabiglittleasheman"
# line = "guanzhoumintianindustrialareashatiantown"
# line = "copiesintotaltoourwarehousewhendeliveringCFScargo"
# line = "transactionsallgoodsaresubjectstoredtotheinCompany'soutgodownStandardmustbeTradinginsuredConditionsagainst"
# line = "unlessinitialledbytheCompanfromanyliabilitywhatsoeverarisingoutofunforeseencircumstances"
line = "remarks:pleasebring3(three)copiesintotaltoourwarehousewhendeliveringcfscargo."
lst = []

qwe = line.split(" ")
start = end = 0

# print(line[0:2])
# print(len(kp.extract_keywords("e")))

dicasasd = {}

with open("./data/english_word_dict_now.txt", "r", encoding="utf-8") as reader:
    for il in reader.readlines():
        if il.strip():
            if len(il.strip()) > 2:
                dicasasd[il.strip()] = 1

for i in range(len(line)):
    for j in range(i, len(line) + 1):
        start = i
        asd = line[i:j]
        if asd in dicasasd.keys():
            lst.append(str(i) + "-" + str(j -1))

def cangoto(thisone,lstleft):
    zxcasd = []
    temp = []
    # temp.append(thisone)
    flag = False
    temp_traing = thisone
    flaggg = True
    for q,t in enumerate(lstleft):
        if int(temp_traing.split("-")[1]) + 1 == int(t.split("-")[0]):
            pp = temp_traing.split("-")[0] + "-" + t.split("-")[1]
            if flaggg:
                temp.append(thisone)
            if pp not in lstleft:
                temp.append(t)
                temp_traing = pp
                flag = True
            else:
                if flaggg:
                    temp.append(t)
                temp_traing = pp
                # for canbedelete in temp:
                #     if canbedelete in lstleft:
                #         lstleft.remove(canbedelete)
                return temp
            flaggg = False

        if int(t.split("-")[0]) == int(lstleft[q-1].split("-")[0]):
            if flag:
                pp = temp_traing.split("-")[0] + "-" + t.split("-")[1]
                flaggg = False
                if pp not in lstleft:
                    if q == 0:
                        temp.append(thisone)
                    temp.append(t)
                    temp_traing = pp
                    flag = True
                else:
                    temp.append(t)
                    temp_traing = pp
                    # for canbedelete in temp:
                    #     if canbedelete in lstleft:
                    #         lstleft.remove(canbedelete)
                    return temp

def cantreach(thisone,lstleft):
    ersad = thisone
    maxmum = int(thisone.split("-")[1])
    lstasd = []
    lst_2 = []
    lst_2.append(int(ersad.split("-")[1]) + 1)
    for q, t in enumerate(lstleft):
        # if t.split("-")[0] == ersad.split("-")[0] and t.split("-")[1] > ersad.split("-")[1]:
        #     if int(maxmum) < int(t.split("-")[1]):
        #         maxmum = t.split("-")[1]

        if int(t.split("-")[0]) in lst_2:
            pp = ersad.split("-")[0] + "-" + t.split("-")[1]
            lstasd.append(pp.split("-")[1])
            lst_2.append(int(pp.split("-")[1]) + 1)
    if lstasd :
        maxmum = max(int(lstasd[-1]),maxmum)
    return maxmum

def isunique(thisone,lst):
    begin = thisone.split("-")[0]
    end = thisone.split("-")[1]
    indexofthisone = lst.index(thisone)
    leftlst = lst[:indexofthisone]
    leftmax = []
    rightmin = []
    rightlst = lst[indexofthisone+1:]
    leftmaxmax = -1
    rightminnnn = 10000
    for leftitem in leftlst:
        leftmax.append(int(leftitem.split("-")[1]))
    for rightitem in rightlst:
        rightmin.append(int(rightitem.split("-")[0]))
    if leftmax:
        leftmaxmax = max(leftmax)
    if rightmin:
        rightminnnn = min(rightmin)
    if int(begin) > leftmaxmax and int(end) < rightminnnn:
        return True
    return False

askd = []
print(lst)
#选择1

for idx,iasd in enumerate(lst):
    pppasd = cangoto(iasd, lst[idx:])
    lst_repeat = []
    if pppasd:
        for zmxczmxc in pppasd:
            if zmxczmxc not in askd:
                askd.append(zmxczmxc)
    lst_repeat.append(iasd)
    for nexta in lst[idx:]:
        if iasd.split("-")[0] == nexta.split("-")[0]:
            if nexta not in lst_repeat:
                lst_repeat.append(nexta)
    maxd = 0
    bereplaced = ""
    for repeat in lst_repeat:
        dddd = lst.index(repeat)
        maxthis = cantreach(repeat, lst[dddd:])
        if maxthis >= maxd:
            bereplaced = repeat
    if bereplaced in lst_repeat:
        lst_repeat.remove(bereplaced)
    for shouldremove in lst_repeat:
        lst.remove(shouldremove)

musthave = []
for zxcqwe in lst:
    if isunique(zxcqwe, lst):
        musthave.append(zxcqwe)
for mmm in musthave:
    lst.remove(mmm)

print("mushave___" + str(musthave))
for mm in askd:
    if mm in lst:
        lst.remove(mm)
# exit(1)

def isIncompatible(x, lst_u):
    lst_incompatible = []
    if lst_u:
        for ir in lst_u:
            start = ir.split("-")[0]
            end = ir.split("-")[1]
            if int(start) >= int(x.split("-")[0]):
                if min(int(end), int(x.split("-")[1])) - max(int(x.split("-")[0]), int(start)) >= 0:
                    continue
                else:
                    lst_incompatible.append(ir)
    return lst_incompatible

def anyleft(lstt, firstpick, one_selection, total_selection):
    lst_incompatible = isIncompatible(firstpick, lstt)
    if len(lst_incompatible) > 0:
        for saqwe in lst_incompatible:
            nextpick = saqwe
            one_selection.append(nextpick)
            lst_incompatible.remove(nextpick)
            anyleft(lst_incompatible, nextpick, one_selection, total_selection)
    else:
        total_selection.append(one_selection)
        return total_selection

    return total_selection


def chooseBest(lst):
    all_selection = []
    dic = {}
    for isa in lst:
        one_selection =[]
        total_selection = []
        lst_copy = []
        lst_copy += lst
        one_selection.append(isa)
        lst_copy.remove(isa)
        re_selection = anyleft(lst_copy, isa, one_selection, total_selection)
        re_selection.sort()
        if re_selection not in all_selection:
            all_selection.append(re_selection)
        lst_num = []
        lst_notinnum = []
        for aas in re_selection:
            for iwq in range(int(aas.split("-")[0]), int(aas.split("-")[1]) + 1):
                lst_num.append(iwq)
        for ist in range(len(line) + 1):
            if ist not in lst_num:
                lst_notinnum.append(ist)
        if len(lst_notinnum) not in dic.keys():
            dic[len(lst_notinnum)] = []
        dic[len(lst_notinnum)].append(re_selection)
    awqwe = sorted(dic.items(), key=lambda x:x[0])
    lst_asd = awqwe[0][1]
    final_choose = []
    if len(lst_asd) > 1:
        minmum = 100
        for cc in lst_asd:
            lst_finalnum = []
            lst_num2 = []
            for sst in cc:
                for zxc in range(int(sst.split("-")[0]), int(sst.split("-")[1]) + 1):
                    lst_num2.append(zxc)
                for ist in range(len(lst) + 1):
                    if ist not in lst_num2:
                        lst_finalnum.append(ist)
                        if ist < minmum:
                            final_choose = cc
                            minmum = ist
    else:
        final_choose = lst_asd[0]

    print(final_choose)

def chooseevery(lst, choose, all_selection):
    if len(lst) > 0:
        for ix,sd in enumerate(lst):
            choose.append(sd)
            lst_incompatible = isIncompatible(sd, lst[ix+1:])
            zxc = chooseevery(lst_incompatible, choose,all_selection)
            if zxc == 0:
                choose.remove(sd)
        return 0
    else:
        choose_copy = []
        choose_copy += choose
        result = list(set(choose_copy))
        result.sort(key=choose_copy.index)
        if result not in all_selection:
            all_selection.append(result)
        return 0


def chooseBest2(lst):
    all_selection = []
    lst_copy = []
    lst_copy += lst
    choose = []
    chooseevery(lst_copy, choose, all_selection)
    # print(lst)
    # print(len(all_selection))

    final_choose = []
    dics ={}

    for aas in all_selection:
        # print(aas)
        lst_num = []
        lst_notinnum = []
        count = 0
        for qqt in aas:
            for iwq in range(int(qqt.split("-")[0]), int(qqt.split("-")[1]) + 1):
                lst_num.append(iwq)
        for ist in range(len(line)):
            if ist not in lst_num:
                lst_notinnum.append(ist)
                count += 1
        # if "0-6" in aas and "7-16" in aas and "17-20" in aas:
        #     print()
        # if count == 0:
        #     print(aas)
        # if not lst_notinnum:
        #     print()
        if len(lst_notinnum) not in dics.keys():
            dics[len(lst_notinnum)] = []
        dics[len(lst_notinnum)].append(aas)

    awqwe = sorted(dics.items(), key=lambda x: x[0])
    lst_asdd = awqwe[0][1]

    if len(lst_asdd) > 1:
        minmum = 100
        for cc in lst_asdd:
            lst_finalnum = []
            lst_num2 = []
            for sst in cc:
                for zxc in range(int(sst.split("-")[0]), int(sst.split("-")[1]) + 1):
                    lst_num2.append(zxc)
                for ist in range(len(lst) + 1):
                    if ist not in lst_num2:
                        lst_finalnum.append(ist)
                        if ist < minmum:
                            final_choose = cc
                            minmum = ist
    else:
        final_choose = lst_asdd[0]

    return final_choose


# line = "dongguancity,guangdong,523991,china"
# line = "guanzhou,mintianindustrialarea,shatiantown"
print("lastlst____" + str(lst))
current_time = time.time()
finalchose = chooseBest2(lst)
finalchose += musthave
print(finalchose)
after_time = time.time()

print("cost time " + str(after_time - current_time))