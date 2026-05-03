import streamlit as st
import math

st.title('📡 デシベル計算アプリ')
st.markdown("---")

# 入力
dbm_in = st.number_input("dBmを入力してください", value=33.0)

# 計算
mw_val = 10 ** (dbm_in / 10)
w_val = mw_val / 1000
v_val = math.sqrt(mw_val * 50 / 1000)
dbuv_50 = 20 * math.log10(v_val * 10**6)

# 表示
st.subheader("変換結果")
c1, c2 = st.columns(2)
with c1:
    st.metric("電力 (mW)", f"{mw_val:,.2f}")
    st.metric("電力 (W)", f"{w_val:,.4f}")
with c2:
    st.metric("電圧 (V)", f"{v_val:,.4f}")
    st.metric("dBμV (50Ω)", f"{dbuv_50:.2f}")
