import logging
import uvicorn
from api.core import settings
from api.app import app


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT, reload=True)