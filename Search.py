import streamlit as st
import openai 
import os

from database import get_redis_connection, get_redis_results
from config import INDEX_NAME, COMPLETIONS_MODEL
from file_viewer import download_pdf, read_pdf

openai.api_key = "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"

# initialise Redis connection

client = get_redis_connection()

### SEARCH APP

st.set_page_config(
    page_title="TaxCon",
    page_icon=":robot:"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css')

col1, col2 = st.columns([1,2], gap = "large")

with col1:
    st.image("logo2.png", width=2, use_column_width=True)

st.title('Legal Tax Search')
st.subheader("Searching Inside Documents Made Easy")

prompt = st.text_input("","", key="input",placeholder = "Enter your search here...")

prev_query = ''
if st.button('Submit', key='generationSubmit') or (prev_query != prompt):
    prev_query = prompt
    result_df = get_redis_results(client,prompt,INDEX_NAME)
    
    # Build a prompt to provide the original query, the result and ask to summarise for the user
    summary_prompt = '''Summarise this result in a bulleted list to answer the search query a customer has sent.
    Search query: SEARCH_QUERY_HERE
    Search result: SEARCH_RESULT_HERE
    Summary:
    '''
    summary_prepped = summary_prompt.replace('SEARCH_QUERY_HERE',prompt).replace('SEARCH_RESULT_HERE',result_df['result'][0])
    # @st.cache_resource
    def summary(summary_prepped ):
        return openai.Completion.create(engine=COMPLETIONS_MODEL,prompt=summary_prepped,max_tokens=500)['choices'][0]['text']
    
    # Response provided by GPT-3
    
    st.write(summary(summary_prepped))
    
    # Display pdf document  
    with st.expander("Show Details", expanded = False):
        col1, col2, col3 = st.columns([2,1,1], gap = "large")
        with col1:
            filename = result_df['filename'][0]
            st.write(f"Filename: {filename}")

        with col2:
            score = result_df['certainty'][0]
            st.write(f"Score: {score:0.5}")

        with col3:
            download_pdf(filename)

#         with st.expander("Read the full document", expanded = False):       
#             read_pdf(filename)
        
    
    
    
    

    # Option to display raw table instead of summary from GPT-3
    #st.table(result_df)