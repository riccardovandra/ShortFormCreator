from langchain.document_loaders import YoutubeLoader

def load_yt_video(url):
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
    doc = loader.load()

    return doc