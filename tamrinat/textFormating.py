# marhaleye aval
# moshakhas ajnas va gheymatha
name1, price1 = "book", 20000
name2, price2 = "computer", 100000
name3, price3 = "pen", 1000
name4, price4 = "monitor", 50000
# marhale dovom
# addres dehi
store_name = "canbo"
store_addres = "Tehran"
store_city = "tehran"
# marhaleye sevom
message = "thanks for shopping with us today!"
# mathaleye chaharom
# jaygozari
# addres
print("*"*50)
print("\t\t{}".format(store_name.title()))
print("\t\t{}".format(store_addres.title()))
print("\t\t{}".format(store_city.title()))
# gheymat
print("="*50)
print("\t name,\t\t price")
print("\t{}\t\t${}".format(name1.title(), price1))
print("\t{}\t${}".format(name2.title(), price2))
print("\t{}\t\t${}".format(name3.title(), price3))
print("\t{}\t\t${}".format(name4.title(), price4))
# tashakor
# jame kol
print("*"*50)
print("\t\t\t Total")
Total = (price1+price2+price3+price4)
print("\t\t\t${}".format(Total))
print("="*50)
print("\n\t{}".format(message))
