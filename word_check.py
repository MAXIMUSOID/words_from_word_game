from config import WORD
class WordCheck():
	def __init__(self):
		self.dictionary = self.ChekerInicialize()

	def ChekerInicialize(self):
		with open('test.txt', mode="r", encoding="utf-8") as f:
			dictionary=f.readlines()
			dictionary = list(map(lambda x: x.replace('\n', ''), dictionary))
		return dictionary

	def SubWordIsDictionary(self, subWord:str) -> bool:
		if len(subWord) == 0:
			return False
		return subWord.lower() in self.dictionary

	def is_word_generated(self, word_check:str, word_target:str)->bool:
		if len(word_check) == 0:
			return False
		word_target_list = list(word_target)
		for char in word_check:
			try:
				word_target_list.remove(char)
			except:
				return False
		return True
		

	def get_answer_number(self, word) -> int:
		count = 0
		for answer in self.dictionary:
			if self.is_word_generated(answer, word):
				print(answer)
				count += 1
		return count

if __name__ == "__main__":
	
	WC = WordCheck()
	print(WC.get_answer_number(WORD))
