Decompile the Binary and we see this code for the main method
```
undefined8 main(void)

{
  int iVar1;
  char local_118 [256];
  char local_18 [16];
  
  printf("Hello everyone, say your name: ");
  gets(local_118);
  iVar1 = strcmp("CyberCastors",local_18);
  if (iVar1 == 0) {
    get_flag();
  }
  puts("You lose!");
  return 0;
}
```

Notice that our input gets put into local_118, BUT the actual strcmp call compares with with local_18, so it's comparing two constants, however we do know that local_118 has a 256 character buffer and that its next to local_18 in memory, so we can overflow local_118 into local_18, so we just use a simple python one liner to feed 256 a's and then the string "CyberCastors" into the function and out pops the flag


`castorsCTF{b0f_4r3_n0t_th4t_h4rd_or_4r3_th3y?}`