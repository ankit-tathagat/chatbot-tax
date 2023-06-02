import streamlit as st
from streamlit_chat import message

from database import get_redis_connection
from chatbot import RetrievalAssistant, Message

# Initialise database

## Initialise Redis connection

redis_client = get_redis_connection()

# Set instruction

# System prompt requiring Question and Year to be extracted from the user
system_prompt = '''
You are a helpful Indian Tax Consultant knowledge base assistant. You need to capture a Question from each customer.
The Question is their query on Indian Taxation, may or may not be related to any legal information.
Think about this step by step:
- The user will ask a Question
- You will ask them for any additional information of case like parties involved
- Once you have the additional information, say "searching for answers".

Example:

User: Sumarrize the Assistant Commissioner Of Income vs M/S Hari Narain Parwal case

Assistant: Certainly, do you know the city of the Tax Appellate Tribunal?

User: yes please.

Assistant: Searching for answers.
'''

### CHATBOT APP

st.set_page_config(
    page_title="Demo",
    page_icon=":robot:",
    initial_sidebar_state="expanded"
    
)
st.image("logo.png", use_column_width=False)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5F5FF;
        color: #00008B;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('TaxCon')
st.subheader("Help us help you learn about Taxation")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

@st.cache_data
def query(question):
    response = st.session_state['chat'].ask_assistant(question)
    return response

prompt = st.text_input("What do you want to know: ","", key="input")

prev_qry = ""
if st.button('Submit', key='generationSubmit') or (prev_qry != prompt):
    prev_qry = prompt

    # Initialization
    if 'chat' not in st.session_state:
        st.session_state['chat'] = RetrievalAssistant()
        messages = []
        system_message = Message('system',system_prompt)
        messages.append(system_message.message())
    else:
        messages = []


    user_message = Message('user',prompt)
    messages.append(user_message.message())

    response = query(messages)

    # Debugging step to print the whole response
    #st.write(response)

    st.session_state.past.append(prompt)
    st.session_state.generated.append(response['content'])

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
