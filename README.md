# RSA File Encryption/Decryption

This repository contains a Python script that demonstrates file encryption and decryption using the RSA algorithm. It utilizes the `rsa` library for RSA key generation, encryption, and decryption.

## Table of Contents

- [Usage](#usage)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [License](#license)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/AMAN-ARABZADEH/File_Encryption_RSA
   
2. Install the required dependencies:
       pip install rsa
3. Run the script:
       python  main.py


This will generate an RSA key pair, save the keys to files, encrypt a file (`plain.txt`), and then decrypt the encrypted file (`encrypted.txt`). The decrypted file will be saved as `decrypted.txt`.

4. Customize the script:

- Adjust the chunk sizes (`chunk_size`) in the `encrypt_file` and `decrypt_file` functions based on your requirements.
- Modify the input and output file paths as needed.

## Dependencies

The script relies on the following dependencies:

- `rsa`: A library for RSA encryption, decryption, and key generation. Visit [Python-RSA](https://stuvel.eu/python-rsa-doc/) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.




