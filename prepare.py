from flask import Flask, request
import pandas as pd
import json as js
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder

#app = Flask(__name__)

#@app.route('/prepdata', methods=['POST'])
def prepdata(file, labelCol, nanThreshold):

	#initialize variables
	#nanThreshold = 0.6
	enc = OrdinalEncoder()
	le = LabelEncoder()
	imputer = SimpleImputer(strategy="mean")

	df=file.copy()
	df2=file.copy()

	labelCol_cat=labelCol+'_cat'

	#Label categorical data
	#get label from user 

	#df[labelCol] = enc.fit_transform(df[[labelCol]])
	df2[labelCol] = le.fit_transform(df2[labelCol])

	#ordinal encoder

	#print(enc.categories_)
	#print(df2.shape)
	
	#Replace ? with NaN
	df2 = df2.replace("?", np.nan)
	print(df2)
	print(df2.shape)
	#Check the % of NaN in each column
	x=df2.isna().sum()/len(df2)*100
	#print(x[2])
	#print(type(x))
	
	#Drop the columns with more than x % NaN values
	df2.dropna(thresh=nanThreshold*len(df2),axis=1,inplace=True)

	#print(df2)

	#Imputation
	#Encountered error before adding categorical encoding

	imputer.fit(df2)
	imputedDF = imputer.transform(df2)

	#print(imputedDF)
	#print(pd.DataFrame(imputedDF))

	idf = pd.DataFrame(imputedDF)

	print(idf)

	return 0

#Main


labelCol = ''

	
labelCol = 'diagnosis'
nanThreshold = 0.6
#Read file
df = pd.read_csv('breast-cancer.csv')

prepdata(df,labelCol,nanThreshold)
