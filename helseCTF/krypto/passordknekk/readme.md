# Breaking

Hashcat based on old password, unsing mask and custom masks

```
$ hashcat --force -a 3  -m 2100 --status -o found.txt hash.txt -1 \(\) -2 01 Vinter?d?u?2?l?2?l?1?2
$ hashcat --force -a 3  -m 2100 --status -o found.txt hash.txt -1 \(\) -2 01 Sommer?d?u?2?l?2?l?1?2
```

```
$ cat found.txt 
$DCC2$10240#kylling#9eb4ad793886bb81bb24daf3cf90ba4e:Sommer3Q0g1k(1

```
