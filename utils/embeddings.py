from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def text_splitter(yt_transcript):
    transcript = yt_transcript[0]

    text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 1000,
    chunk_overlap  = 100,
    )

    texts = text_splitter.create_documents([transcript.page_content])
    return texts

def create_vector_database(docs):
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    return db

def save_vector_database(db,filename):
    db.save_local(filename)

def load_vector_database(filename):
    db = FAISS.load_local(filename)

    return db