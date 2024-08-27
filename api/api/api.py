from fastapi import FastAPI, status
from fastapi.responses import Response

api = FastAPI()


@api.get("/livez")
async def _livez() -> Response:
    return Response(status_code=status.HTTP_202_ACCEPTED)
