
# coding: utf-8

# ##### 1. U(0,1)에서 난수를 1000개 발생하여 x축에는 표본수 n, y축에는 누적평균을 선그래프로 그리시오. 누적평균값은 n이 커짐에 따라 어떤 값을 수렴하는가?

# In[1]:


import random, math
from matplotlib import pyplot as plt

def mean(x):
    return sum(x) / len(x)


# In[2]:


data = [random.random() for _ in range(1000)]
xs = range(1001)
n_mean = [mean(data[0:(i+1)]) for i in xs]
plt.plot(xs, n_mean,'-')
plt.show()
n_mean[-1]


# 0.5 에 근사하게 수렴함을 알 수 있다.

# ##### 2. random 모듈을 이용하여 숫자 맞추기 게임을 구현하시오. 컴퓨터가 랜덤하게 1과 100사이의 정수를 고르고, 사용자가 1과 100사이의 추측값을 주면 정답과 비교하여 적절한 메시지(가령 크다, 작다, 잘했어요 등)를 주시오.

# In[3]:


from random import randint
sel_num = str(randint(1,100))
sel_num


# In[4]:


while True:
    guess = input('숫자를 입력하시오.')
    if guess > sel_num:
        print('크다')
    elif guess < sel_num:
        print('작다')
    else:
        print('잘했어요')
        break


# ##### 3. Medals.csv, Athelete_Country_Map.csv, Athelete_Sports_MAP.csv 파일을 이용하여 대한민국의 연도별로 메달을 집계해 보시오. 또한 대한민국의 선수별로 총메달 갯수를 구하고 금메달, 은메달, 동메달 갯수 순으로 정렬하시오. 

# In[5]:


import pandas as pd

medal = pd.read_csv('C:/Users/kyucheol/Desktop/Python_study/dataset/Medals.csv')
Country = pd.read_csv('C:/Users/kyucheol/Desktop/Python_study/dataset/Athelete_Country_Map.csv')
Sports = pd.read_csv('C:/Users/kyucheol/Desktop/Python_study/dataset/Athelete_Sports_Map.csv')


# In[6]:


Country_dp = Country.drop_duplicates(subset='Athlete')
Sports_dp = Sports.drop_duplicates(subset='Athlete')
merged_dp = pd.merge(left=medal, right=Country_dp, left_on='Athlete', right_on='Athlete')


# In[7]:


merged_final = pd.merge(left=merged_dp, right=Sports_dp, left_on='Athlete', right_on='Athlete')
merged_final.head()


# In[8]:


korea_data = merged_final[merged_final['Country'] =='South Korea']
korea_data.head()


#     (1) 대한민국 연도별 메달 갯수 집계

# In[9]:


k_year_medal = korea_data[['Year', 'Gold Medals', 'Silver Medals', 'Bronze Medals']]
grouped_year = k_year_medal.groupby('Year')
grouped_year.sum()


#     (2). 대한민국 총 선수별 메달갯수 및, 금메달 은메달 동메달 순 정렬

# In[10]:


k_athlete_medal = korea_data[['Athlete', 'Gold Medals', 'Silver Medals', 'Bronze Medals']]
grouped_athlete = k_athlete_medal.groupby('Athlete')
korean_medal = grouped_athlete.sum()


# In[11]:


korean_medal['Total Medals'] = korean_medal['Gold Medals'] + korean_medal['Silver Medals'] + korean_medal['Bronze Medals']
korean_medal.sort_values(by =['Gold Medals','Silver Medals', 'Bronze Medals'], ascending= False)

