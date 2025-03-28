"""Main Module"""

from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain_community.chat_message_histories import FileChatMessageHistory


from configs.env_configs import OPENAI_API_KEY


# This is a simple example of how to use LangChain with OpenAI's ChatGPT API
# The ChatPromptTemplate is used to create a chat prompt
# The HumanMessagePromptTemplate is used to create a human message prompt
# The MessagesPlaceholder is used to create a placeholder for messages
prompt = ChatPromptTemplate(
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
    input_variables=["content", "messages"],
)

# The ChatOpenAI is used to create a chat model
llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    verbose=True
)

# The ConversationBufferMemory is used to create a memory buffer for the conversation
memory = ConversationSummaryMemory(
    chat_memory=FileChatMessageHistory("chat_history.json"),
    memory_key="messages",
    return_messages=True,
    llm=llm,
    max_token_limit=1000
)

# The LLMChain is used to create a chain of operations
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True
)

# Here, there is now= mechanism to store the conversation history
while True:
    content = input(">> ")
    if content == "exit":
        break
    response = chain({"content": content})
    # print(response)
    print(response["text"])
