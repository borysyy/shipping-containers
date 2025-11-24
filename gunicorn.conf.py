# gunicorn.conf.py

# Number of worker processes
workers = 1 * 2 + 1

# Type of worker
worker_class = 'sync'

# Bind the server to a specific address and port
bind = '0.0.0.0:5000'

# Log level
loglevel = 'info'