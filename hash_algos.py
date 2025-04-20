import hashlib

def calculate_file_hash(file_path, algorithm):
	try:
		# Δημιουργία αντικειμένου hash με βάση τον επιλεγμένο αλγόριθμο
		hash_obj = hashlib.new(algorithm)

		# Άνοιγμα του αρχείου σε δυαδική (binary) μορφή για ανάγνωση
		with open(file_path, 'rb') as text:
			chunk = text.read(65536)
			while chunk:
				chunk = text.read(65536)
		hash_final = hash_obj.hexdigest()
		# Επιστρέφουμε το τελικό hash σε μορφή hex
		return str(hash_final)
    
	except (FileNotFoundError, IOError, ValueError) as e:
		# Αν υπάρξει κάποιο σφάλμα, επιστρέφουμε None
		print("Υπήρξε κάποιο σφὰλμα!")
		return False