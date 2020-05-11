pragma solidity = 0.4.25;

contract Guessing {
    address public owner;    
    bytes32 private passphrase;
    
    constructor(bytes32 _passphrase) public payable {
        owner = msg.sender;
        passphrase = keccak256(abi.encodePacked(_passphrase));
    }
    
    function withdraw() public {
        require(msg.sender == owner);
        msg.sender.call.value(address(this).balance)();
    }

    function claim(bytes32 _secret) public payable {
        require(keccak256(abi.encodePacked(_secret)) == passphrase);
        owner = msg.sender; 
    }
}