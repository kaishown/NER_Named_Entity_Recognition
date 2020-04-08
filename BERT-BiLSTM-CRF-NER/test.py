# for test
from __future__ import division
import codecs
def read_txt(txt_path):
	with codecs.open(txt_path,'r',encoding='utf-8') as f:
		return f.readlines()
def save_txt(lines,txt_path):
	with codecs.open(txt_path,'w',encoding='utf-8') as f:
		f.writelines(lines)
		print("=======保存文件成功========目标文件为{}".format(txt_path))
def txt_to_lines(txt_path):
	txt = read_txt(txt_path)
	lines = [i+' O\n' for i in txt[0]]
	print(lines,txt)
	# save_path = flags.data_dir + 'test.txt'
	save_path = 'ttt.txt'
	save_txt(lines=lines,txt_path=save_path)

if __name__ == '__main__':
	txt_path = 't1.txt'
	# txt_to_lines(txt_path)
	print(3/4)
