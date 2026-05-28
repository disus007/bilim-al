import traceback
from fastapi import APIRouter, HTTPException
from app.models.schemas import ExplainErrorRequest, ExplainErrorResponse
from app.services.ai_service import ai_service

router = APIRouter(prefix="/explainer", tags=["Explainer"])


@router.post("/explain_error", response_model=ExplainErrorResponse)
def explain_error(request: ExplainErrorRequest):
    try:
        result = ai_service.explain_error(
            code=request.code,
            error=request.error_message,
            level=request.student_level
        )
        return ExplainErrorResponse(
            error_type=result.get("error_type", "Error"),
            explanation=result.get("explanation", ""),
            fix_suggestion=result.get("fix_suggestion", ""),
            example=result.get("example", "")
        )
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))