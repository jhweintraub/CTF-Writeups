Prompt - "Look, it's the flag! Oh wait...it looks like we need to take a closer look... not_so_meta.jpg"

Given it's a forensics challenge and the title says the word "meta" let's run exiftool and see if we can find anything interesting

We immediately find something related to the flag with this line 

"Its The Flag                    : QUNJezVmMzQ1NjRiM2ViNjk3YjE2MzA3OTIxNjFmYX0="

the "=" means base64 so decode it and we get the flag

ACI{5f34564b3eb697b1630792161fa}

