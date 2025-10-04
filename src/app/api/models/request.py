import pydantic as pd

import typing as tp

from app.api.models.page import *


class CreatePageRequest(pd.BaseModel):
	title: str = pd.Field(..., min_length=1, max_length=256, description='title')
	content: str = pd.Field(..., min_length=1, max_length=1024, description='content')

	author_name: str = pd.Field(..., min_length=1, max_length=64, description='author name')
	author_url: str = pd.Field(..., min_length=1, max_length=256, description='author url')


class EditPageRequest(pd.BaseModel):
	access_token: str = pd.Field(..., description='access token')

	title: tp.Optional[str] = pd.Field(..., min_length=1, max_length=256, description='title')
	content: tp.Optional[str] = pd.Field(..., min_length=1, max_length=1024, description='content')

	author_name: tp.Optional[str] = pd.Field(..., min_length=1, max_length=64, description='author name')
	author_url: tp.Optional[str] = pd.Field(..., min_length=1, max_length=256, description='author url')


class DeletePageRequest(pd.BaseModel):
	access_token: str = pd.Field(..., description='access token')


class GetPageRequest(pd.BaseModel):
	page_url: str = pd.Field(..., description='page url')


class GetPagesRequest(pd.BaseModel):
	pages: tp.List[Page] = pd.Field(..., description='pages')

