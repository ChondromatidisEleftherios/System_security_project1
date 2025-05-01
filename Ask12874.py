import hashlib
import os

def calculate_file_hash(file_path, algorithm):
	try:
		if not os.path.exists(file_path):
			raise FileNotFoundError("Το αρχείο δεν βρέθηκε.")

		hash_obj = hashlib.new(algorithm)

		with open(file_path, 'rb') as f:
			while True:
				chunk = f.read(65536)  # 64KB
				if not chunk:
					break
				hash_obj.update(chunk)
		hash_final = hash_obj.hexdigest()
		
		return str(hash_final)
    
	except (IOError, ValueError) as e:
		return False
