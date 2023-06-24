import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

subprocess.run(
    [
        "docker",
        "run",
        "-e",
        f"PORT=5567",
        "-e",
        f"OPENAI_API_KEY={os.getenv('OPENAI_API_KEY')}",
        "-p",
        "5567:5567",
        "aiapp",
    ]
)
