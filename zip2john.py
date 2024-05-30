import subprocess
import os

def extract_hash_from_zip(zip_file, hash_file):
    # Run zip2john and write the output to a hash file
    with open(hash_file, 'w') as f:
        subprocess.run(['zip2john', zip_file], stdout=f)

def crack_zip_password(hash_file, wordlist):
    # Run john the ripper on the hash file using the provided wordlist
    result = subprocess.run(['john', '--wordlist=' + wordlist, hash_file], capture_output=True, text=True)
    print(result.stdout)

def show_cracked_password(hash_file):
    # Show the cracked password
    result = subprocess.run(['john', '--show', hash_file], capture_output=True, text=True)
    print(result.stdout)

def main(zip_file, wordlist):
    hash_file = 'zip_hash.txt'
    
    # Extract hash from zip file
    extract_hash_from_zip(zip_file, hash_file)
    
    # Crack the zip password
    crack_zip_password(hash_file, wordlist)
    
    # Display the cracked password
    show_cracked_password(hash_file)
    
    # Clean up hash file
    if os.path.exists(hash_file):
        os.remove(hash_file)

if __name__ == "__main__":
    zip_file = 'example.zip'  # Replace with your zip file
    wordlist = 'wordlist.txt'  # Replace with your wordlist file
    
    main(zip_file, wordlist)
