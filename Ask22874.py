def verify_file_integrity(original_hash, current_hash):
    try:
        with open(original_hash, 'r') as file:
            original_hash = file.read() 
            print("Το περιεχόμενο του αρχείου είναι:", original_hash)
    except FileNotFoundError:
        print("Το αρχείο δεν βρέθηκε!")
    if original_hash and current_hash:
        original_hash = original_hash.strip()
        current_hash = current_hash.strip()
        if current_hash == original_hash:
            return True
        return False
    else:
        return False
