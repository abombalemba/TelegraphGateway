from fastapi import FastAPI
import uvicorn

app = FastAPI(
	title='TelegraphGateway',
	description='microservice for telegraph',
	version='1.0.0'
)


@app.get('/')
def index():
	return {
		'status_code': 200,
		'message': 'ok'
	}


if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=5011)

