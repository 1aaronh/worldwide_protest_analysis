import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, roc_auc_score, plot_roc_curve
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

def get_dum_cols(df, list_of_columns):
    list_of_dfs = []
    for col in list_of_columns:
        col_df = pd.get_dummies(df[col])
        list_of_dfs.append(col_df)
    #combine all df's vertically, so only areas with null values are where a potential column was empty    
    dfs_concat = pd.concat(list_of_dfs, axis = 0).fillna(0)
    #convert the concatenated df with all values now filled in into a list of separate dfs - each with all columns
    num_dfs = len(list_of_columns)
    num_rows = len(df)
    list_of_final_dfs = []
    for i in range(num_dfs):
        new_df = dfs_concat[num_rows*i : num_rows*(i+1)]
        list_of_final_dfs.append(new_df)
    # create combined final df
    final_df = list_of_final_dfs[0]
    for j in range(1, len(list_of_final_dfs)):
        final_df += list_of_final_dfs[j]
    return final_df

def dummy_columns(df):
    state_responses = ['stateresponse1', 'stateresponse2', 'stateresponse3', 'stateresponse4','stateresponse5', 'stateresponse6', 'stateresponse7']
    response_cats = get_dum_cols(df, state_responses)
    df_total = pd.concat([df,response_cats],axis=1)
    return df_total

def split_scale(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
    ss = StandardScaler()
    X_train_sc = ss.fit_transform(X_train)
    X_test_sc = ss.transform(X_test)
    return X_train_sc, X_test_sc, y_train, y_test

def scoring_class(model, X1, y1, X2, y2):
    model.fit(X1, y1)
    print(f'{model} train score Accuracy: {model.score(X1, y1)}')
    print(f'{model} test score Accuracy: {model.score(X2, y2)}')

def con_plot(model, X, y, title):
    sns.set_style("white")
    metrics.plot_confusion_matrix(model, X, y, cmap='Blues', 
                          values_format='d', display_labels=['No accomodations', 'Accomodations'])
    plt.title(f'Confusion matrix of predicted accomodations vs\n actual in {title}', fontsize=16)
    plt.show();

def con_mets(model, X2, y2):
    preds = model.predict(X2)
    # Save confusion matrix values
    tn, fp, fn, tp = confusion_matrix(y2, preds).ravel()
    print(f'Specificity: {tn / (fp + tn)}')
    print(f'Sensitivity: {tp / (fn + tp)}')
    print(f'Precision:   {tp / (tp + fp)}')
    
def roc_curve(model,title,X_test,y_test):
    plot_roc_curve(model,X_test,y_test)
    plt.plot([0,1],[0,1],label='baseline',linestyle='--')
    plt.title(f'{title} ROC Curve')
    plt.legend;
