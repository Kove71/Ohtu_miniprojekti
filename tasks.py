from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src; coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def robot(ctx):
    ctx.run("robot src/tests")

@task
def build(ctx):
    ctx.run("python3 src/repositories/db_build.py")

@task
def clear(ctx):
    ctx.run("python3 src/repositories/db_clear.py")