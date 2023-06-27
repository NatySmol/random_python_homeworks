import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

doc = pd.read_csv('PKLM.csv')
doc.columns = ['rok','měsíc','den','průměrná teplota','maximální teplota','minimální teplota','srážky','Flag']

def graf1():
    graf1_a = doc.groupby('rok')[['průměrná teplota']].mean()
    graf1_b = doc.groupby("rok")[["maximální teplota"]].max()
    graf1_c = doc.groupby("rok")[["minimální teplota"]].min()

    fig, axes = plt.subplots(nrows=3, ncols=1)
    graf1_a.plot(title="Roční průměrné, minimální a maximální teploty", linestyle="solid", linewidth=0.5, color="navy", ax=axes[0])
    graf1_b.plot(linestyle="solid", linewidth=0.5, color="red", ax=axes[1])
    graf1_c.plot(linestyle="solid", linewidth=0.5, color="yellow", ax=axes[2])

    plt.xlabel("Roky")
    plt.ylabel("°C")
    plt.legend()
    plt.show()
    plt.savefig("graf1.pdf")

def graf2():
    graf2 = doc.groupby('měsíc')[['průměrná teplota','maximální teplota', 'minimální teplota']].mean()

    graf2.plot(title="Měsíční průměrné, minimální a maximální teploty", linewidth= 2.0, linestyle='--', color=['tab:pink', 'lightcoral', 'cyan'])
    ax = plt.gca()
    ax.set_facecolor("antiquewhite")
    plt.ylabel("°C")
    plt.legend()
    plt.show()
    plt.savefig("graf2.pdf")

def graf3():
    maxim = pd.DataFrame(doc.groupby(["rok", "měsíc"]).max())
    graf3 = pd.DataFrame(maxim.groupby("měsíc")[["srážky"]].mean())
    minim = pd.DataFrame(doc.groupby(["rok", "měsíc"]).min())
    x = pd.DataFrame(minim.groupby("měsíc")[["srážky"]].mean())
    graf3["Průměrné minimální srážky"] = x["srážky"]
    gr1 = pd.DataFrame(doc.groupby("měsíc")[['srážky']].mean())
    graf3["Průměrné srážky"] = gr1['srážky']
    g3 = graf3.rename(columns={"srážky": "Průměr maximálních srážek"})

    g3.plot()
    plt.title("Měsíční průměrné, minimální a maximální srážky")
    ax = plt.gca()
    ax.set_facecolor("mintcream")
    plt.ylabel("Srážky v mm")
    plt.legend(labels=['Maximální srážky',  'Minimální srážky','Průměrné srážky'])
    plt.show()
    plt.savefig("graf3.pdf")


def graf4():
    doc2=doc.loc[(doc['měsíc']==3) & (doc['den']==21), :].set_index('rok')
    graf4_1 = doc2.groupby('měsíc')[['průměrná teplota']]
    graf4_2 = doc2.groupby('měsíc')[['maximální teplota']]
    graf4_3 = doc2.groupby('měsíc')[['minimální teplota']]

    fig, axes = plt.subplots(nrows=3, ncols=1)

    graf4_1.plot(title = "Teploty 21. března každého roku", linestyle="solid", linewidth=0.5, color="navy", ax=axes[0])
    graf4_2.plot(linestyle="solid", linewidth=0.5, color="aquamarine", ax=axes[1])
    graf4_3.plot(linestyle="solid", linewidth=0.5, color="lime", ax=axes[2])

    plt.ylabel("°C")
    plt.legend()
    plt.show()
    plt.savefig("graf4.pdf")

graf1()
graf2()
graf3()
graf4()


