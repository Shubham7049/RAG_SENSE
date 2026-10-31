
import json
from pathlib import Path

import pandas as pd

from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader,
    BSHTMLLoader
)

from pptx import Presentation


def load_document(file_path):

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    # PDF
    if extension == ".pdf":
        loader = PyPDFLoader(str(path))
        documents = loader.load()

    # Word
    elif extension == ".docx":
        loader = Docx2txtLoader(str(path))
        documents = loader.load()

    # Text and Markdown
    elif extension in [".txt", ".md"]:
        loader = TextLoader(str(path), encoding="utf-8")
        documents = loader.load()

    # CSV
    elif extension == ".csv":
        loader = CSVLoader(
            file_path=str(path),
            encoding="utf-8"
        )
        documents = loader.load()

    # Excel
    elif extension == ".xlsx":
        documents = []

        excel_file = pd.ExcelFile(path)

        for sheet_name in excel_file.sheet_names:

            df = pd.read_excel(
                excel_file,
                sheet_name=sheet_name
            )

            content = df.to_string(index=False)

            documents.append(
                Document(
                    page_content=content,
                    metadata={
                        "source": path.name,
                        "sheet_name": sheet_name,
                        "file_type": "xlsx"
                    }
                )
            )

    # PowerPoint
    elif extension == ".pptx":
        presentation = Presentation(str(path))
        documents = []

        for slide_number, slide in enumerate(
            presentation.slides, start=1
        ):

            slide_text = []

            for shape in slide.shapes:
                if shape.has_text_frame:
                    slide_text.append(shape.text)

                if shape.has_table:
                    for row in shape.table.rows:
                        slide_text.append(
                            " | ".join(
                                cell.text for cell in row.cells
                            )
                        )

            documents.append(
                Document(
                    page_content="\n".join(slide_text),
                    metadata={
                        "source": path.name,
                        "slide": slide_number,
                        "file_type": "pptx"
                    }
                )
            )

    # JSON
    elif extension == ".json":
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        documents = [
            Document(
                page_content=json.dumps(
                    data,
                    ensure_ascii=False,
                    indent=2
                ),
                metadata={
                    "source": path.name,
                    "file_type": "json"
                }
            )
        ]

    # HTML
    elif extension in [".html", ".htm"]:
        loader = BSHTMLLoader(
            str(path),
            open_encoding="utf-8"
        )
        documents = loader.load()

    else:
        raise ValueError(
            f"Unsupported file format: {extension}"
        )

    # Add common metadata
    for document in documents:
        document.metadata["file_name"] = path.name
        document.metadata["file_type"] = extension.lstrip(".")

    return documents
