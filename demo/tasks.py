from typing import Any

from invoke import task


@task
def lint(ctx: Any) -> None:
    """Run lint checks."""
    with ctx.cd(".."):
        ctx.run("uv run ruff check .")
        ctx.run("npm run check:js")
        ctx.run("uv run djlint semantic_forms demo --check")
        ctx.run(
            "git ls-files '*.py' | xargs uv run django-upgrade "
            "--target-version 4.2 --check"
        )


@task
def format_code(ctx: Any) -> None:
    """Format JavaScript and Django templates."""
    with ctx.cd(".."):
        ctx.run("npm run fix:js")
        ctx.run("uv run djlint semantic_forms demo --reformat")


@task
def test(ctx: Any) -> None:
    """Run the package test suite."""
    with ctx.cd(".."):
        ctx.run(
            "SECRET_KEY=test-secret uv run python demo/manage.py "
            "test semantic_forms.tests --verbosity 1"
        )


@task
def check(ctx: Any) -> None:
    """Run lint, tests, and a package build."""
    lint(ctx)
    test(ctx)
    with ctx.cd(".."):
        ctx.run("uv build")
