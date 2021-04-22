**certs_extract** is a tiny script that comes to play after the openssl s_client command. You start from a file with all the certificates that provided by the server, and this script extracts and splits them to seperate files. Then, you can parse and present each certificate.
This script was written for personal use. Enjoy!

# Example

```
# openssl s_client -connect WEBSITE.com:443 -showcerts > downloadedcerts
# python certs_extract.py downloadedcerts
# openssl x509 -text -in cert_0 -noout
```

# Downloading

```
download the main.py file.
```
