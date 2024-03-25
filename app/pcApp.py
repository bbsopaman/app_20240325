import streamlit as st
import joblib

# 頁面標題
st.title("IRIS 品種測試")

# 載入模型  # 會涉及路徑
svm = joblib.load("app/svc_model.joblib")
knn = joblib.load("app/knn_model.joblib")
lr = joblib.load("app/lr_model.joblib")
rf = joblib.load("app/rf_model.joblib")

# 左側：選單欄
name = st.sidebar.selectbox("### 請選擇分類器", 
                             ("KNN", 
                              "LogisticRegression", 
                              "SVM", 
                              "Randomforest"))

if name == "KNN":
    model = knn

if name == "LogisticRegression":
    model = lr

if name == "SVM":
    model = svm

if name == "Randomforest":
    model = rf

# 右側：接收資料並預測
s1 = st.slider("花萼長度：", 3.5, 8.5, 4.0)
s2 = st.slider("花萼寬度：", 1.5, 5.5, 2.1)
s3 = st.slider("花瓣長度：", 0.5, 7.5, 2.4)
s4 = st.slider("花瓣長度：", 0.05, 3.5, 1.1)

labels = ['setosa', 'versicolor', 'virginica']
response = st.button("進行預測")

if response:
    X = [[s1, s2, s3, s4]]   # 二維
    y_hat = model.predict(X) # 一維  # 也只有第一筆有資料
    st.write("### 預測結果：", y_hat[0])  # 若列印 y_hat 只會出現[有資料, 後面空白]
    st.write("### 品種名稱：", labels[y_hat[0]])