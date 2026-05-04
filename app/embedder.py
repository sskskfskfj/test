import torch
import json
from sentence_transformers import SentenceTransformer
from transformers import logging

logging.set_verbosity_error()

EMBEDDING_MODEL = "jhgan/ko-sroberta-multitask"
FILE_DIR = "data/dummy.json"

class SimilartyBaseLogic():
    def __init__(self):
        print("모델 로딩 중...")
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        self.model.encode("warm up")
        self.baseQuestions = []
        self.baseAnswers = []
        self.keyEmbedding = None
        self.is_ready = False

    def getSentenceFromJson(self, fileDir : str = FILE_DIR):
        with open(fileDir, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                for key, value in item.items():
                    self.baseQuestions.append(key)
                    self.baseAnswers.append(value)
        
        # 질문 임베딩 미리 계산 (캐싱)
        if self.baseQuestions:
            self.keyEmbedding = self.model.encode(self.baseQuestions)
            self.is_ready = True

    def getSimilarity(self, question : str) -> str:
        if not self.is_ready or self.keyEmbedding is None:
            return "시스템이 아직 준비 중입니다. 잠시만 기다려주세요."

        queryEmbedding = self.model.encode(question)
        similarities = self.model.similarity(queryEmbedding, self.keyEmbedding)

        # 평균이 아닌 최대 유사도를 기준으로 판단
        maxSimilarity = torch.max(similarities)
        
        if maxSimilarity < 0.4:
            return "주제를 벗어난 질문"
        else:
            highSimilarityIndex = torch.argmax(similarities)
            return self.baseAnswers[highSimilarityIndex]


if __name__ == "__main__":
    test = SimilartyBaseLogic()

    test.getSentenceFromJson()
    print(test.getSimilarity("어떻게 의사가 되실 생각을 하셨나요?"))
    print(test.getSimilarity("안녕하세요"))






