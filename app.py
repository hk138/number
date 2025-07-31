import streamlit as st

st.set_page_config(page_title="مسابقه حدس عدد", page_icon="🎯", layout="centered")

st.markdown(
    """
    <div style="text-align:center;">
        <h2 style="color:#4A90E2;">🎯 مسابقه شبانه حدس عدد 🎯</h2>
        <p style="font-size:18px;">شانس خودت رو امتحان کن و جایزه ببر!</p>
        <hr style="border:1px solid #4A90E2;">
    </div>
    """,
    unsafe_allow_html=True,
)

# دریافت آیدی ایتا
user_id = st.text_input("👤 آیدی ایتای خود را وارد کنید (مثلاً: @yourid):")

if user_id:
    st.info("✅ آیدی ثبت شد. حالا بازی را شروع کن.")

    if "step" not in st.session_state:
        st.session_state.step = 1

    if "in_range1" not in st.session_state:
        st.session_state.in_range1 = False

    if st.session_state.step == 1:
        st.subheader("مرحله اول: حدس محدوده اول")
        min1 = st.number_input("🔢 حد پایین:", min_value=1, max_value=99, step=1, key="min1")
        max1 = st.number_input("🔢 حد بالا:", min_value=min1 + 1, max_value=100, step=1, key="max1")

        if st.button("بررسی محدوده 1"):
            if 42 >= min1 and 42 <= max1:
                st.success("✅ عدد در این محدوده هست!")
                st.session_state.in_range1 = True
            else:
                st.warning("❌ عدد در این محدوده نیست.")
            st.session_state.step = 2

    elif st.session_state.step == 2:
        st.subheader("مرحله دوم: حدس محدوده دوم")
        min2 = st.number_input("🔢 حد پایین:", min_value=1, max_value=99, step=1, key="min2")
        max2 = st.number_input("🔢 حد بالا:", min_value=min2 + 1, max_value=100, step=1, key="max2")

        if st.button("بررسی محدوده 2"):
            if 42 >= min2 and 42 <= max2:
                st.success("✅ عدد در این محدوده هست!")
            else:
                st.warning("❌ عدد در این محدوده نیست.")
            st.session_state.step = 3

    elif st.session_state.step == 3:
        st.subheader("مرحله نهایی: عدد نهایی رو حدس بزن")
        final_guess = st.number_input("🔢 عدد مورد نظر شما:", min_value=1, max_value=100, step=1, key="final")

        if st.button("ثبت پاسخ نهایی"):
            st.success("✅ عدد شما ثبت شد!")
            st.markdown(
                f"<p style='color:green; font-size:18px;'>نتیجه ساعت ۲۱:۳۰ در کانال اعلام خواهد شد. موفق باشی {user_id}!</p>",
                unsafe_allow_html=True
            )
