import streamlit as st

st.set_page_config(
    page_title="課程回饋表單",
    page_icon="📝",
    layout="centered",
)

# ---- Sidebar ----
st.sidebar.header("📋 基本資料")
department = st.sidebar.selectbox(
    "科系",
    ["資訊工程系", "電子工程系", "其他"],
)
st.sidebar.divider()
st.sidebar.info("💡 填寫約需 1 分鐘，所有資料僅供教學改善使用。")

# ---- Main ----
st.title("📝 課程回饋表單")
st.markdown(
    "> 歡迎填寫本課程回饋表單，您的意見將幫助我們改善教學品質。\n"
    "> 請填寫以下欄位後按下送出。"
)

with st.container(border=True):
    name = st.text_input(
        "姓名",
        placeholder="請輸入您的姓名",
        help="請填寫真實姓名以利後續聯繫",
    )

    col_sat, col_tip = st.columns([3, 2])
    with col_sat:
        satisfaction = st.slider("課程滿意度", min_value=1, max_value=5, value=5)
    with col_tip:
        st.metric("目前評分", f"{satisfaction} / 5")
        if satisfaction >= 4:
            st.caption("😊 很高興你喜歡這門課！")
        elif satisfaction == 3:
            st.caption("😐 還有進步空間")
        else:
            st.caption("🙏 感謝直言，我們會改進")

    feedback = st.text_area(
        "意見回饋",
        placeholder="請分享您對課程內容、教學方式的建議…",
        height=140,
    )

    submitted = st.button("送出回饋 ✨", type="primary", use_container_width=True)

if submitted:
    if not name.strip():
        st.warning("⚠️ 請先輸入姓名再送出。", icon="⚠️")
    else:
        st.balloons()
        st.success("感謝您的回饋！")
        with st.container(border=True):
            st.subheader("✅ 已收到以下內容")
            c1, c2, c3 = st.columns(3)
            c1.metric("姓名", name.strip())
            c2.metric("科系", department)
            c3.metric("滿意度", f"{satisfaction} 分")
            if feedback.strip():
                with st.expander("查看意見回饋", expanded=True):
                    st.write(feedback)
            else:
                st.caption("（未填寫意見回饋）")
