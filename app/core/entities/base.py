import re

from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class Base:
    __name__: str
    __allow_unmapped__ = True

    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        # pylint: disable=no-self-argument
        # Camel case to snake case
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()
