# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 20:48:54 2023

@author: anish
"""
#importing Libraries
import pandas as pd
import matplotlib.pyplot as plt

#Defining Line function


def coal_prices():
    '''
        Line plot representing Coal prices of different countries 
        in the years 2001 to 2021.
    '''

    
    #Reading csv dataset
    cp = pd.read_csv("coal-prices.csv")
    print(cp)

    China = cp[cp['Entity'] == "China Qinhuangdao spot price (BP)"]
    Japan_steam_coil = cp[cp['Entity'] == "Japan coking coal import\
                        CIF price (BP)"]
    Japan_steam_spot = cp[cp['Entity'] == "Japan steam spot CIF price (BP)"]
    Northwest = cp[cp['Entity'] == "Northwest Europe marker price (BP)"]
    US = cp[cp['Entity'] == 
        "US Central Appalachian coal spot price index (BP)"]

    #plotting figuresize
    plt.figure(figsize = (10, 5))

    plt.plot(China["Year"], China["Coal - Prices"], label = "China")
    plt.plot(Japan_steam_coil["Year"],
             Japan_steam_coil["Coal - Prices"], label = "Japan_steam_coil")
    plt.plot(Japan_steam_spot["Year"],
             Japan_steam_spot["Coal - Prices"], label = "Japan_steam_spot")
    plt.plot(Northwest["Year"], Northwest["Coal - Prices"], \
             label = "Northwest")
    plt.plot(US["Year"], US["Coal - Prices"], label = "US")
    plt.xticks(China['Year'][::2])
    #plt.plot(df["Year"], df[""], label = "")

    #plotting labels and legeds
    #plotting fontsize
    plt.xlabel("Year", fontsize = 15)
    plt.ylabel("Coal Price (USD)", fontsize = 15)
    plt.legend()
    #plotting title
    plt.title('Coal Price 2001 - 2021', fontsize = 20)
    plt.grid()
    plt.show()
    


#Defining the Bar function


def India_health():
    '''
        Bar plot representing India state health data EDA
        of reporting Asthma in men aged from 15 to 49 years.
    '''

    
    #Reading the csv data set
    data = pd.read_csv("India_health.csv")
    print(data)
    plt.figure(figsize = (15, 5))
    plt.bar(data['State/UT'], 
    data['Proportion of men and women Reporting Asthma 15-49 years - Men'])

    #plotting the labels and legend
    plt.legend()
    #plotting fontsize
    plt.xlabel('State/UT', fontsize = 15)
    plt.xticks(rotation = 'vertical')
    plt.ylabel('Proportion of reporting Asthma 15-49 years-Men', \
               fontsize = 15)
    plt.title('India state health data EDA', fontsize = 20)
    plt.show()
    
    

#Defining the pie function


def Olympic_Medals():
    '''
        Pie chart representing the Tokyo 2020 Olympics Medals
        for the Preferred countries.
    '''
    
    
    #Reading the csv data set
    df = pd.read_csv("Tokyo Olympic Medals 2020.csv")
    print(df)
    df2 = df[:5].copy()
    #plotting the labels and legend
    plt.figure()
    plt.pie(df2['Total'], labels=df2['Country'], 
                autopct = '%.2f%%', shadow = 'True')
    #plt.legend(loc = 'lower left')
    plt.legend(loc = 'center left', bbox_to_anchor = (1, 0.5))
    plt.title('Tokyo Olympic Medals 2020', fontsize = 20)
    plt.show()

#function calling
coal_prices()
India_health()
Olympic_Medals()
    


