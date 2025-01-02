[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/jacobEAdamson/ai-fungeon-api/ci.yml)](https://github.com/jacobEAdamson/ai-fungeon-api/actions/workflows/ci.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/69f5b55f3fca5fc7c1ae/maintainability)](https://codeclimate.com/github/jacobEAdamson/ai-fungeon-api/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/69f5b55f3fca5fc7c1ae/test_coverage)](https://codeclimate.com/github/jacobEAdamson/ai-fungeon-api/test_coverage)

# AI Fungeon

This is a simple project to allow a user to generate a simple story using any OpenAI compatible API. Simply make create an `.env` file using the `sample.env` template as a guide, start the server on your machine, open the [demo page](https://github.com/jacobEAdamson/ai-fungeon-api/blob/master/demo.html) and type your name!

## Installation

```sh
pyenv install
pip install virtualenv
virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Run

```sh
bin/start
```


## License

[MIT licensed](https://github.com/jacobEAdamson/ai-fungeon-api/blob/master/LICENSE).
