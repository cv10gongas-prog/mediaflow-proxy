#!/bin/bash

# Pega a senha da variável de ambiente que vamos criar no Railway
PASSWORD=${API_PASSWORD}

# PORT é fornecida automaticamente pelo Railway
PORT=${PORT:-3000}

# Executa o MediaFlow Proxy
mediaflow-proxy --host 0.0.0.0 --port $PORT --password $PASSWORD
