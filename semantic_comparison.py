
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the pretrained model
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_similarity(text1, text2):
    """
    Compare two texts based on their meaning.
    Returns a similarity percentage.
    """

    if not text1.strip() or not text2.strip():
        return 0.0

    # Convert both texts into numerical embeddings
    embeddings = model.encode([text1, text2])

    # Calculate similarity between the embeddings
    score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    # Convert the score into a percentage
    percentage = max(0.0, min(100.0, float(score) * 100))

    return percentage
