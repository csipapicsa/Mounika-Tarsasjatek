import pandas as pd
import importlib as i
import numpy as np

# scaler
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def getLotto(link, mode="hatos"):
    """
    Open a lotto from the net and send it back as pandas file
    """
    df = pd.read_excel(link, index_col=0)
    if mode == "hatos":
        df.drop(columns=['Hét', 'Húzásdátum', '6 találat (db)', '6 találat (Ft)',
       '5+1 találat (db)', '5+1 találat (Ft)', '5 találat (db)',
       '5 találat (Ft)', '4 találat (db)', '4 találat (Ft)', '3 találat (db)',
       '3 találat (Ft)', "Unnamed: 19"], inplace=True)
        df.rename(columns={"Számok": "1", "Unnamed: 14": "2", "Unnamed: 15": "3", 'Unnamed: 16':"4", "Unnamed: 17":"5", "Unnamed: 18": "6"}, inplace=True)
    elif mode == "otos":
        df.drop(columns=['Hét', 'Húzásdátum', '5 találat (db)', '5 találat (Ft)',
       '4 találat (db)', '4 találat (Ft)', '3 találat (db)', '3 találat (Ft)',
       '2 találat (db)', '2 találat (Ft)'], inplace=True)
        df.rename(columns={"Számok": "1", "Unnamed: 12": "2", "Unnamed: 13": "3", 'Unnamed: 14':"4", "Unnamed: 15":"5"}, inplace=True)
    return df
    
def plotTrainHistory(history):
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()
    return None

def minMaxValuePrint(array, columns=6):
    chance = []
    for i in range(0,columns):
        print(f" minimum value {min(array[:, i])}, maximum value {max(array[:, i])} column {i+1}")
        c = max(array[:, i])-min(array[:, i])+1
        chance.append(c)
    chance.sort()
    return chance
if __name__ == "__main__":
    import importlib as i