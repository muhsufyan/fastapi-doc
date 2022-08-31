# A database dependency with yield
# create a database session and close it after finishing.
async def get_db():
    db = DBSession()
    # dg try error dr dependency, ex rollback, akan ditangkap & dpt diketahui melalui except SomeException
    try:
    #  yielded value is what is injected into path operations and other dependencies
        yield db
    # executed after the response has been delivered
    finally:
        db.close()

# Sub-dependencies with yield
# ex dependency_c can have a dependency on dependency_b, and dependency_b on dependency_a
from fastapi import Depends


async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


async def dependency_b(dep_a=Depends(dependency_a)):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


async def dependency_c(dep_b=Depends(dependency_b)):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)
