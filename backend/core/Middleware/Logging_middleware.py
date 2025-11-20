# middleware/date_logger.py
import os
import traceback
from datetime import datetime
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class DateWiseLoggerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, log_dir="logs"):
        super().__init__(app)
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    async def dispatch(self, request: Request, call_next):
        start_time = datetime.now()

        try:
            response = await call_next(request)
            status_code = response.status_code
            error_message = ""
        except Exception as e:
            status_code = 500
            error_message = f"Exception: {str(e)}\n{traceback.format_exc()}"
            response = Response("Internal Server Error", status_code=500)

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        # Prepare log entry
        log_entry = (
            f"Time: {start_time.isoformat()}\n"
            f"Method: {request.method}\n"
            f"Path: {request.url.path}\n"
            f"Query Params: {dict(request.query_params)}\n"
            f"Headers: {dict(request.headers)}\n"
            f"Status Code: {status_code}\n"
            f"Duration: {duration:.4f}s\n"
        )

        if error_message:
            log_entry += f"{error_message}\n"

        log_entry += "-" * 100 + "\n"

        # Write to date-wise log file
        log_filename = start_time.strftime("%Y-%m-%d") + ".log"
        log_path = os.path.join(self.log_dir, log_filename)

        with open(log_path, "a", encoding="utf-8") as log_file:
            log_file.write(log_entry)

        return response
