from fastapi import APIRouter, status
from helpers import response
# from fastapi.encoders import jsonable_encoder
# from config.DB.DBConfig import get_db
# from sqlalchemy.orm import Session
# from mappers.itemMapper import dbtodtolist
# from models.testTableModel import Post

from fastapi.responses import StreamingResponse
from jinja2 import Environment, FileSystemLoader
# from weasyprint import HTML
from xhtml2pdf import pisa
import io

router = APIRouter(prefix="/test", tags=["Test"])

# Setup Jinja2 environment
templates = Environment(loader=FileSystemLoader("templates"))

# @router.get("/", response_model=response.APIResponse)
# def get_data(db: Session = Depends(get_db)):

#     db_items = jsonable_encoder(db.query(Post).all())
#     # print(db_items)

#     items = jsonable_encoder(dbtodtolist(db_items))
#     # print(items)

#     data = {"Id": 1, "Details": "Test Details from test controller","DB_Item":items}

#     result = {
#         "status_code": status.HTTP_200_OK,
#         "message": "Test Response",
#         "data": data,
#     }
#     return result


@router.get("/test2")
def get_data_test2():
    data = {"Id": 1, "Details": "Test2 Details from test controller"}

    result = response.APIResponse(
        status_code=status.HTTP_200_OK, message="Test Response", data=data
    )
    return result


@router.get("/pdf_download")
def generate_invoice():
    # Example dynamic data
    data = {
        "invoice_number": "INV-001",
        "items": [
            {"name": "Laptop", "qty": 1, "price": 800},
            {"name": "Mouse", "qty": 2, "price": 25},
            {"name": "Keyboard", "qty": 1, "price": 50},
        ],
    }
    data["total"] = sum(item["qty"] * item["price"] for item in data["items"])

    # Render HTML
    template = templates.get_template("invoice.html")
    html_content = template.render(**data)

    pdf = convert_html_to_pdf(html_content)

    return StreamingResponse(
        io.BytesIO(pdf),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=invoice.pdf"},
    )


def convert_html_to_pdf(source_html: str) -> bytes:
    output = io.BytesIO()
    pisa_status = pisa.CreatePDF(io.StringIO(source_html), dest=output)
    if pisa_status.err:
        return None
    return output.getvalue()