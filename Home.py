from openai import OpenAI
import streamlit as st

st.logo("demo-logo.png")

st.title("DEMO-GPT ")

st.warning("This Proof of Concept is a non-production demonstration version of OSS, provided exclusively for evaluation and testing purposes. It is not intended for use in a production environment and should not be relied upon for any operational deployment.")

st.markdown("---")
st.info("""
        Sentiment: This agent is designed to analyze and summarize social media posts by identifying key 
            themes, determining sentiment, and providing a sentiment score along with 
            suggestions for improvement. 
""")
# Create buttons that link to specific pages
if st.button("Comment Sentiment", type="primary", key='sentiment'):
    st.switch_page("pages/1_Sentiment.py")
    
st.info("""
 Email Summary: This agent is an email assistant that helps with email-related tasks such as 
            summarizing conversations, writing tentative replies, and rephrasing content. 
            It follows a structured template to providing summaries and suggest follow ups.
""")

if st.button("Email Summary", type="primary", key='summarize'):
    st.switch_page("pages/2_Summary.py")
    