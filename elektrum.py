from electrum import bitcoin
from electrum import keystore
from electrum.mnemonic import Mnemonic
from tqdm import tqdm



def read_mnemonics(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()
    
def generate_address(input_file, file1, file2, file3):
    seeds = read_mnemonics(input_file)
    with open(file1, 'w') as f, open(file2, 'w') as k, open(file3, 'w') as t:
        for seed in tqdm(seeds, desc='Generating addresses', unit='addresses'):
            try:
                
                k = keystore.from_seed(seed, passphrase=False)

                master_public_key = k.get_master_public_key()

                pubkey = k.derive_pubkey(for_change=0, n=0)

                pubkey1 = k.derive_pubkey(for_change=0, n=1)

                address = bitcoin.public_key_to_p2pkh(pubkey, net=None)

                address1 = bitcoin.public_key_to_p2pkh(pubkey1, net=None)
                
                f.write(f"{seed}, electrum Address: {address}, {address1} \n")
                k.write(address + '\n')
                t.write(address1 + '\n')



            except Exception as e:
                print(f"Error converting mnemonic to address: {e}")
                continue             
            
        
        
input_file_path = 'mnemonics.txt'
file1 = 'electrum_addresses44.txt'
file2 = 'addr1.txt'
file3 = 'addr2.txt'
generate_address(input_file_path, file1, file2, file3)



#'omit traffic crawl leisure equal labor raccoon naked dark ketchup play'
#"money money money money money money money money money money money money"
#"abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
#"sometimes sometimes sometimes sometimes sometimes sometimes sometimes sometimes sometimes sometimes sometimes sometimes"
