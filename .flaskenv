FLASK_APP=microblog.py
FLASK_DEBUG=0

# For e-mail support:
# Run an e-mail server on separeted shell
# python -m smtpd -n -c DebuggingServer localhost:8025
# and set:
MAIL_SERVER=localhost
MAIL_PORT=8025


# Optionally set a real e-mail server with:
# MAIL_SERVER=smtp.googlemail.com
# MAIL_PORT=587
# MAIL_USE_TLS=1
# MAIL_USERNAME=<your-gmail-username>
# MAIL_PASSWORD=<your-gmail-password>
