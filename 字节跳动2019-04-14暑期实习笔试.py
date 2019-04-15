# encoding: utf-8 
"""
@file : 字节跳动2019-04-14暑期实习笔试.py
@author rj
@ide:pycharm
@time : 2019/4/14 10:12
"""
# 铲屎官观察猫的动态，输出猫的特征（说白了就是找到字串中连续重复字符的次数）
import sys


def getMaxlen(s_input, startIndex=0, curMaxlen=1, maxlen=1):
	if startIndex == len(s) - 1:
		return max(curMaxlen, maxlen)
	if list(s)[startIndex] == list(s)[startIndex + 1]:
		return getMaxlen(s, startIndex + 1, curMaxlen + 1, maxlen)
	else:
		return getMaxlen(s, startIndex + 1, 1, max(curMaxlen, maxlen))


while True:
	try:
		n = int(sys.stdin.readline().strip())
		result = []
		for i in range(n):
			m = int(sys.stdin.readline().strip())
			arr = []
			out = []
			for i in range(m):
				line = sys.stdin.readline().strip()
				values = list(map(int, line.split()))
				arr.append(values)
			for i in arr:
				s = "".join(map(str, i))
				out.append(getMaxlen(s, 0, 1, 1))
			result.append(max(out))

		for i in result:
			print(i)

	except:
		break

# 过河问题，每次三个人，时间由最长的人定
while True:
	try:
		# 测试组的数量为n
		n = int(input())
		result = []
		for i in range(n):
			# 每组中过河的人数为m
			m = int(input())
			# 将过河的人的时间降序排列，选择末尾的人做船夫
			arr = sorted(list(map(int, input().split())), reverse=True)
			min_time = arr[-1]
			if m == 2 or m == 3:
				print(max(arr))
			else:
				arr.pop()
				# 除去船夫其他人组成过河团队c,船夫每次携带做多2人
				c = [arr[i:i + 2] for i in range(0, m - 1, 2)]
				c_time = 0

				for i in c:
					max_time = max(i)
					c_time += max_time

			# 船夫返回的次数为len(c)-1
			out = c_time + (len(c) - 1) * min_time
			result.append(out)

		for i in result:
			print(i)
	except:
		break
