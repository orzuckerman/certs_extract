# certs_extract

openssl s_client -connect WEBSITE.com:443 -showcerts > downloadedcerts\n
python main.py downloadedcerts\n
openssl x509 -text -in cert_0 -noout\n
