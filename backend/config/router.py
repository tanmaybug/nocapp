from fastapi import APIRouter

from controllers.V1 import (
    otp_controller,
    registration_controller,
    login_controller,
    noc_application_controller,
    test_new,
)

from controllers.V1.institution import (
    form1Controller,
    form2Controller,
    form3Controller,
    inspectionController,
    institutionDashboardController,
    trackApplicationController,
    view_download_application_controller,
)

master_router = APIRouter()

master_router.include_router(noc_application_controller.router, prefix="/v1")
master_router.include_router(test_new.router, prefix="/v1")

master_router.include_router(registration_controller.router, prefix="/v1")
master_router.include_router(otp_controller.router, prefix="/v1")

master_router.include_router(login_controller.router, prefix="/v1")

# ----------Institution Section Start-------------------

master_router.include_router(institutionDashboardController.router, prefix="/v1")
master_router.include_router(trackApplicationController.router, prefix="/v1")
# master_router.include_router(nocDocumentController.router, prefix="/v1")
master_router.include_router(inspectionController.router, prefix="/v1")
master_router.include_router(form1Controller.router, prefix="/v1")
master_router.include_router(form2Controller.router, prefix="/v1")
master_router.include_router(form3Controller.router, prefix="/v1")
master_router.include_router(view_download_application_controller.router, prefix="/v1")

# ----------Institution Section End---------------------

# ----------Department Section Start-------------------

# master_router.include_router(dashboardController.router, prefix="/v1")
# master_router.include_router(view_download_application_controller.router, prefix="/v1")

# ----------Department Section End---------------------