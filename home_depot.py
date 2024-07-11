import pandas as pd
import tiktoken
import os
import openai
from langchain.document_loaders.csv_loader import CSVLoader 
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
import os
from langchain_openai import ChatOpenAI
import warnings


# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


#from openai.embeddings_utils import get_embedding

from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.prompts import PromptTemplate


api_key = 'Openai_key' 
os.environ['OPENAI_API_KEY'] = api_key

def recommend(query):
    loader = CSVLoader(file_path="home_depot_updated.csv")
    data = loader.load()

    # Text Splitter
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)

    # Embeddings Model (assuming you want to use OpenAIEmbeddings)
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    # LLM (Large Language Model) for document processing
    #llm = OpenAI(openai_api_key=api_key)

    # Vector Database for document search
    docsearch = Chroma.from_documents(texts, embeddings)

    docs = docsearch.similarity_search(query, k=1)

    template = """You are a recommendation system for Home Depot that assists users in finding products that match their needs. For each query, suggest five products from Home Depot with the following details:

    Generate a product recommendation response for a Home Depot product in the following format:
    Product name:\n
    - Description:\n
    - Availability:\n
    - Price:\n
    - Brand:\n
    

    Product name: 20 in. x 26 in H. Recessed or Surface Mount Mirrored Medicine Cabinet in Oil Rubbed Bronze
    - Description: Showcasing elegant bronze detailing on its frame, this wall-mounted medicine cabinet features a reversible door that can be installed with a left- or right-hand hinge. Mirrors are positioned on the front and back of the door as well as the interior back of the cabinet. Two adjustable glass shelves hold your toiletries and bath items. Durable aluminum construction makes this cabinet rust- and rot-resistant.
    - Availability: InStock
    - Price: 162.42 USD
    - Brand: KOHLER
   
    

    Product name: 20 in. x 26 in H. Recessed or Surface Mount Mirrored Medicine Cabinet in Oil Rubbed Bronze
    - Description: Showcasing elegant bronze detailing on its frame, this wall-mounted medicine cabinet features a reversible door that can be installed with a left- or right-hand hinge. Mirrors are positioned on the front and back of the door as well as the interior back of the cabinet. Two adjustable glass shelves hold your toiletries and bath items. Durable aluminum construction makes this cabinet rust- and rot-resistant.
    - Availability: InStock
    - Price: 162.42 USD
    - Brand: KOHLER


    {context}

    Question: {question}
    Your response:"""


    PROMPT = PromptTemplate(
        template=template, input_variables=["context", "question"])

    chain_type_kwargs = {"prompt": PROMPT}

    llm=ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0) 

    qa = RetrievalQA.from_chain_type(llm=llm, 
        chain_type="stuff", 
        retriever=docsearch.as_retriever(),
        return_source_documents=True, 
        chain_type_kwargs=chain_type_kwargs)

    result = qa({'query':query})
    return (result['result'])







