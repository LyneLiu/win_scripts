# 学习一个关机/重启的脚本
# -*- coding:utf-8 -*-

import os,time

running = True

while running:
	command = input("关机(s)or重启(r)？（q退出）\n")
	if command == 'q' or command == 'quit':
		running = False
		print("退出程序")
		break
	elif command == 's':
		print("正在关机。。。")
		os.system('shutdown -s')
		break
	elif command == 'r':
		print("正在重启。。。")
		os.system('shutdown -r')
		break
	else:
		print("输入错误，please input again！")
		running = True


