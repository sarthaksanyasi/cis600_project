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
	nanThreshold = 0.6
	enc = OrdinalEncoder()
	le = LabelEncoder()
	imputer = SimpleImputer(strategy="mean")
	labelCol = ''


	#Read file
	df = pd.read_csv('breast-cancer.csv')
	
	labelCol = 'diagnosis'
	
	#Label categorical data
	#get label from user 

	df[labelCol] = enc.fit_transform(df[[labelCol]])

	#ordinal encoder

	print(enc.categories_)
	print(df.shape)
	
	#Replace ? with NaN
	df = df.replace("?", np.nan)
	print(df)
	print(df.shape)
	#Check the % of NaN in each column
	x=df.isna().sum()/len(df)*100
	#print(x[2])
	#print(type(x))
	
	#Drop the columns with more than x % NaN values
	df.dropna(thresh=nanThreshold*len(df),axis=1,inplace=True)

	#print(df2)

	#Imputation
	
	imputer.fit(df)
	imputedDF = imputer.transform(df)
	#print(imputedDF)
	#print(pd.DataFrame(imputedDF))

	idf = pd.DataFrame(imputedDF)

	print(idf)

	return 0

#Main

prepdata()
