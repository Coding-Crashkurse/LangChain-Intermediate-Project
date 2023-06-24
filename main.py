from app.app import app
import uvicorn
import os

port = int(os.getenv("PORT", "5566"))

uvicorn.run(app, host="0.0.0.0", port=port)
