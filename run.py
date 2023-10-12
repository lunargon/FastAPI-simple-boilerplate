import uvicorn
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
  # reload = True for develop mode -> remove it when release
  uvicorn.run("app.main:app", reload=True)