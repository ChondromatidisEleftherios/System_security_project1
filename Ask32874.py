import Ask12874
import Ask22874

def hash_selection_menu(file_path):
	while True:
		print("\nΕπιλέξτε μέθοδο hash: ")
		print("Πατήστε 1 για SHA-1")
		print("Πατήστε 2 για SHA-256")
		print("Πατήστε 3 για SHA3-256")
		print("Πατήστε 4 για MD5")
		choice = input()
		if choice == "1":
			hash_value = Ask12874.calculate_file_hash(file_path,"sha1")
			if hash_value is not False:
				print("Αποτέλεσμα: " + hash_value)
				print("\nΑν θελετε να αποθηκευτεί σε ένα αρχείο txt η Hash, πατήστε 1")
				ch=input()
				if ch == "1":
					file_name_with_hash = file_path[:-4] + "_sha1ver.txt"
					with open(file_name_with_hash, 'w') as file:
						file.write(hash_value)
			else:
				print("\nΠροέκυψε σφάλμα!!!")
		elif choice == "2":
			hash_value = Ask12874.calculate_file_hash(file_path,"sha256")
			if hash_value is not False:
				print("Αποτέλεσμα: " + hash_value)
				print("\nΑν θελετε να αποθηκευτεί σε ένα αρχείο txt η Hash, πατήστε 1")
				ch=input()
				if ch == "1":
					file_name_with_hash = file_path[:-4]  + "_sha256ver.txt"
					with open(file_name_with_hash, 'w') as file:
						file.write(hash_value)
			else:
				print("Προέκυψε σφάλμα!!!")
		elif choice == "3":
			hash_value = Ask12874.calculate_file_hash(file_path,"sha3_256")
			if hash_value is not False:
				print("Αποτέλεσμα: " + hash_value)
				print("\nΑν θελετε να αποθηκευτεί σε ένα αρχείο txt η Hash, πατήστε 1")
				ch=input()
				if ch == "1":
					file_name_with_hash = file_path[:-4] + "_sha3_256ver.txt"
					with open(file_name_with_hash, 'w') as file:
						file.write(hash_value)
			else:
				print("\nΠροέκυψε σφάλμα!!!")
		elif choice == "4":
			hash_value = Ask12874.calculate_file_hash(file_path,"md5")
			if hash_value is not False:
				print("Αποτέλεσμα: " + hash_value)
				print("\nΑν θελετε να αποθηκευτεί σε ένα αρχείο txt η Hash, πατήστε 1")
				ch=input()
				if ch == "1":
					file_name_with_hash = file_path[:-4]  + "_md5ver.txt"
					with open(file_name_with_hash, 'w') as file:
						file.write(hash_value)
			else:
				print("\nΠροέκυψε σφάλμα!!!")
		else:
			print("\nΔεν υπάρχει αυτή η επιλογή.")
		print("\nΠληκτρολογήστε Ναι αν θέλετε να επαναλάβετε τη διαδικασία.")
		option=input()
		option=option.upper()
		if option != "ΝΑΙ":
			return hash_value
		print("Αν επιθυμείτε να χρησιμοποιήσετε διαφορετικό αρχείο, γράψτε Ναι")
		option=input()
		option=option.upper()
		if option == "ΝΑΙ":
			print("Δώστε τη τοποθεσία του νέου αρχείου")
			file_path=input()

def verification(current_hash):
	while True:
		print("\nΔώσε το όνομα του αρχείου που περιέχει τη γνωστή hash τιμή")
		original_hash = input()
		result = Ask22874.verify_file_integrity(original_hash, current_hash)
		if not result:
			print("Δεν είναι ίδια! Το αρχείο έχει αλλοιωθεί!")
			print("Πληκτρολογήστε Ναι αν επιθυμείτε να προσπαθήσετε ξανά;")
			choice = input()
			choice = choice.upper()
			if choice != "ΝΑΙ":
				return True
		else:
			print("\nΕίναι ίδια! Το αρχείο δεν έχει υποστεί καμία αλλαγή.")
			return True

def main():
 print("Εργαστηριακή Άσκηση - Έλεγχος Ακεραιότητας Αρχείων") 
 print("Δώστε τη τοποθεσία του αρχικού αρχείου")
 file_path=input()
 current_hash=hash_selection_menu(file_path)
 print("\n\nΠληκτρολογήστε Ναι αν επιθυμείτε να ελέγξετε την ακεραιότητα των hash")
 print("Σημείωση: Για ορθό έλεγχο, πρέπει και τα δύο αρχεία να έχουν χρησιμοποιήσει τον ίδιο αλγόριθμο hash.")
 choice = input()
 choice = choice.upper()
 if choice == "ΝΑΙ":
 	end=verification(current_hash)
 	return end

if __name__ == "__main__":
 main()
