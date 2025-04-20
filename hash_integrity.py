def verify_file_integrity(original_hash, current_hash):
    # Έλεγχος για κενές ή μη έγκυρες τιμές
    if original_hash and current_hash:
        # Κανονικοποίηση: αφαιρούμε περιττά κενά και μετατρέπουμε σε πεζά (για συνέπεια)
        original_hash = original_hash.strip().lower()
        current_hash = current_hash.strip().lower()
        if current_hash == original_hash:
            return True
        return False
    else:
        return False