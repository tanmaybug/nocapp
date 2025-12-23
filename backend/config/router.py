from fastapi import APIRouter

from controllers.V1 import (
    otp_controller,
    registration_controller,
    login_controller,
    noc_application_controller,
    test_new,
    file_upload_controller,
    test_controller,
    view_file_controller
)

from controllers.V1.institution import (
    form1Controller,
    form2Controller,
    form3Controller,
    inspectionController,
    institutionDashboardController,
    trackApplicationController,
    docketNumberController,
    view_download_application_controller,
)

from controllers.V1.department import (
    departmentDashboardController,
    pendingApplicationController,
    inprocessApplicationController,
    nocCompleteApplicationController,
    viewApplicationController,
    departmentInspectionController,
)

master_router = APIRouter()

master_router.include_router(noc_application_controller.router, prefix="/v1")
master_router.include_router(test_new.router, prefix="/v1")
master_router.include_router(test_controller.router, prefix="/v1")
master_router.include_router(file_upload_controller.router, prefix="/v1")

master_router.include_router(registration_controller.router, prefix="/v1")
master_router.include_router(otp_controller.router, prefix="/v1")

master_router.include_router(login_controller.router, prefix="/v1")
master_router.include_router(view_file_controller.router, prefix="/v1")

# ----------Institution Section Start-------------------

master_router.include_router(institutionDashboardController.router, prefix="/v1")
master_router.include_router(trackApplicationController.router, prefix="/v1")
# master_router.include_router(nocDocumentController.router, prefix="/v1")
master_router.include_router(inspectionController.router, prefix="/v1")
master_router.include_router(form1Controller.router, prefix="/v1")
master_router.include_router(form2Controller.router, prefix="/v1")
master_router.include_router(form3Controller.router, prefix="/v1")
master_router.include_router(view_download_application_controller.router, prefix="/v1")
master_router.include_router(docketNumberController.router, prefix="/v1")

# ----------Institution Section End---------------------

# ----------Department Section Start-------------------

master_router.include_router(departmentDashboardController.router, prefix="/v1")
master_router.include_router(pendingApplicationController.router, prefix="/v1")
master_router.include_router(inprocessApplicationController.router, prefix="/v1")
master_router.include_router(nocCompleteApplicationController.router, prefix="/v1")
master_router.include_router(viewApplicationController.router, prefix="/v1")
master_router.include_router(departmentInspectionController.router, prefix="/v1")

# ----------Department Section End---------------------