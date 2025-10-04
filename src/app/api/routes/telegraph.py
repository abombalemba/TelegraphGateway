from fastapi import APIRouter

import datetime as dt
import typing as tp

from app.api.models.page import *
from app.api.models.request import *
from app.api.models.response import *

router = APIRouter(prefix='/telegraph')

temp_pages_db = {}
access_tokens_db = {}


def generate_page_url() -> str:
	pass


def generate_access_token() -> str:
	pass


router.get(path='/page/{page_url:path}')
def get_page(page_url: str):
	pass


router.get('/pages')
def get_pages(request: list[Pages]) -> PageResponse:
	pass


router.post(
	path='/page',
	response_model=CreatePageResponse
)
def create_page(request: CreatePageRequest):
	try:
		generated_url = generate_page_url()
		generated_access_token = generate_access_token()

		page = Page(
			url=generated_url
			title=request.title,
			description=request.content,
			views=0,
			author_name=request.author_name,
			author_url=request.author_url,
			created_at=dt.datetime.now()
			updated_at=dt.datetime.now()
		)

		temp_pages_db[page_url] = {
			**page.dict(),
			'content': request.content,
			'access_token': generated_access_token
		}

		access_tokens_db[generated_access_token] = page_url

		return CreatePageResponse(
			success=True,
			message='ok',
			page=page,
			access_token=generated_access_token
		)

	except Exception as ex:
		return CreatePageResponse(
			success=False,
			message=f'{ex}',
			page=Page(url='', title='', description='', views=0, created_at=dt.datetime.now(), updated_at=dt.datetime.now()),
			access_token=''
		)


router.put('/page')
def edit_page(request: EditPageRequest) -> PageResponse:
	pass


@router.delete('/page')
def delete_page(request: DeletePageRequest) -> PageResponse:
	pass

