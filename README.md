# symmetric-partial-ransomware
yes based script, which encrypts files in the execution directory upto two levels

# USE WITH CAUTION
⚠️Do not modify any key related information in one of the files,
Do the same changes in both of the files
the file for encryption - secret_gift.py contains key as binary data, just to disguise it.
the file for decryption - you_are_freed.py contains key as ascii data.

Once executed secret_gift.py will encrypt the files in the current working directory and the files in the folders upto another level.
Then, the file secret_gift.py will be deleted.

The target needs you_are_freed.py file inorder to decrypt files back.
⚠️Do not rename the encrypted files.
