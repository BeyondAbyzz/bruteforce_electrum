For that moment you remember some of your electrum seeds.
This code reads a text file containing 12 electrum words each line, converts them to electrum addresses and write them out to 3 other text files.

To use:
First install python, set environment path but ofcourse I am not here to teach you python.
You have to pip-install electrum(clone their repository locally and point pip to it and don't forget to make libsecp256k1 and drop in electrum folder), create a text file named "mnemonics.txt" in the same 
folder with this code and fill it with electrum words line by line.
Then run "python elektrum.py"

For each line in mnemonics.txt, the code will write out to 3 text files, the first file "electrum_addresses.txt" contains the 12 words, first receiving address and second receiving address.
the second file "addr1.txt" contains only first receiving address. The third file "addr2.txt" contains only second receiving address.

Do not use this code for any illegal activity, also this code is made to work offline, no internet connection is needed.

If the code helped you, you can support the creator
bc1qv0pfur63yvsm3tsy87v606n7usgz7pn9t3dfsp
