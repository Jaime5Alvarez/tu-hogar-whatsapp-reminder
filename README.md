
#INSTALL

```bash
uv sync
```
## Create .env file and add your credentials

```bash
cp .env.example .env
```

##RUN LAMBDA FUNCTION

```bash
uv run lambda_function.py
```

##CREATE LAMBDA PACKAGE

```bash
source scripts/create_lambda_package.sh
```

##RUN TESTS

```bash
python -m pytest
```