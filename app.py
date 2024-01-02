import argparse
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from utils import BaseResponse


def create_app():
    _app = FastAPI(
        title="Tool Server",
        version="v1.0.0"
    )
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    mount_app_routes(_app)
    return _app


def mount_app_routes(_app: FastAPI):
    from api import get_medication_history
    # Tag: register apis
    _app.get("/api/get_medication_history/{patientId}",
             tags=["获取患者药品记录"],
             response_model=BaseResponse,
             summary="获取患者药品记录",
             )(get_medication_history)


def run_api(host, port, **kwargs):
    uvicorn.run(app, host=host, port=port)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=7861)
    args = parser.parse_args()
    app = create_app()
    run_api(
        host=args.host,
        port=args.port
    )
