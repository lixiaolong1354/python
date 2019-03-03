class str_t_num:
	def __init__(self,path,end_num,start_num=0,sli_num=1):
		"""字符串添加数字自增后缀迭代器"""
		if isinstance(path,str) and isinstance(end_num,int) and isinstance(start_num,int) and isinstance(sli_num,int):
			return None
		self.path	=	path
		self.sli 	=	sli_num
		self.max	=	end_num
		self.num	=	start_num-1
		return self
	def __iter__(self):
		return self
	def __next__(self):
		self.num +=self.sli
		if self.num < self.max:
			return self.path + str(self.num)
		else:
			raise StopIteration

import re
def str_mat(str_base,str_start,str_end,count=1):
	"""匹配字符串对 并返回位置列表。count为搜索次数，为负数时将无限次搜索，为0时返回空列表。"""
	if isinstance(str_start,str) and isinstance(str_end,str) and isinstance(count,int) and isinstance(str_base,str):
		min_num	=	0
		max_num	=	0
		tem 	=	[]
		while count != 0:"""循环提取count次"""
			count	-=	1
			tem_start	=	re.search(str_start,str_base[max_num:])"""搜索开始字符串"""
			if tem_start is None:
				return tem
			min_num		+=	tem_start.end()

			tem_end		=	re.search(str_end,str_base[min_num:])"""搜索结束字符串"""
			if tem_end	is	None:
				return tem
			max_num		+=	tem_end.start()

			if tem_start.end() and tem_end.start():"""保存搜索结果，无结果将返回"""
				tem.append((min_num,max_num))
				max_num	+=	tem_end.end()-tem_end.start()
			else:
				return tem

		return tem"""完成count次搜索"""
	else:
		return None"""参数列表不正确将返回None"""


def str_list_connect(chars,list2,max_num=200,connect_chars=""):
	"""函数将用connect_chars拼接str字符串中list列表中的子字符串,并截取为num长度的字符串。
	num为负数时将无限长度拼接"""
	if isinstance(chars,str) and isinstance(list2,list) and isinstance(max_num,int) and isinstance(connect_chars,str):
		print(list2)
		tem_cs	=	""
		for list_tem in list2:
			tem_cs	=	tem_cs + chars[list_tem[0]:list_tem[1]]	+	connect_chars
			if len(tem_cs) >= max_num:
				return	tem_cs[:max_num]
		return tem_cs
	else:
		return None
