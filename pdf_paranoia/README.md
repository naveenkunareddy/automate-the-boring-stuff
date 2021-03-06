# PDF Paranoia

Using the `os.walk()` function, write a script that will go through every PDF in a folder (and its subfolders) and encrypt the PDFs using a password provided on the command line. Save each encrypted PDF with an _encrypted.pdf suffix added to the original filename. Before deleting the original file, have the program attempt to read and decrypt the file to ensure that it was encrypted correctly.

Then, write a program that finds all encrypted PDFs in a folder (and its subfolders) and creates a decrypted copy of the PDF using a provided password. If the password is incorrect, the program should print a message to the user and continue to the next PDF.

## Sample Output
#### Before Encryption
<p align=center>
  <img src=./images/before_encryption.png alt=files before running encrypt_pdfs()>
</p>

#### After Encryption
<p align=center>
  <img src=./images/after_encryption.png alt=files after running encrypt_pdfs()>
</p>

#### After Decryption
<p align=center>
  <img src=./images/after_decryption.png alt=files after running edcrypt_pdfs()>
</p>
