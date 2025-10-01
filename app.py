import os
import subprocess

psw = os.getenv("API_PASSWORD", "changeme")
port = int(os.getenv("PORT", 10000))  # Render usa portas dinâmicas

cmd = [
    "mediaflow-proxy",        # binário instalado pelo pip
    "--host", "0.0.0.0",
    "--port", str(port),
    "--password", psw
]

print(f"✅ MediaFlow Proxy a iniciar na porta {port} com senha {psw}")
subprocess.run(cmd)
