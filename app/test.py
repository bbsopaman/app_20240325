"""streamlit test"""

import streamlit as st
import numpy as np
import pandas as pd

# # 任何修改，存檔後，到網頁更新就呈現
# # -------# 網頁結構
# st.title("st.titleABC")
# st.write("st.writeABCV")
# st.header("st.headerABV")
# st.text("st.textAVB")

# # -------# 字體大小寫
# # "#" 表示文字大寫到小寫，隔1個空白
# st.write("# ABC")
# st.write("## ABC")
# st.write("### ABC")
# st.write("#### ABC")
# st.write("##### ABC")
# st.write("###### ABC")

# # -------# 表格
# a = np.array([[1,2,3],[3,4,5],[7,8,9],])
# st.write(a)

# b = np.array([[1,2],[3,4],[5,6],[7,8],])
# st.write(b)

# st.table(a)
# st.table(b)

# c = pd.DataFrame(a)
# d = pd.DataFrame(b)
# st.write(c)
# st.table(d)

# name = "John Wick"
# st.write(name, b[0])

# -------# 網頁常用元件
# 簡易底色
# st.info(name)

# # 核取方塊
# st.write("核取方塊-------------")

# checkbox_1 = st.checkbox("美食")
# if checkbox_1:
#     st.info("喜歡美食")
# else:
#     st.info("我在減肥")

# checkbox_2 = st.checkbox("運動")
# if checkbox_2:
#     st.info("喜歡運動")
# else:
#     st.info("沙發上追劇")

# # 核取方塊2
# st.write("核取方塊2-------------")

# columns = st.columns(3)
# with columns[0]:
#     c0 = st.checkbox("A")
#     if c0:
#         st.info("A")

# with columns[1]:
#     c1 = st.checkbox("B")
#     if c1:
#         st.info("B")

# with columns[2]:
#     c2 = st.checkbox("C")
#     if c2:
#         st.info("C")

# # 選項按鈕
# st.write("選項按鈕-------------")

# radio1 = st.radio("性別：", ("男", "女", "新人類"), index=2)
# st.info(radio1)

# # 新增第二個選項時，要設定key=任何字串，網頁才不會跳ERR
# st.write("選項按鈕-------------")

# radio2 = st.radio("性別：", ("男", "女", "新人類"), index=2, key="key")
# st.info(radio2)

#選項按鈕2
st.write("### 選項按鈕2")

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("input number1:")
with col2:
    num2 = st.number_input("input number2:", key="num2")

response = st.radio("計算:", ("加", "減", "乘", "除"), key="radio")
# if response == "加":
#     st.write("{} + {} = {}".format(num1, num2, num1+num2))
if response == "加":
    st.write(f"{num1} + {num2} = {num1+num2}")
if response == "減":
    st.write("{} - {} = {}".format(num1, num2, num1-num2))
if response == "乘":
    st.write(f"{num1} * {num2} = {num1*num2}")
if response == "除":
    if num2 != 0:
        st.write("{} / {} = {}".format(num1, num2, num1/num2))
    else:
        st.info("number2 could not be zero.")

# 滑桿
st.write("滑桿--------------")
re5 = st.slider("amount", step=1)
st.info(re5)

# 下拉選單
st.write("下拉選單--------------")
re6 = st.selectbox("分類器", ("KNN", "SVC", "TREE"))
st.info(re6)