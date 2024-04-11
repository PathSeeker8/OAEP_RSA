#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import statements
import sys
import string
import os

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Random import get_random_bytes

# Global variables (None for this script)

def main(args):
    print(f"\nThis script encrypts a 256-bit symmetric key (emulating a 'pre-shared' secret) using the OAEP RSA method and also decrypts it for you as well. No input is needed as this is a demonstration. Please wait...")
    
    public_key, private_key, symmetric_key = key_gen()
    print(f"\n*** Running the OAEP RSA cipher based on these generated keys *** \n" + f"\nPublic key (Raw): \n{public_key.decode()}\n" 
          + f"\nPrivate Key (): \nThat key is TOP SECRET!\n" + f"\nSymmetric key (Hex): \n{symmetric_key.hex()}")
    
    print("\n*** Encapsulating and decapsulating the symmetric key using our generated keys with OAEP RSA ***")
    encapsulated_key = encrypt(public_key, symmetric_key)
    print(f"\nEncapsulated symmetric key (Hex): \n{encapsulated_key.hex()}")

    decapsulated_key = decrypt(private_key, encapsulated_key)
    print(f"\nDecapsulated symmetric key (Hex): \n{decapsulated_key.hex()}")

    del public_key, private_key, symmetric_key, encapsulated_key, decapsulated_key
    print("\n*** OAEP RSA cipher on key encapsulation implementation complete. All sensitive data has been cleared. ***\n")

def key_gen():
    key_pair = RSA.generate(3072)
    
    public_key = key_pair.public_key().export_key()
    private_key = key_pair.export_key()
    
    symmetric_key = get_random_bytes(32)
    
    return public_key, private_key, symmetric_key

def encrypt(public_key, symmetric_key):
    try:
        enc_public_key = RSA.import_key(public_key)
        ciphertext = PKCS1_OAEP.new(enc_public_key)
        enc_symmetric_key = ciphertext.encrypt(symmetric_key)
        
        return enc_symmetric_key
        
    except Exception as error:
        print(f"Encountered an error during encryption: {error}")
        sys.exit()

def decrypt(private_key, enc_symmetric_key):
    try:
        dec_private_key = RSA.import_key(private_key)
        ciphertext = PKCS1_OAEP.new(dec_private_key)
        dec_symmetric_key = ciphertext.decrypt(enc_symmetric_key)
        
        return dec_symmetric_key
    
    except Exception as error:
        print(f"Encountered an error during decryption: {error}")
        sys.exit()

if __name__ == '__main__':
    main(sys.argv[1:])