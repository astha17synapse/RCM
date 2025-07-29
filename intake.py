from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/intake/new")
async def new_patient_intake():
    return JSONResponse(content={"message": " New patient intake route working!"})

@router.get("/intake/existing")
async def existing_patient_intake():
    return JSONResponse(content={"message": " Existing patient intake route working!"})

@router.get("/intake/referral")
async def referral_patient_intake():
    return JSONResponse(content={"message": " Referral intake route working!"})
