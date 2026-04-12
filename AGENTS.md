## Setup

Install Python dependencies:

```bash
uv sync --group dev
```

Install JavaScript dependencies:

```bash
npm install
```

## Checks

Run Python lint:

```bash
uv run ruff check .
```

Run Django template lint:

```bash
uv run djlint semantic_forms demo --check
```

Run JavaScript lint and formatting checks:

```bash
npm run check:js
```

Run Django upgrade compatibility checks against the minimum supported Django version:

```bash
git ls-files '*.py' | xargs uv run django-upgrade --target-version 4.2 --check
```

Run the package test suite:

```bash
SECRET_KEY=test-secret uv run python demo/manage.py test semantic_forms.tests
```

Build the package:

```bash
uv build
```
