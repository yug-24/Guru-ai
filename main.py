import streamlit as st
import openai
import os
from dotenv import load_dotenv
import io  # For audio handling

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Guru AI: Personalized Learning Tutor for Rural Students")

# User inputs
st.markdown("### Select Your Details")
grade = st.selectbox("Grade", ["Class 5", "Class 6", "Class 7", "Class 8"])
subject = st.selectbox("Subject", ["Math", "Science", "English", "Social Studies"])
language = st.selectbox("Language", ["English", "Hindi", "Tamil", "Bengali", "Other"])

st.markdown("### Ask a Question or Request a Quiz")
query = st.text_input("Example: 'Explain photosynthesis' or 'Quiz on fractions'")

# Optional voice input
audio_file = st.file_uploader("Or speak your question (upload an audio file)", type=["wav", "mp3", "m4a"])

if st.button("Get Learning Help"):
    user_input = query
    if audio_file:
        try:
            audio_bytes = audio_file.read()
            transcript_response = openai.audio.transcriptions.create(
                model="whisper-1",
                file=io.BytesIO(audio_bytes)
            )
            user_input = transcript_response.text
            st.write(f"Transcribed Voice: {user_input}")
        except Exception as e:
            st.error(f"Voice processing error: {str(e)}. Try text input.")

    if user_input:
        # Generate explanation/quiz with GPT
        prompt = f"You are a friendly tutor for {grade} {subject} in simple {language} for rural Indian students. User query: {user_input}. Provide a clear explanation, then a short 2-3 question quiz with answers. Make it engaging and culturally relevant (e.g., use Indian examples like farming for science)."
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",  # Cheaper model for free tier
                messages=[{"role": "user", "content": prompt}]
            )
            explanation = response.choices[0].message.content
            st.markdown("### Your Personalized Lesson")
            st.write(explanation)

            # Generate visual with DALL-E
            image_prompt = f"Simple, colorful educational diagram for {grade} {subject} topic: {user_input}. Style: Cartoon for kids, with Indian elements like village scenes."
            image_response = openai.images.generate(
                model="dall-e-2",  # Free tier friendly
                prompt=image_prompt,
                n=1,
                size="512x512"
            )
            image_url = image_response.data[0].url
            st.image(image_url, caption="Visual Aid to Help You Learn")
        except Exception as e:
            st.error(f"AI error: {str(e)}. Check API key or try simpler query.")

# Simple progress tracker
if 'progress' not in st.session_state:
    st.session_state.progress = 0
st.session_state.progress += 1 if query or audio_file else 0
st.sidebar.markdown(f"### Your Progress: {st.session_state.progress} sessions done! Keep going!")