# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

# %%
def csv_to_df(input_string):
    return pd.read_csv(input_string)


# %%
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# %%
def capitalize_columns(input_df):
    new_df=input_df.copy()
    # new_df.rename(str.upper,axis=1)
    mylist=[]
    for name in new_df.columns:
        if not 'e' in name:
            mylist.append(name.upper())
        else: mylist.append(name)
    new_df.columns = mylist
    return new_df




# %%
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

# %%
def math_passed_count(input_df):
    new_df=input_df.copy()
    math = new_df['math score']
    return math[math > 50].count()


# %%
'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

# %%
def did_pre_course(input_df):
    new_df=input_df.copy()
    output = []
    for index,row in new_df.iterrows():
        if row['test preparation course'] == 'completed':
            output.append(row)
    return pd.DataFrame(output)


# %%
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

# %%
def average_scores(input_df):
    new_df = input_df.copy()
    return new_df.groupby('parental level of education').mean()

    

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# %%
import random


def add_age(input_df):
    new_df = input_df.copy()
    age = []
    random.seed(42)
    for i in range(len(new_df)):
        age.append(random.randint(18,66))
    new_df['age']=age
    return new_df


# %%
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# %%
def female_top_score(input_df):
    new_df = input_df.copy()
    gal = new_df.loc[new_df['gender']=='female'].max()
    return (gal['math score'],gal['reading score'],gal['writing score'])


# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

# %%
def add_grade(input_df):
    new_df = input_df.copy()
    grades = []
    for i in new_df.sum(axis=1):
        x = i/300
        if x >= 0.9:
            grades.append('A')
        elif x >= 0.8:
            grades.append('B')
        elif x >= 0.7:
            grades.append('C')
        elif x>= 0.6:
            grades.append('D')
        else:
            grades.append('F')
    new_df['grade']=grades
    return new_df


# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# %%
def math_bar_plot(input_df):
    new_df = input_df.copy()
    fig, ax = plt.subplots()
    plt.bar(new_df['gender'],new_df['math score'].mean())
    plt.xlabel('Gender')
    plt.ylabel('Math Score')
    plt.title('Average Math Score by Gender')
    return fig


# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# %%
def writing_hist(input_df):
    new_df = input_df.copy()
    fig, ax = plt.subplots()
    plt.title('Distribution of Writing Scores')
    plt.xlabel('Writing Score')
    plt.ylabel('Number of Studnets')
    plt.hist(new_df['writing score'])
    return fig


# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

# %%
def enthnicity_pie_chart(input_df):
    new_df= input_df.copy()
    fig, ax = plt.subplots()
    plt.pie(new_df.groupby('race/ethnicity').size()/len(new_df),labels=new_df['race/ethnicity'].unique(),autopct='%1.1f%%')
    plt.title('Proportion of Students by Race/Ethnicity')
    return fig



