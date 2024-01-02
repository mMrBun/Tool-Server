from typing import List

from fastapi import UploadFile, File, Form, Depends
from sqlalchemy.orm import Session

from db.curd.users import get_users
from db.database import get_db
from utils import BaseResponse


def upload_docs(
        files: List[UploadFile] = File(..., description="上传文件，支持多文件"),
        knowledge_base_name: str = Form(..., description="知识库名称", examples=["samples"]),
        override: bool = Form(False, description="覆盖已有文件"),
        to_vector_store: bool = Form(True, description="上传文件后是否进行向量化"),
        chunk_size: int = Form(500, description="知识库中单段文本最大长度"),
        chunk_overlap: int = Form(50, description="知识库中相邻文本重合长度"),
        zh_title_enhance: bool = Form(True, description="是否开启中文标题加强"),
        not_refresh_vs_cache: bool = Form(False, description="暂不保存向量库（用于FAISS）"),
) -> BaseResponse:
    """
    API接口：上传文件，并/或向量化
    """
    print(
        files,
        knowledge_base_name,
        override,
        to_vector_store,
        chunk_size,
        chunk_overlap,
        zh_title_enhance,
        not_refresh_vs_cache
    )

    return BaseResponse(code=200, msg="文件上传与向量化完成", data={"failed_files": "xxx"})


def db_query(db: Session = Depends(get_db)) -> BaseResponse:
    """
        API接口： 数据库查询
    """
    objs = get_users(db)
    return BaseResponse(code=200, msg="查询数据库成功", data=[{"id": obj.id, "name": obj.name} for obj in objs])
