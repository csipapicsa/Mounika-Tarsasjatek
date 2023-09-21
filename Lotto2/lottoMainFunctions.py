import pandas as pd

import matplotlib.pyplot as plt

def getLotto(link, type):
    if type == "hatos":
        df = pd.read_excel(link, index_col=0)
        df.drop(columns=['Hét', 'Húzásdátum', '6 találat (db)', '6 találat (Ft)',
        '5+1 találat (db)', '5+1 találat (Ft)', '5 találat (db)',
        '5 találat (Ft)', '4 találat (db)', '4 találat (Ft)', '3 találat (db)',
        '3 találat (Ft)', "Unnamed: 19"], inplace=True)
        df.rename(columns={"Számok": "1", "Unnamed: 14": "2", "Unnamed: 15": "3", 'Unnamed: 16':"4", "Unnamed: 17":"5", "Unnamed: 18": "6"}, inplace=True)
        column_values = df[["1", "2", "3", "4", "5", "6"]].values
        return df, column_values
        
    elif type == "ötös":
        df = pd.read_excel(link, index_col=0)
        df.drop(columns=["Húzásdátum", 'Hét', '5 találat (db)',
        '5 találat (Ft)', '4 találat (db)', '4 találat (Ft)', '3 találat (db)',
        '3 találat (Ft)', '2 találat (Ft)', '2 találat (db)'], inplace=True)
        df.rename(columns={"Számok": "1", "Unnamed: 12": "2", "Unnamed: 13": "3", 'Unnamed: 14':"4", "Unnamed: 15":"5"}, inplace=True)
        column_values = df[["1", "2", "3", "4", "5"]].values
        return df, column_values
    
def getLottoDB(type = ""):
    if type == "ötös":
        return "https://bet.szerencsejatek.hu/cmsfiles/otos.xls"
        
    elif type == "hatos":
        return "https://bet.szerencsejatek.hu/cmsfiles/hatos.xls"
    
def plotTrainingHistory(history):
    # Create a figure and axis for the loss plot
    training_loss = history.history['loss']
    training_accuracy = history.history['accuracy']
    
    fig, ax1 = plt.subplots()

    # Plot the training loss on the left y-axis
    ax1.plot(range(1, len(training_loss) + 1), training_loss, label='Training Loss', color='b')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.legend(loc='upper left')

    # Create a second axis for the accuracy plot, sharing the same x-axis
    ax2 = ax1.twinx()

    # Plot the training accuracy on the right y-axis
    ax2.plot(range(1, len(training_accuracy) + 1), training_accuracy, label='Training Accuracy', color='r')
    ax2.set_ylabel('Accuracy', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    ax2.legend(loc='upper right')

    plt.title('Training Loss and Accuracy')
    return plt


#tip = "ötös"
#print(getLotto(getLottoDB(tip), type=tip).head())


#print(getLotto(getLottoDB(tip), type=tip))