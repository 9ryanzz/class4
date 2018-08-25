# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 04:40:31 2018

@author: 黃琦翔
"""

#%%
import random
import os
score = []

#%%
def begin():
    print('----------------------------------------------------------------------')
    print('剪刀石頭布')
    print('----------------------------------------------------------------------')
    
#%%
def judge(a,b):
    if a == b:
        print('平')
        score.append('0')
    elif a == 99:
        print('勝')
        score.append('2')
    elif b == 99:
        print('敗')
        score.append('1')
    elif a == 1 and b == 2:
        print('敗')
        score.append('1')
    elif a == 2 and b == 3:
        print('敗')
        score.append('1')
    elif a == 3 and b == 1:
        print('敗')
        score.append('1')
    elif a == 2 and b == 1:
        print('勝')
        score.append('2')
    elif a == 3 and b == 2:
        print('勝')
        score.append('2')
    elif a == 1 and b == 3:
        print('勝')
        score.append('2')
        
#%%
def player1():
    global input_1
    while 1 :
        input_1 = int(input('玩家一輸入，剪刀:1，石頭:2，布:3:'))
        if input_1 == 1 or input_1 == 2 or input_1 == 3 or input_1 == 99:
            break
        else:
            print('給我認真點')
#%%
def player2():
    global input_2
    while 1 :
        input_2 = input('玩家二輸入，剪刀:1，石頭:2，布:3:')
        if input_2 == 1 or input_2 == 2 or input_2 == 3 or input_2 == 99:
            break
        else:
            print('給我認真點')
#%%
def com():
    global com_1
    com_1 = random.randint(1,3)  
          
#%%
while 1:
    begin()
    mood = input('輸入模式，1:單人，2:雙人，以外:離開')
    score = []
    if mood == 1:
        times = int(input('遊玩次數'))
        for i in range(times):
            player1()
            com()
            judge(input_1,com_1)
            os.system('pause')
            os.system('cls')
            begin()
        win = score.count('2')
        lose = score.count('1')
        if win > lose:
            print('你贏了')
        elif win < lose:
            print('你輸了')
        else:
            print('平手')
        os.system('cls')
    elif mood == 2:
        times = int(input('遊玩次數'))
        for i in range(times):
            player1()
            os.system('cls')
            begin()
            player2()
            os.system('cls')
            begin()
            judge(input_1,input_2)
            os.system('pause')
            os.system('cls')
            begin()
        win = score.count('2')
        lose = score.count('1')
        print('結束!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        if win > lose:
            print('玩家一贏了')
            os.system('pause')
            os.system('cls')
        elif win < lose:
            print('玩家二贏了')
            os.system('pause')
            os.system('cls')
        else:
            print('平手')
            os.system('pause')
            os.system('cls')
    else:
        break
    