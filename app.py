import os
import subprocess

psw = os.getenv("API_PASSWORD", "changeme")
port = int(os.getenv("PORT", 10000))  # Render usa portas entre 10000-19999

cmd = [
    "python3",
    "-m", "mediaflow_proxy",
    "--host", "0.0.0.0",
    "--port", str(port)
]

print(f"✅ MediaFlow Proxy a iniciar na porta {port} com senha {psw}")
subprocess.run(cmd)
