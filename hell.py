# arry = ["one", "two", 3]
# arry.append("four")  ## 在列表中末位增加
# arry.pop()  ##在列表中末位删除
# arry.extend(["five", "six"])  ##在末位增加集合
# arry.remove("five")  ##删除特定项
# arry.insert(3, "x")  ##操纵index插入
# for run_arry in arry:               ##for 标识 In 列表
#  ## print(arry[1])
#  print(run_arry)
# print("--------------")

# i = 1                               ## while
# while i < len(arry):
#     print(arry[i],"-",i)
#     i = i + 2
#     print("i=",i)
#     print(i)

nesting_list = ["data1", 'data2', ['ndata1', 'ndata2', ['nndata']]]  ##多层嵌套list
## print(nesting_list[2][2][0])
for run_nl in nesting_list:
## print(run_nl)
 if isinstance(run_nl, list):
    for ndata in  run_nl:
        print(ndata)
else:
    print(run_nl )
