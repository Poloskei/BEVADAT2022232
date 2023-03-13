# %%
# import numpy as np

# %%
#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)

# %%
# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait. Bemenetként egy array-t vár.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()

# %%
def column_swap(input_array:np.array)->np.array:
    temp=np.copy(input_array[:,0])
    input_array[:,0]=input_array[:,1]
    input_array[:,1]=temp
    return input_array

# print(column_swap(np.array([[1,2],[3,4]])))

# %%
# Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön

# %%
def compare_two_array(input1:np.array, input2:np.array)->np.array:
    return np.where(np.equal(input1,input2))

# print(compare_two_array([7, 8, 9], [9, 8, 7]))

# %%
# Készíts egy olyan függvényt, ami vissza adja string-ként a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!, 

# %%
def get_array_shape(input_array:np.array)->str:
    shape =np.shape(input_array)
    sor = shape[len(shape)-1] if len(shape) > 0 else 0
    oszlop = shape[len(shape)-2] if len(shape) > 1 else 1
    melyseg = shape[len(shape)-3] if len(shape) > 2 else 1
    return "sor: " +str(sor)+", oszlop: "+str(oszlop)+", melyseg: "+ str(melyseg)


# print(get_array_shape(np.array([[[1]],[[2]]])))

# %%
# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges pred-et egy numpy array-ből. 
# Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli. 
# Pl. ha 1 van a bemeneten és 4 classod van, akkor az adott sorban az array-ban a [1] helyen álljon egy 1-es, a többi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()

# %%
def encode_Y(input_array:np.array, num_class:int)->np.array:
    output_array = np.zeros((len(input_array),num_class))
    output_array[np.arange(len(input_array)),input_array] = 1
    return output_array

# print(encode_Y([1, 2, 0, 3], 4))

# %%
# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()

# %%
def decode_Y(input_array:np.array)->np.array:
    output_array = len(input_array[:,0])
    
    return output_array

# %%
# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! Bemenetként egy listát és egy array-t és adja vissza azt az elemet, aminek a legnagyobb a valószínüsége(értéke) a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. # Az ['alma', 'körte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()

# %%
def eval_classification(input_list:list, input_array:np.array):
    idx = np.argmax(input_array)
    return input_list[idx]

# print(eval_classification(['alma', 'korte', 'szilva'], np.array([0.2, 0.2, 0.6])))

# %%
# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# replace_odd_numbers()

# %%
def replace_odd_numbers(input_array:np.array)->np.array:
    input_array[input_array%2==1] = -1
    return input_array

# print(replace_odd_numbers(np.array([1, 2, 3, 4, 5, 6])))

# %%
# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()

# %%
def replace_by_value(input_array:np.array, split_value:int)->np.array:
    input_array[input_array<split_value] = -1
    input_array[input_array>=split_value]=1
    return input_array

# print(replace_by_value(np.array([1, 2, 5, 0]),2))

# %%
# Készíts egy olyan függvényt, ami egy array értékeit összeszorozza és az eredményt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza

# %%
def array_multi(input_array:np.array)->int:
    return np.prod(input_array)

# print(array_multi(np.array([1,2,3,4])))

# %%
# Készíts egy olyan függvényt, ami egy 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()

# %%
def array_multi_2d(input_array:np.array)->np.array:
    return np.prod(input_array,axis=1)

# print(array_multi_2d(np.array([[1,2],[3,4]])))

# %%
# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal. Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()


# %%
def add_border(input_array:np.array)->np.array:
    return np.pad(input_array,1)

# print(add_border(np.array([[1,2],[3,4]])))

# %%
# A KÖTVETKEZŐ FELADATOKHOZ NÉZZÉTEK MEG A NUMPY DATA TYPE-JÁT!

# %%
# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot és ezt adja vissza egy numpy array-ben. A fgv ként str vár paraméterként 'YYYY-MM' formában.
# Be: '2023-03', '2023-04'  # mind a kettő paraméter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()

# %%
def list_days(start:str,end:str)->np.array:
    return np.arange(np.datetime64(start,'D'),np.datetime64(end,'D'))

# print(list_days('2023-03','2023-04'))

# %%
# Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD. Térjen vissza egy 'numpy.datetime64' típussal.
# Be:
# Ki: 2017-03-24
# get_act_date()

# %%
def get_act_date()->np.datetime64:
    return np.datetime64('today')


# %%
# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta. Int-el térjen vissza
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()

# %%
def sec_from_1970()->int:
    dt = np.datetime64('today') - np.datetime64('1970-01-01T00:00:00')
    return dt.astype(np.int32)

# print(type(sec_from_1970()))
# print(sec_from_1970())


