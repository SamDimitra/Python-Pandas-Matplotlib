#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv('survey_results_public.csv',index_col='ResponseId')

df.shape

df

df.columns

df.PlatformHaveWorkedWith.unique()

df.Employment.unique()

df['Employment'].value_counts(normalize=True)

slice=[0.643088,0.141390,0.096504,0.035536,0.029536,0.024615]
labels=['Employed full-time ','Student, full-time ','Independent contractor, freelancer, or self-employed',
        'Not employed, but looking for work ','Employed part-time','Student, part-time ']

plt.pie(slice,labels=labels,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})


df.rename(columns={'ConvertedCompYearly':'Salary'},inplace=True)

df['Salary'].median()

country_group=df.groupby(['Country'])

country_group.get_group('Greece')

sal_gre=country_group['Salary'].median().loc['Greece']

sal_germ=country_group['Salary'].median().loc['Germany']

sal_aus=country_group['Salary'].median().loc['Austria']
sal_gre
sal_germ
sal_aus

sal_neth=country_group['Salary'].median().loc['Netherlands']
sal_neth

avg_sal=[25944.0,64859.0,54049.0,59676.0]
labels=['Greece','Germany','Austria','Netherlands']

plt.pie(avg_sal,labels=labels)



country_uses_python=country_group['LanguageHaveWorkedWith'].apply(lambda x:x.str.contains('Python').sum())


country_uses_python.head(10)


gre_py=country_uses_python.loc['Greece']


can_py=country_uses_python.loc['Canada']


ger_py=country_uses_python.loc['Germany']


austr_py=country_uses_python.loc['Australia']


use_python=[gre_py,can_py,ger_py,austr_py]

labels=['Greece','canada','Germany','Australia']
explode=[0.1,0,0,0]


plt.pie(use_python,labels=labels,explode=explode)






