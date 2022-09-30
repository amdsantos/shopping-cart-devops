from fastapi import APIRouter, status
from starlette.responses import JSONResponse

router = APIRouter(tags=['Healthcheck'], prefix='/healthcheck')

@router.get('')
def healthcheck():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "OK"})
