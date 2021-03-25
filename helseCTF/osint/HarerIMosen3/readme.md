# Letts goo

```
$ steghide info first 
"first":
  format: jpeg
  capacity: 111.7 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "ThisLooksSuspicios.key":
    size: 1.7 KB
    encrypted: rijndael-128, cbc
    compressed: yes

john@john-bond:~/Documents/helseCTF/osint/HarerIMosen3$ file ThisLooksSuspicios.key 
ThisLooksSuspicios.key: ASCII text
john@john-bond:~/Documents/helseCTF/osint/HarerIMosen3$ head ThisLooksSuspicios.key 
-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCw29tWB+lxoO/p
AkuZsPr+70O04q79IKRiZrGPLrNzl4gCwrJ0sgaDGw3Iq2x9Lva24tuLrEsI27c6
6yVnQqey0dpPl4gtyqGsv2AVORUQHGtcvDqyp1UYA99W8Y/QDah7iLqRBjQW6Q5Q
/J98/pei/ki4ABsOuKTY81xclA3+65U5GHsN+jRIlUGqyqGTObX91lgwrgoT1yTr
sdJnYLi+f8mfNuDKQUEFffo7ZEo3gA68y0UgeyvnnQ517YmSu5E6gvEJtbMs+lnF
XnHyZ4MuWiMhTjuiq2pB94rxzk4WBci95KQHxKYlY/NEEtcZBx9futPdUUOkDjo5
BJB8taLbAgMBAAECggEBAKPOPkxkb5dK1GogMh1bil3tBezXt/PC8/4f130iaBs7
0kGcSuVCrj1oJVAjVgxsHx4s5+Np5OWDeyYa/T2ywtgg/e6SDxM6hpwVdMyzXgra
B6aQwF0QFwRzMby5Z9XvkIk6jnIcKMq/eP8RvDZtJ81Tb87cajMsWaKHZJhqmLvt


```

### Tshark time!!

```
$ tshark -o "ssl.keys_list: 172.18.0.3,443,http,ThisLooksSuspicios.key" -r mistenksom_trafikk.pcap -w decrypt.pcap

```

filter http

```

POST /bloggpost/ HTTP/1.1
Host: srv-dmz12.ctf
User-Agent: curl/7.61.1
Accept: */*
Content-Length: 712
Content-Type: multipart/form-data; boundary=------------------------dfa83fc40bbceed3

--------------------------dfa83fc40bbceed3
Content-Disposition: form-data; name="text"; filename="blogginnlegg.txt"
Content-Type: text/plain

Heia bloggen! Jeg var en tur p.. kontoret i dag og tok noen bilder, se den flotte utsikten! Man kan se flere av de kjente byggene i Trondheim slik som Nidarosdomen og Gr..kallen radarhode. Vi har til og med utsikt til Moholt studentby, hvor jeg bodde da jeg var student. Good times. I dag serverte de hjortegryte i kantina, nam nam! Vi f..r jo n..rmest restaurantmat her p.. jobben. Men det var alt for denne gang. Husk .. f..lge EGG{H4R3BL0GG3N} for .. f.. med deg fremtidige blogginnlegg fra meg! Harald Harepus out!
--------------------------dfa83fc40bbceed3--

```
