import streamlit as st
import time

st.set_page_config(page_title="IELTS Speaking Part 1", page_icon="🎤", layout="centered")

# Danh sách câu hỏi
QUESTIONS = [
    "What kind of job do you hope to have in the future?",
    "Do you think you will need any special training or qualifications for this career?",
    "How do you think technology will change the type of work you want to do?",
    "Would you prefer to work for a big company or start your own business in the future?",
    "Is it easy to find your dream job in your country nowadays?"
]

st.title("🎤 IELTS Speaking Part 1 Simulator")
st.subheader("Chủ đề: Future Work / Career")
st.info("Hệ thống sẽ chạy qua 5 câu hỏi. Mỗi câu bạn có 1 phút chuẩn bị và 1 phút để nói. Hãy mở phần mềm ghi âm trên điện thoại/máy tính của bạn để lưu lại bài nói.")

if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'status' not in st.session_state:
    st.session_state.status = "Sẵn sàng"

def next_question():
    st.session_state.current_q += 1

if st.session_state.current_q < len(QUESTIONS):
    q_idx = st.session_state.current_q
    st.markdown(f"### 📍 Câu hỏi số {q_idx + 1}/5:")
    st.success(QUESTIONS[q_idx])
    
    # Giả lập đọc (Dùng Audio hỗ trợ trực tuyến thay vì pyttsx3 để tránh lỗi máy chủ)
    st.audio(f"https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q={QUESTIONS[q_idx].replace(' ', '%20')}", format="audio/mp3")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⏳ Bắt đầu 1 phút CHUẨN BỊ"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            for percent_complete in range(100):
                time.sleep(0.6) # Giả lập 60 giây (tốc độ test nhanh có thể chỉnh lại)
                progress_bar.progress(percent_complete + 1)
                status_text.text(f"Thời gian chuẩn bị còn lại... {60 - int(percent_complete*0.6)}s")
            st.warning("🔔 HẾT GIỜ CHUẨN BỊ! Hãy chuẩn bị bấm nút trả lời.")
            
    with col2:
        if st.button("🔴 Bắt đầu 1 phút TRẢ LỜI"):
            progress_bar_speak = st.progress(0)
            status_text_speak = st.empty()
            for percent_complete in range(100):
                time.sleep(0.6)
                progress_bar_speak.progress(percent_complete + 1)
                status_text_speak.text(f"🔊 Đang đếm giờ nói... Còn lại {60 - int(percent_complete*0.6)}s")
            st.error("🛑 HẾT GIỜ NÓI!")

    st.button("Câu hỏi tiếp theo ➡️", on_click=next_question)

else:
    st.balloons()
    st.success("🎉 Bạn đã hoàn thành bài luyện tập IELTS Speaking Part 1!")
    
    # Khung Feedback hiển thị cho học sinh
    st.markdown("---")
    st.markdown("## 📊 KHUNG ĐÁNH GIÁ & SỬA LỖI TỰ CHẤM")
    
    with st.expander("🔍 1. Fluency and Coherence (Độ trôi chảy & Mạch lạc)"):
        st.write("- Trả lời trực tiếp câu hỏi, mở rộng bằng cấu trúc: *Answer -> Explain -> Example*.")
        st.write("- Dùng các từ nối tự nhiên: *Actually, To be honest, From my perspective...*")
        
    with st.expander("📚 2. Lexical Resource (Từ vựng chủ đề Career)"):
        st.write("- Nên dùng: *Career path (Con đường sự nghiệp), Lucrative income (Thu nhập cao), Follow my passion (Theo đuổi đam mê), Nine-to-five job (Việc hành chính)*.")
        
    with st.expander("🛠️ 3. Grammatical Range (SỬA NGỮ PHÁP HAY GẶP)"):
        st.error("⚠️ Lỗi thì tương lai: Vì hỏi về tương lai, tránh lặp lại từ 'I will' quá nhiều. Hãy thay bằng:")
        st.code("I am planning to...\nI aspire to be...\nI see myself working as...")
        st.write("- Kiểm tra lại đuôi chia động từ: *He wants* (Không được nói *He want*).")
        
    with st.expander("🗣️ 4. Pronunciation (SỬA PHÁT ÂM HAY GẶP)"):
        st.error("⚠️ Lỗi quên âm đuôi (Ending sounds) và trọng âm:")
        st.write("- Bật rõ âm đuôi: **/s/, /z/, /t/, /d/** (Ví dụ: *job* khác với *jobs*, *work* khác với *worked*).")
        st.write("- Nhấn đúng trọng âm: *ca'reer* (âm 2), *'qualification* (âm 4).")
        
    if st.button("🔄 Luyện tập lại từ đầu"):
        st.session_state.current_q = 0
        st.rerun()