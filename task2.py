dic = {}

n = int(input("Number of books: "))

for i in range(n):
    print("Book Title - Days")
    # "book1 - 30"  => ["book1" , '30']
    # book1 - 30
    # book1 - 25
    # book2 - 90
    # book1 - 55
    pair = input().split(" - ")
    dic[pair[0]] = int(pair[1])


print("most borrowed book : " , max(dic , key= dic.get))
print("least borrowed book : " , min(dic , key= dic.get))
print(f"unique books: {set(dic.keys())}")
[" , "]
sortedDic = dict(sorted(dic.items() , key= lambda b : b[1] , reverse=True))

print(f"sortedbooks {sortedDic}")