import subprocess
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build the Docker image
subprocess.run(["docker", "build", "-t", "aiapp", "."])
