import os

from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm.settings")

application = get_wsgi_application()

from fastapimain.urls import router as main_router

app = FastAPI(
    title="FastApiMain",
    description="A demo project. Also, an actual fish with a weird name.",
    version="We aren't doing versions yet. Point oh.",
)

app.include_router(main_router, prefix="/api")