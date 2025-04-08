# Contributing

Thank you for considering to contribute to `flocky`! Here we provide some general guidelines to streamline the contribution process. The goal of this library is to make it easier to submit models to the [Flock.io](https://www.flock.io) platform and to provide easy access to the [Flock.io API](https://fed-ledger-prod.flock.io/docs). This library is built on [nbdev](https://nbdev.fast.ai/) and therefore requires some familiarity with this library. It also heavily leverages other tools from [Answer.AI](https://github.com/AnswerDotAI), like [fastcore](https://github.com/AnswerDotAI/fastcore).

## Before you start

1. Fork [flocky](https://github.com/CarloLepelaars/flocky) from Github.

2. install `flocky` in editable mode:

```bash
pip install -e .
```

3. Develop within the notebooks in the `nbs` folder.

4. When pushing code, make sure to run `nbdev_prepare` first. This runs tests and cleans notebooks.

## How you can contribute

We always welcome contributions to `flocky`. There are several aspects to this repository:

1. **API:** The Flock API reference can be found [here](https://fed-ledger-prod.flock.io/docs).

2. **Training:** We welcome contributions related to training of models for Flock. This can be related to LLM fine-tuning and uploading to the [HuggingFace Hub](https://hf.co).

## PR submission guidelines

- Keep each PR focused. While it's more convenient, do not combine several unrelated contributions together. It can be a good idea to split contributions into multiple PRs.
- Do not turn an already submitted PR into your development playground. If after you submitted a pull request you discovered that more work is needed - close the PR, do the required work and then submit a new PR. Otherwise each of your commits requires attention from maintainers of the project.
- Make sure to add tests for new features.