from fastapi import FastAPI, HTTPException, Depends
from models import  Base
from database import engine,get_db
from sqlalchemy.orm import Session, configure_mappers, registry
from sqlalchemy import text
from routers import orders
from config import settings

api = FastAPI(
            # swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}},
            # root_path_in_servers="/app",
            # version="3.0.0",
            # docs_url="/app/docs",  # Example with a root path
            # openapi_url="/app/openapi.json", # Example with a root path

              )
Base.metadata.create_all(engine)
configure_mappers()
# registry.configure()

api.include_router(orders.router)

@api.get("/health")
def health(db: Session = Depends(get_db)):
    try:

        db.execute(text("SELECT 1"))
        db_status = "ok"

    except Exception as e:
        db_status = "error"

    if db_status == "ok":
        return {"status": "ok", "database": db_status, "message": "API is healthy"}
    else:
        raise HTTPException(status_code=503, detail={"status": "error", "database": db_status, "message": "API is unhealthy due to dependency issues"})

if __name__=="__main__":
    import  uvicorn
    uvicorn.run(api, host="127.0.0.1", port=8080) # , 
