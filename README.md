# Dual Discriminator Hybrid Quantum Generative Adversarial Networks (DDHQ-GAN)

## Introduction

This project explores the implementation and research of Dual Discriminator Hybrid Quantum Generative Adversarial Networks (DDHQ-GAN). DDHQ-GAN is an innovative approach that combines the power of quantum computing with the generative capabilities of GANs to create quantum-enhanced generative models. This repository contains the code and resources needed to understand, implement, and experiment with DDHQ-GANs.

## Features

- Hybrid quantum-classical GAN architecture
- Configurable models via config.yml
- Training and evaluation scripts
- Example notebooks for interactive exploration
- Modular codebase to swap generator/discriminator implementations

## Project structure

```
DDHQ-GAN/
├── README.md
├── config.yml                # Default configuration file
├── requirements.txt          # Python dependencies (if present)
├── data/                     # root-level dataset files and manifests
│   └── MNIST/raw/            # raw datasets (will available after run dataloader.py)
├── notebooks/                # root-level notebooks for quick tests and experiments
│   ├── models/               # notebook-backed models and experiments
│   │   └── example_model.ipynb
│   ├── utils/                # helper notebooks (data inspect, viz)
│   │   └── data_inspect.ipynb
│   ├── tests/                # tests moved under notebooks during refactor
│   │   └── test_trainer.py
│   └── ...
├── src/
│   ├── main.py               # CLI entrypoint (run training/eval)
│   ├── main.ipynb            # paired notebook kept with src code (deprecated)
│   ├── features/             # feature extraction, loaders and experiment utilities
│   │   ├── featurize.py
│   │   ├── loader.py         # dataset loaders and helpers
│   │   ├── wandb_utils.py    # Weights & Biases helpers / experiment logging
│   │   └── ...
│   ├── models/               # Generator, discriminator, quantum layers
│   │   ├── __init__.py
│   │   ├── generator.py      # example generator implementation
│   │   ├── discriminator.py  # example discriminator implementation
│   │   ├── initializer/      # helpers to build quantum circuits and parameter initializers
│   │   │   ├── __init__.py
│   │   │   └── quantum_initializer.py
│   │   └── ...
│   └── visualization/        # plotting and sample visualization
│       ├── viz.py
│       └── ...
├── docs/                     # documentation (may not exist in repo)
│   └── REFERENCES.md         # curated references and reading list
└── LICENSE
```

Note: `src/models/initializer/` contains helpers and builders used to construct quantum circuits, parameter initialization strategies, and utilities for mapping classical parameters into quantum circuit gates. You can add builders for new circuit templates in this folder.

## Prerequisites

To ensure a smooth setup process, it is highly recommended to use Conda or Miniconda for managing dependencies and creating a virtual environment. Conda helps to avoid potential conflicts between package dependencies and makes it easier to manage different environments.

### Install Conda/Miniconda

If you don't have Conda or Miniconda installed, you can download and install Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html).

## Installation

Follow the steps below to set up the environment and install the necessary packages.

1. Create Conda environment

```bash
conda create --name ddhqgan python=3.12.4
```

2. Activate environment

```bash
conda activate ddhqgan
```

3. Install the package and dependencies

```bash
pip install .
# or, if a requirements file exists
pip install -r requirements.txt
```

## Configuration

Edit `config.yml` to configure model hyperparameters, dataset paths, training schedule, logging and checkpointing. Common settings:

- model: generator / discriminator architecture choices
- training: batch_size, lr, epochs, optimizer
- data: dataset path, transforms, preprocessing
- logging: checkpoint interval, tensorboard folder

## Usage

Option 1: Run the training or evaluation script

```bash
python src/main.py
```

Option 2: Interactive exploration (deprecated)

```bash
# quick tests: top-level notebooks
jupyter notebook notebooks/scratch.ipynb

# or the paired src notebook (kept for reference, may be out of date)
jupyter notebook src/main.ipynb
```

Note: The notebook in `src/` is deprecated and may not be fully functional. For reliable, reproducible workflows prefer using the CLI (`python src/main.py`) or scripts in `src/examples/` which are kept runnable.

## Examples

- src/notebooks/main.ipynb — walkthrough of training and sampling
- src/examples/ (if present) — quick scripts demonstrating common tasks

## Training & Evaluation

- Launch training or evaluation using `python src/main.py` or the example scripts under `src/examples/`.
- Use `src/features/loader.py` (and related helpers in `src/features/`) to prepare datasets and data loaders.
- Checkpoints and logging hooks are managed by utilities in `src/features/` or `src/examples/` (e.g., wandb_utils).

## Testing

Run unit and integration tests (if provided):

```bash
pytest notebooks/tests/
```

## Troubleshooting

- Missing dependencies: ensure environment is activated and dependencies installed
- CUDA/quantum backend issues: check installed versions and backend configuration in `config.yml`
- Training diverging: try lowering learning rate, reducing batch size, or using gradient clipping

## Citation

If you use this code in research, please cite the repository and any included papers or references that accompany the project.

## Contributing

Contributions are welcome. Please open an issue to discuss major changes, and submit pull requests for fixes and improvements. Add unit tests for any new features.

## License

See the LICENSE file in the project root for licensing details (add one if not present).

## Contact

For questions, open an issue or contact the repository owner.
