# app/routers/pessoa.py
from fastapi import HTTPException
from sqlmodel import Session, select
from controller.generic import create_crud_router, Hooks
from model.models import Pessoa, Endereco
from model.dto import PessoaCreate, PessoaUpdate, PessoaRead

router = create_crud_router(
    model=Pessoa,
    create_schema=PessoaCreate,
    update_schema=PessoaUpdate,
    read_schema=PessoaRead,
    prefix="/pessoas",
    tags=["Pessoas"],
)
