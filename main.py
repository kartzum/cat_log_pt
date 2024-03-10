from typing import Annotated

from fastapi import FastAPI, Depends, BackgroundTasks
import uvicorn

from model import app_data, AppData
from operation import run_operation

app = FastAPI()


@app.get("/providers/")
async def providers(application_data: Annotated[AppData, Depends(app_data)]):
    return application_data.providers


@app.get("/catalogs/")
async def catalogs(application_data: Annotated[AppData, Depends(app_data)]):
    return application_data.catalogs


@app.get("/catalog_schemes/")
async def catalog_schemes(application_data: Annotated[AppData, Depends(app_data)]):
    return application_data.catalog_schemes


@app.get("/catalog_scheme_operations/")
async def catalog_scheme_operations(application_data: Annotated[AppData, Depends(app_data)]):
    return application_data.catalog_scheme_operations


@app.get("/catalog_scheme_operation_instances/")
async def catalog_scheme_operation_instances(application_data: Annotated[AppData, Depends(app_data)]):
    return application_data.catalog_scheme_operation_instances


@app.get("/catalog_results/")
async def catalog_results(application_data: Annotated[AppData, Depends(app_data)]):
    return application_data.catalog_results


@app.post("/schedule_catalog_scheme_operation/{operation_id}")
async def schedule_catalog_scheme_operation(
        operation_id: str,
        background_tasks: BackgroundTasks,
        application_data: Annotated[AppData, Depends(app_data)],
):
    scheme_operation = application_data.catalog_scheme_operations[operation_id]
    background_tasks.add_task(run_operation, scheme_operation, application_data)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
