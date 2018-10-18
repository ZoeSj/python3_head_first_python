"""
the example about movie
"""
movies = ["The holy Grail","The Life of Brain","Teh Meaning of Life"]

print(movies) #['The holy Grail', 'The Life of Brain', 'Teh Meaning of Life']
print(movies[1])#The Life of Brain
print(len(movies))#3

"""
append() 列表末尾增加一个数据项
pop()列表末尾删除一个数据
extend()列表末尾增加一个数据线集合
remove()删除指定的数据项
insert()在某个特定的位置前面增加一个数据项
"""

movies.append("The Space War")
print(movies) #['The holy Grail', 'The Life of Brain', 'Teh Meaning of Life', 'The Space War']

movies.pop()
print(movies)#['The holy Grail', 'The Life of Brain', 'Teh Meaning of Life', 'The Space War']

movies.extend(["The Space War","The world"])
print(movies)#['The holy Grail', 'The Life of Brain', 'Teh Meaning of Life', 'The Space War', 'The world']

movies.remove("The holy Grail")
print(movies)#['The Life of Brain', 'Teh Meaning of Life', 'The Space War', 'The world']

movies.insert(0,"The holy Grail")
print(movies)#['The holy Grail', 'The Life of Brain', 'Teh Meaning of Life', 'The Space War', 'The world']

"""
处理列表数据
迭代
递归
"""

fav_movies = ["The holy Grail","The Life of Brain"]
print(fav_movies[0])
print(fav_movies[1])

for each_item in fav_movies:
	print(each_item)
	pass

"""
列表中嵌套列表，如何处理？
"""
cir_movies = ["The holy Grail",1986,["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam"]],"The Life of Brain",1992,"Teh Meaning of Life",1976]

for each_item in cir_movies:
	print(each_item)#列表中还存在嵌套列表
	pass

"""
The holy Grail
1986
['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam']]
The Life of Brain
1992
Teh Meaning of Life
1976
"""

"""
在列表中查询列表
可以使用isinstance（BIF）
"""

for each_item in cir_movies:
	if isinstance(each_item,list):
		for iterm in each_item:
			print(iterm)
	else:
		print(each_item)
	pass
"""
The holy Grail
1986
Graham Chapman
['Michael Palin', 'John Cleese', 'Terry Gilliam']
The Life of Brain
1992
Teh Meaning of Life
1976
"""

"""
处理多层嵌套
"""
def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item)
		else:
			print(each_item)
	pass

print_lol(cir_movies)
"""
The holy Grail
1986
Graham Chapman
Michael Palin
John Cleese
Terry Gilliam
The Life of Brain
1992
Teh Meaning of Life
1976
"""











































