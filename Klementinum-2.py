import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('PKLM.csv')
df.columns = ['Rok','Mesic','Den','Teplota','MaxTeplota','MinTeplota','Srazky','Nic']

with plt.style.context('dark_background'):
    graf1 = df.groupby('Rok')[['Teplota', 'MaxTeplota', 'MinTeplota']].mean()
    graf1.plot(title="Graf1", linestyle='solid', linewidth=2.0, color=['yellow', 'magenta', 'lime'])
    plt.legend()
    plt.ylabel("Teplota")
    plt.show()
    #plt.savefig("Graf1.pdf")

#Měsíční průměr chápu tak, že udělám průměr ze všech hodnot v měsíci ve všech letech
graf = df.groupby('Mesic')[['Teplota', 'MaxTeplota', 'MinTeplota']].mean()
graf2 = graf.plot(title="Graf2", linewidth=4.0, linestyle='dotted', color=['green', 'blue', 'orange'])
plt.ylabel("Teplota")
plt.legend()
plt.show()
plt.savefig("Graf2.pdf")

graf3 = df.groupby('Mesic')['Srazky'].agg(['mean', 'max','min'])
graf3.plot(title="Graf3", linestyle='solid', linewidth=1.5, color=['magenta', 'darkorange', 'red'])
plt.ylabel("Srazky v mm")
plt.legend(labels=['Prumer', 'Max', 'Min'])
plt.show()
plt.savefig("Graf3.pdf")

df2=df.loc[(df['Mesic']==3) & (df['Den']==21), :].set_index('Rok')
graf4 = df2.groupby('Mesic')[['Teplota', 'MaxTeplota', 'MinTeplota']]
graf4.plot(title='Graf4', linewidth=1.0)
plt.ylabel("Teplota")
plt.xlabel("Rok")
plt.legend()
plt.show()
plt.savefig("Graf4.pdf")

