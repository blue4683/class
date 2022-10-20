import os
os.chdir('C:/pytest/')

import pandas as pd
import numpy as np

data = pd.read_csv('감성대화말뭉치(최종데이터)_Validation.csv', encoding = 'cp949')
# 행 범위 지정
human = data.loc[0:149]

for i in range(len(human)):
    print(human.loc[i,'사람문장1'])
    temp = input()
    human.loc[i, '감정_대분류'] = temp

human_data = human[['감정_대분류', '사람문장1']]

human_data.to_csv('감정분류.csv',index = False, encoding='cp949')