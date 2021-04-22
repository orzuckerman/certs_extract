# certs_extract

openssl s_client -connect WEBSITE.com:443 -showcerts > downloadedcerts
python main.py downloadedcerts
openssl x509 -text -in cert_0 -noout
