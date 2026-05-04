import torch
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = "jhgan/ko-sroberta-multitask"
model = SentenceTransformer(EMBEDDING_MODEL)

questions = ["어떻게 의사가 되실 생각을 하셨나요?", "안녕하세요", "취업에 도움 줄 준비사항"]
baseQuestions = ["아동청소년 분야 선택 이유", "현재 직장까지의 경로", "학교생활과 취업준비", "취업에 도움 줄 준비사항", "봉사활동 팁"]

for q in questions:
    queryEmbedding = model.encode(q)
    keyEmbedding = model.encode(baseQuestions)
    
    similarities = model.similarity(queryEmbedding, keyEmbedding)
    print(f"Query: {q}")
    print(f"Similarities shape: {similarities.shape}")
    print(f"Similarities: {similarities}")
    
    avg_sim = torch.sum(similarities) / similarities.size()[1]
    max_sim = torch.max(similarities)
    print(f"Average similarity: {avg_sim}")
    print(f"Max similarity: {max_sim}")
    print("-" * 20)
