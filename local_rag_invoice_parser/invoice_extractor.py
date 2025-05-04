from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import ollama 
import argparse
import re

template = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know.
Question: {question} 
Context: {context} 
Answer:
"""
question = '''
    Extract structured information from an invoice document. The data may be in German or English. Do not add, modify, or delete any information. Present the extracted data in XML format with the following structure:

    Sender Information:

    Name (string, or None if missing)
    Address (string, or None if missing)
    Contact details:
    Phone (string, or None if missing)
    Fax (string, or None if missing)
    Website (string, or None if missing)
    Bank details:
    Bank name (string, or None if missing)
    IBAN (string, or None if missing)
    SWIFT-BIC (string, or None if missing)
    UST-ID (string, or None if missing)
    Receiver Information:

    Name (string, or None if missing)
    Address (string, or None if missing)
    Order Details:

    Customer number (string, or None if missing)
    Order date (string in DD.MM.YYYY format, or None if missing)
    Order number (string, or None if missing)
    Invoice date (string in DD.MM.YYYY format, or None if missing)
    Invoice number (string, or None if missing)
    Items List: (Each item should have the following fields)

    Position (string or number, or None if missing)
    Article number (string, or None if missing)
    Description (string, or None if missing)
    Quantity (integer, or None if missing)
    Price per unit in EUR (float, or None if missing)
    Total price in EUR (float, or None if missing)
    VAT percentage (integer, or None if missing)
    Total Amount:

    Net amount in EUR (float, or None if missing)
    VAT amount in EUR (float, or None if missing)
    Gross amount in EUR (float, or None if missing)
    Payment Details:

    Paid at (string, or None if missing)
    Receipt order number (string, or None if missing)
    Important Notes:

    Ensure no data is omitted. If a value is missing in the document, explicitly set it to None.
    Maintain the original currency format and percentages (do not modify values).
    Keep dates in DD.MM.YYYY format.
    Preserve the language of extracted text (do not translate).

    Always give the data in XML format. No JSON and no other format
    '''
try:
    print("Cheching availability of model")
    ollama.show("deepseek-r1:8b")
except:
    print("Model not present. Downloading the model this will take few minutes to hour depending on your internet")
    ollama.pull("deepseek-r1:8b")

print("Model loading in process")
embeddings = OllamaEmbeddings(model="deepseek-r1:8b")
vector_store = InMemoryVectorStore(embeddings)
model = OllamaLLM(model="deepseek-r1:8b", max_token=4096)


def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()

    return documents

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )

    return text_splitter.split_documents(documents)

def index_docs(documents):
    vector_store.add_documents(documents)

def retrieve_docs(query):
    return vector_store.similarity_search(query)

def answer_question(question, documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    return chain.invoke({"question": question, "context": context})

def process_file(input_file, output):
    documents = load_pdf(input_file)
    file_name = input_file.split("\\")[-1]

    chunked_documents = split_text(documents)
    index_docs(chunked_documents)    
    print("Process started. System parsing the data. It may take a while.")
    related_documents = retrieve_docs(question)
    answer = answer_question(question, related_documents)
    answer = re.sub(r"<think>.*?</think>", "", answer, flags=re.DOTALL).strip()
    answer = answer.replace("```xml",'<?xml version="1.0" encoding="UTF-8"?>')
    answer = answer.replace("```","")
    with open(f"{output}/{file_name.replace('pdf','xml')}", "w", encoding="utf-8") as file:
        file.write(answer)
    print(f"XML file saved as {file_name.replace('pdf','xml')}")

if __name__ == "__main__":
    """Main function to parse arguments and process files."""
    parser = argparse.ArgumentParser(description="Process an input file and save results to an output file.")

    parser.add_argument("-i", "--input", type=str, required=True, help="Path to the input file")
    parser.add_argument("-o", "--output", type=str, required=True, help="Path to the output folder")

    args = parser.parse_args()
    print(args.input)
    print(args.output)
    process_file(args.input, args.output)