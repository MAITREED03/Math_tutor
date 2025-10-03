
from google import genai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()


def solve_math(question):

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents = "You are a Mathematics expert. Please solve this mathematics problem and give me the correct answer: " + question,
        
    )
    
    return response.text



def main():
    
    html_temp = """
    <div style="background-color:red;padding:8px">
    <h2 style="color:white;text-align:center;">Solving Mathematics Problems by AI Tutor</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)    

    st.markdown("""

        <style>
            .stFileUploader label {
                font-size: 40px; /* Adjust font size as needed */
            }

        </style>

    """, unsafe_allow_html=True)

    st.image("logo.jpg", width=500)
   
    math_problem = st.text_input("**Math Problem/Question**","")
    
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #2E8B57;
        color:#eeffee;
    }
    </style>""", unsafe_allow_html=True)

    if st.button("Solve"):
        
        result = solve_math(math_problem)
        print(result)
        
        st.success('Solution: {}'.format(result))
    

if __name__=='__main__':
    main()

