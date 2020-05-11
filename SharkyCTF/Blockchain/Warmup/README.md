We need to drain the contract of its funds by calling the withdraw() function. To call that function we need to meet require()'s conditions, which we do by calling unlock(). To meet that requirement we send a request to execute that contract's method with a value of .0005 ether, if we do then the contract unlocks. We send it with myetherwallet and the ropsten testnet and we can get the flag. 

shkCTF{th4t_w4s_4n_1ns4n3_w4rmup_65c8522c0f36ed2566afa7}
