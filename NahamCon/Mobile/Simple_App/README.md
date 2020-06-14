`Prompt - Here's a simple Android app. Can you get the flag?`

decompile the apk file with `apktool d simple_app.apk` and run recursive grep on it to find the flag

`grep -R "flag{" simple_app/`

`flag{3asY_4ndr0id_r3vers1ng}`