class Vigenere:
	def __init__(self, a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
		"""Inicia a classe com alfabeto default ou personalizado"""
		self.alphabet = a
		self.size = len(a)
		self.char_to_index = {char: idx for idx, char in enumerate(a)}

	def extend_key(self, key, text_length):
		"""expade os caractereres da chave ate o tamanho do texto"""
		return (key * (text_length // len(key) + 1))[:text_length]

	def encrypt(self, plaintext, key):
		if not key or not all(c in self.alphabet for c in key):
			raise ValueError("Chave Inválida")
		if not all(c in self.alphabet for c in plaintext):
			raise ValueError("O texto contém caracteres fora do alfabeto")

		extended_key = self.extend_key(key, len(plaintext))
		ciphertext = []

		for p, k in zip(plaintext, extended_key):
			p_index = self.char_to_index[p]
			k_index = self.char_to_index[k]
			c_index = (p_index + k_index) % self.size
			ciphertext.append(self.alphabet[c_index])

		return ''.join(ciphertext)

	def decrypt(self, ciphertext, key):
		if not key or not all(c in self.alphabet for c in key):
			raise ValueError("Chave Inválida")
		if not all(c in self.alphabet for c in ciphertext):
			raise ValueError("O texto contém caracteres fora do alfabeto")

		extended_key = self.extend_key(key, len(ciphertext))
		plaintext = []

		for c, k in zip(ciphertext, extended_key):
			c_index = self.char_to_index[c]
			k_index = self.char_to_index[k]
			p_index = (c_index - k_index) % self.size
			plaintext.append(self.alphabet[p_index])

		return ''.join(plaintext)
