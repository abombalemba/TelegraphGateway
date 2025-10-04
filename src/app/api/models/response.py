import pydantic as pd

from app.api.models.page import *


class BaseResponse(pd.BaseModel):
	success: bool = pd.Field(..., description='is ok?')
	message: str = pd.Field(..., description='message')


class CreatePageResponse(BaseResponse):
	page: Page = pd.Field(..., description='created page')
	access_token: str = pd.Field(..., description='access token')


class EditPageResponse(BaseResponse):
	page: Page = pd.Field(..., description='edited page')


class DeletePageResponse(BaseResponse):
	deleted_url: str = pd.Field(..., description='deleted page')


class GetPageResponse(BaseModel):
	page: Page = pd.Field(..., description='page')


class GetPagesResponse(BaseModel):
	pages: tp.List[Page] = pd.Field(..., description='pages')

