import hmac

def secure_hash_compare(hash1, hash2):
	try:
		with open(hash1, 'r') as text:
			hash_1= text.read().strip()
	except FileNotFoundError:
		print("Σφάλμα κατά την ανάγνωση του αρχείου")
		return False
	except Exception as e:
		print("Σφάλμα κατά την ανάγνωση του αρχείου")
		return False
	try:
		with open(hash2, 'r') as text:
			hash_2= text.read().strip()
	except FileNotFoundError:
		print("Σφάλμα κατά την ανάγνωση του αρχείου")
		return False
	except Exception as e:
		print("Σφάλμα κατά την ανάγνωση του αρχείου")
		return False

	if hmac.compare_digest(hash_1, hash_2) == True:
		print("Τα αρχεία είναι ίδια! Δεν έχει υπάρξει κάποια αλλοίωση.")
		return True
	print("Τα αρχεία δεν είναι ίδια...")
	return False

while True:
	print("Δώστε το όνομα του αρχείου που περιέχει τη 1η hash")
	hash1=input()
	print("Δώστε το όνομα του αρχείου που περιέχει τη 2η hash")
	hash2=input()
	end=secure_hash_compare(hash1,hash2)
	if end==True:
		break
	print("\nΠατήστε 1 για να τερματίσετε την εκτέλεση του προγράμματος.")
	ch=input()
	if ch=="1":
		break
	print("\nΝέα προσπάθεια:")
