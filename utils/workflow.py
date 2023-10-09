from . import chains
from . import embeddings
from . import prompt_builder
from . import prompts
from . import yt_loader

def get_vector_db_from_yt(youtube_url):
    doc = yt_loader.load_yt_video(youtube_url)
    texts = embeddings.text_splitter(doc)
    db = embeddings.create_vector_database(texts)

    return db

def generate_short_form_ideas(youtube_url):
    db = get_vector_db_from_yt(youtube_url)
    prompt_ideas = prompts.linkedin_content_creation_ideas
    qa = chains.initialize_qa_chain(db)
    ideas = chains.run_qa_chain(qa,prompt_ideas)

    return ideas