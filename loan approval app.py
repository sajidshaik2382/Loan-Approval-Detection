from flask import Flask, request
import pandas as pd
import numpy as np
import pickle


app =Flask(__name__)
pickle_in =open("rf.pkl","rb")
rf=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "welcome All"


@app.route('/predict')
def predict_loan():
    Term=request.args.get('Term')
    NoEmp=request.args.get('NoEmp')
    NewExist=request.args.get('NewExist')
    CreateJob=request.args.get('CreateJob')
    RetainedJob=request.args.get('RetainedJob')
    FranchiseCode=request.args.get('FranchiseCode')
    UrbanRural=request.args.get('UrbanRural')
    DisbursementGross=request.args.get('DisbursementGross')
    BalanceGross=request.args.get('BalanceGross')
    ChgOffPrinGr=request.args.get('ChgOffPrinGr')
    GrAppv=request.args.get('GrAppv')
    SBA_Appv=request.args.get('SBA_Appv')
    prediction=rf.predict([[Term,NoEmp,NewExist,CreateJob,RetainedJob,FranchiseCode,
                            UrbanRural,DisbursementGross,BalanceGross,ChgOffPrinGr,
                            GrAppv,SBA_Appv]])
    return " The predicted loan is"+ str(prediction)


@app.route('/predict_file',methods=["POST"])
def predict_loan():
    Term=request.args.get('Term')
    NoEmp=request.args.get('NoEmp')
    NewExist=request.args.get('NewExist')
    CreateJob=request.args.get('CreateJob')
    RetainedJob=request.args.get('RetainedJob')
    FranchiseCode=request.args.get('FranchiseCode')
    UrbanRural=request.args.get('UrbanRural')
    DisbursementGross=request.args.get('DisbursementGross')
    BalanceGross=request.args.get('BalanceGross')
    ChgOffPrinGr=request.args.get('ChgOffPrinGr')
    GrAppv=request.args.get('GrAppv')
    SBA_Appv=request.args.get('SBA_Appv')
    prediction=rf.predict([[Term,NoEmp,NewExist,CreateJob,RetainedJob,FranchiseCode,
                            UrbanRural,DisbursementGross,BalanceGross,ChgOffPrinGr,
                            GrAppv,SBA_Appv]])
    return " The predicted loan is"+ str(prediction)





if __name__=='__main__':
    app.run()

