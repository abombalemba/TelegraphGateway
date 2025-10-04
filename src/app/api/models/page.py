import pydantic as pd

import datetime as dt
import typing as tp


class Page(pd.BaseModel):
	url: str = pd.Field(..., description='url')
	title: str = pd.Field(..., description='title')
	description: str = pd.Field(..., description='description')
	views: int = pd.Field(0, description='views')

	author_name: tp.Optional[str] = pd.Field(None, description='author name')
	author_url: tp.Optional[str] = pd.Field(None, description='author url')

	created_at: dt.datetime = pd.Field(None, description='created at')
	updated_at: dt.datetime = pd.Field(None, description='updated at')

