from pathlib import Path

from litestar import Litestar, get
from litestar.config.cors import CORSConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response_containers import Template
from litestar.template.config import TemplateConfig

from src.api.chats import general_chat


@get("/")
def index() -> Template:
    return Template(name="index.html")


app = Litestar(
    route_handlers=[index, general_chat],
    template_config=TemplateConfig(
        directory=Path("html"),
        engine=JinjaTemplateEngine,
    ),
    cors_config=CORSConfig(allow_origins=["*"]),
)
