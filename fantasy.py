'''
Identify trends in NFL fantasy data over the past 20 years
Data scraped from pro-football-refernce.com
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# download football data using html scraping
def download(start_yr,end_yr,type):
    for yr in range(start_yr,end_yr):
        if os.path.exists('./data/'+str(yr)+str(type)+'.csv'):
            pass
        else:
            print('downloading...'+str(yr)+' data')
            df = pd.read_html('https://www.pro-football-reference.com/years/'+str(yr)+'/'+str(type)+'.htm')[0]

            #remove all intermediate headers in data set
            df = df[df['Player']!= "Player"]
            df['year'] = yr
            df.drop(['Rk'],axis=1)

            df.to_csv('./data/'+str(yr)+str(type)+'.csv')

    # merge all csv files into master file
    for yr in range(start_yr,end_yr):
        if yr == start_yr:
            main_df = pd.read_csv('./data/'+str(yr)+str(type)+'.csv')
        else:
            temp_df = pd.read_csv('./data/'+str(yr)+str(type)+'.csv')
            main_df = pd.concat([main_df,temp_df])

    # save master csv for databasing
    main_df.to_csv('./data/master_'+str(type)+'.csv')

# ---------- DATA MINING -------------------
# intialize data range
start_yr = 2000
end_yr = 2020

#download csv files and compile master file
download(start_yr,end_yr,'passing')
# download(start_yr,end_yr,'rushing')

# ----------- DATA EXPLORATION -----------------
# clean data by removing values which skew data set
passdf = pd.read_csv('data/master_passing.csv')

# -- remove values for pass attempts less than 50 to remove
passdf = passdf[passdf['Att'] > 50]

# -- remove values for games played less than 10
passdf = passdf[passdf['G'] >= 10]

# compute fantasy points based on ESPN standard scoring
passdf['ftyPts'] = ( passdf['Yds'] / 25 + passdf['TD'] * 4 + passdf['Int'] * -2 ) / passdf['G']

# --- plot data
sns.set_theme(style="darkgrid")
pal = sns.cubehelix_palette(10,rot=-0.25, light=0.7) #color palette

# Set up the matplotlib figure
g=sns.FacetGrid(passdf, col='year',col_wrap=5,height=1.75)
g.map(sns.histplot,'Y/G',bins=10)
for ax in g.axes.flat:
    ax.axvline(x=200,alpha=0.5,ls='--',c='r')

g.set_axis_labels('Avg. Yds/Game','Count')
plt.show()

# track Yd/Gm average across 20 years, as well as 75th and 25th percentile curves
# intialize lists for plotting
years = []
ygmean = []
yg75 = []
yg25 = []
for yr in range(start_yr, end_yr):
    years.append(yr)
    ygmean.append(passdf[passdf['year']==yr]['ftyPts'].mean())
    yg75.append(passdf[passdf['year']==yr]['ftyPts'].quantile(q=0.75))
    yg25.append(passdf[passdf['year']==yr]['ftyPts'].quantile(q=0.25))

plt.plot(years,ygmean,label='Average')
plt.plot(years,yg75,c='r',alpha=0.5,ls='--',label='75th percentile')
plt.plot(years,yg25,c='r',alpha=0.5,ls='--',label='25th percentile')
plt.xlabel('Year')
plt.ylabel('Total Fantasy Points per Game')
plt.title('QB Fantasy Points per game [Min 50 Att and Min 10 games]')
plt.legend(loc='best')
plt.savefig('images/QBpoints.jpg')
plt.show()
plt.close()
