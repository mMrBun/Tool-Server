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
    from api import get_patient_info
    # Tag: register apis
    _app.post("/api/get_patient_info",
              tags=["获取患者基本信息"],
              response_model=BaseResponse,
              summary="get_patient_info",
              )(get_patient_info)


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
