import uvicorn
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env\.env')

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8100, reload=True)
