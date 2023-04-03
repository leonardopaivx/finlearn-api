from fastapi import HTTPException, status


class ErrorModel:
    @classmethod
    def not_found(cls, note: str):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=note)

    @classmethod
    def bad_request(cls, note: str):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=note)

    @classmethod
    def unauthorized(cls, note: str):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=note)
