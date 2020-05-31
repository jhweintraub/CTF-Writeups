This challenge requires knowledge of how ethereum transactions and contracts are created. The constructor() method gets triggered on contract creation. We're trying to figure out the secret passphrase, the catch is that it's hashed with the keccak256 hash algorithm, which is used specifically for ethereum. On first guess you would think you should try to crack the password, but we don't need to do that much. And even if you could, you would still get a weird abi encoding.

However, the hashed passphrase is made from the constructor parameter `_passphrase`, when the contract was created. This means that cause we already have the contract address, we can just go to a blockchain explorer and find the value sent as that parameter. 

ropsten.etherscan.io/contract/[insert contract] and then go to transaction details and scroll down to "input data"

In a transaction, the input data is at the end of the data. We know that it's type bytes_32 so it should be the last 32 bytes of the input data. 

`49276d2070723374747920737572332079307520627275743366307263336421`

Decoded from hex we get the phrase `I'm pr3tty sur3 y0u brut3f0rc3d!`

We plug this into a transaction on claim() and we're able to get the flag

shkCTF{bl0ckch41n_c0uld_b3_h3lpfull_05b12d40c473800270981b} 