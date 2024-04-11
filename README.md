# OAEP_RSA
This script demonstrates the OAEP RSA encryption method using the PyCryptodome library. It generates a 256-bit symmetric key (for key encapsulation), encrypts it using the OAEP RSA method, and then decrypts it for the user. The process is printed to terminal as it goes and the script does not require any input as it is a demonstration. Though it can easily be extended with an input function. At the end of execution it "clears" all sensitive data/keys.

The main method is the entry point for the script and includes all of our print statements adjacent to their respective methods. The key_gen method generates the public and private keys along with the symmetric key, which emulates a "pre-shared secret". The encrypt method encrypts the symmetric key using the public key after correctly setting up the implementation. The decrypt method decrypts the symmetric key using the private key after also correctly setting up the implementation.

In practice, access to the private key would be restricted to the owner of the key and it would involce 2 parties.
