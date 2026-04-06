import torch
import json
from sentence_transformers import SentenceTransformer
from transformers import logging

logging.set_verbosity_error()

EMBEDDING_MODEL = "jhgan/ko-sroberta-multitask"
FILE_DIR = "data/dummy.json"

class SimilartyBaseLogic():
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        self.baseQuestions = []
        self.baseAnswers = []

    def getSentenceFromJson(self, fileDir : str = FILE_DIR):
        with open(fileDir, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                for key, value in item.items():
                    self.baseQuestions.append(key)
                    self.baseAnswers.append(value)

    def getSimilarity(self, question : str) -> str:
        queryEmbedding = self.model.encode(question) # q
        keyEmbedding = self.model.encode(self.baseQuestions)

        #print(queryEmbedding.shape)
        #print(keyEmbedding.shape)
        similarities = self.model.similarity(queryEmbedding, keyEmbedding)

        if (torch.sum(similarities) / similarities.size()[1]) < 0.4:
            return "주제를 벗어난 질문"
        else:
            highSimilarityIndex = torch.argmax(similarities)
            return self.baseAnswers[highSimilarityIndex]


if __name__ == "__main__":
    test = SimilartyBaseLogic()

    test.getSentenceFromJson()
    print(test.getSimilarity("어떻게 의사가 되실 생각을 하셨나요?"))
    print(test.getSimilarity("안녕하세요"))






