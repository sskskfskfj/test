from app.embedder import SimilartyBaseLogic

test = SimilartyBaseLogic()
test.getSentenceFromJson()

print(f"Related query: {test.getSimilarity('취업하려면 뭘 준비해야 하나요?')}")
print(f"Off-topic query: {test.getSimilarity('오늘 점심 뭐 먹지?')}")
