from app import m
from schemes import scheme_echo


@m.user_endpoint(path=["echo"], requires=scheme_echo)
def echo(data: dict, user: str) -> dict:
    return {"message": data["message"], "user": user}


@m.microservice_endpoint(path=["info"])
def info(data: dict, microservice: str) -> dict:
    return {"message": data["message"], "microservice": microservice}


@m.microservice_endpoint(path=["delete_user"])
def delete_user(data: dict, microservice: str) -> dict:
    return {"success": True}
