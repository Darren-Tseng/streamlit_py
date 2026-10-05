import streamlit as st

st.set_page_config(
    page_title="課程回饋中心",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---- 深色 + 橘色主題 CSS ----
st.markdown(
    """
<style>
.stApp { background: #0F172A; color: #F1F5F9; }
.hero {
  background: linear-gradient(135deg, #F97316 0%, #EC4899 55%, #8B5CF6 100%);
  border-radius: 20px; padding: 32px 36px; color: white;
  margin-bottom: 24px;
}
.hero h1 { margin: 0; font-size: 2.2rem; }
.hero p { margin: 8px 0 0 0; opacity: 0.92; }
.card {
  background: #1E293B; border: 1px solid #334155;
  border-radius: 16px; padding: 24px;
}
.ticket {
  background: linear-gradient(180deg, #1E293B, #0F172A);
  border: 2px dashed #F97316; border-radius: 16px; padding: 20px;
}
section[data-testid="stSidebar"] { background: #020617; }
div.stButton > button[kind="primary"] {
  background: linear-gradient(90deg, #F97316, #EC4899);
  border: none; border-radius: 12px; height: 3em;
  font-size: 1.05rem; font-weight: 700;
}
</style>
""",
    unsafe_allow_html=True,
)

# ---- Sidebar（保留：科系選擇在 Sidebar）----
st.sidebar.title("🎓 回饋中心")
st.sidebar.caption("學期課程意見收集")
department = st.sidebar.selectbox(
    "科系",
    ["資訊工程系", "電子工程系", "其他"],
)
st.sidebar.divider()
st.sidebar.markdown("**📊 填寫進度**")
st.sidebar.progress(70, text="3 / 4 個欄位")
st.sidebar.info("💡 約 1 分鐘完成，資料僅供教學改善使用。")

# ---- Hero（完全不同的版頭）----
st.markdown(
    """
<div class="hero">
  <h1>🎓 課程回饋中心</h1>
  <p>這裡是全新的深色回饋面板 — 左邊填寫，右邊即時預覽，送出後產生你的專屬回饋票券。</p>
</div>
""",
    unsafe_allow_html=True,
)

left, right = st.columns([1.2, 1], gap="large")

# ---- 左：表單區 ----
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("✍️ 填寫回饋")
    st.caption("帶 * 為必填")

    name = st.text_input("姓名 *", placeholder="例如：王小明")

    st.write("課程滿意度 *（1～5 分）")
    satisfaction = st.radio(
        "滿意度",
        options=[1, 2, 3, 4, 5],
        index=4,
        horizontal=True,
        label_visibility="collapsed",
    )
    st.progress(satisfaction / 5, text=f"{'⭐' * satisfaction}  {satisfaction} / 5 分")

    feedback = st.text_area(
        "意見回饋",
        placeholder="課程哪裡最有幫助？哪裡可以更好？",
        height=150,
    )

    submitted = st.button("🚀 送出回饋", type="primary", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- 右：說明 + 即時預覽 ----
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("👀 即時預覽")
    st.write(f"**姓名：** {name.strip() if name.strip() else '（尚未填寫）'}")
    st.write(f"**科系：** {department}")
    st.write(f"**滿意度：** {'⭐' * satisfaction}（{satisfaction} 分）")
    st.write(f"**意見：** {feedback.strip()[:60] + '…' if len(feedback.strip()) > 60 else (feedback.strip() if feedback.strip() else '（尚未填寫）')}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("**📌 填寫說明**")
        st.markdown("1. 請先在左側 Sidebar 確認科系\n2. 姓名為必填，未填會跳出警告\n3. 送出後會產生感謝票券")

# ---- 送出結果（橫跨全寬票券）----
if submitted:
    if not name.strip():
        st.warning("⚠️ 請先輸入姓名再送出。", icon="⚠️")
    else:
        st.balloons()
        st.markdown(
            f"""
<div class="ticket">
  <h3>🎉 感謝您的回饋！</h3>
  <p>姓名：<b>{name.strip()}</b> ｜ 科系：<b>{department}</b> ｜ 滿意度：<b>{'⭐' * satisfaction} {satisfaction} / 5</b></p>
  <p>意見：{feedback.strip() if feedback.strip() else '（未填寫）'}</p>
</div>
""",
            unsafe_allow_html=True,
        )
