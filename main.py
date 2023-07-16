import rsa

# Author: Aman Arabzadeh
# Date: 2023-07-16


# Function to encrypt a file using RSA public key
def encrypt_file(input_file, output_file, public_key):
    chunk_size = 245  # Adjust chunk size as needed

    try:
        # Encrypt and write chunks of the file
        with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
            while True:
                chunk = f_in.read(chunk_size)
                if not chunk:
                    break
                encrypted_chunk = rsa.encrypt(chunk, public_key)
                f_out.write(encrypted_chunk)

        print("File encrypted successfully!")
    except Exception as e:
        print("Error occurred during encryption:", str(e))


# Function to decrypt a file using RSA private key
def decrypt_file(input_file, output_file, private_key):
    chunk_size = 256  # Adjust chunk size as needed

    try:
        # Decrypt and write chunks of the file
        with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
            while True:
                chunk = f_in.read(chunk_size)
                if not chunk:
                    break
                decrypted_chunk = rsa.decrypt(chunk, private_key)
                f_out.write(decrypted_chunk)

        print("File decrypted successfully!")
    except Exception as e:
        print("Error occurred during decryption:", str(e))


try:
    # Generate RSA key pair
    (public_key, private_key) = rsa.newkeys(2048)

    # Save the keys to files
    with open('public.pem', 'wb') as f:
        f.write(public_key.save_pkcs1())  # Save the public key in PKCS#1 format

    with open('private.pem', 'wb') as f:
        f.write(private_key.save_pkcs1())  # Save the private key in PKCS#1 format

    # Encrypt a file
    encrypt_file('plain.txt', 'encrypted.txt', public_key)

    # Decrypt the file
    decrypt_file('encrypted.txt', 'decrypted.txt', private_key)

except Exception as e:
    print("An error occurred:", str(e))


# Resources for RSA encryption and decryption:
# - Python-RSA library documentation: https://stuvel.eu/python-rsa-doc/index.html
# - Public-key cryptography on Wikipedia: https://en.wikipedia.org/wiki/Public-key_cryptography
