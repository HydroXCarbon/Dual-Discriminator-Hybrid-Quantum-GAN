from setuptools import setup, find_packages

setup(
    name='QuantumGAN',
    version='0.1.0',
    author="Purin Pongpanich",
    author_email="purin.pongpanich@gmail.com",
    url="https://github.com/HydroXCarbon/QuantumGAN",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        # Core ML & scientific
        'torch==2.3.1',
        'torchvision==0.18.1',
        'numpy==1.26.4',
        'matplotlib==3.9.0',

        # Qiskit stack
        'qiskit==1.1.1',
        'qiskit-aer==0.15.1',
        'qiskit-aer-gpu==0.15.1',
        'qiskit-ibm-runtime==0.24.1',
        'qiskit-algorithms==0.3.0',
        'qiskit-machine-learning==0.7.2',

        # Utilities
        'python-dotenv==1.0.1',
        'pylatexenc==2.10',
        'PyYAML==6.0.2',
        'packaging==24.1',
        'tqdm==4.66.5',
        'wandb==0.18.3',
        'colorama==0.4.6',

        # Metrics & helpers
        'torchsummary==1.5.1',
        'torchmetrics==1.4.2',
        'requests==2.32.2',

        # IBM SDKs (only include if required at runtime)
        'ibm-cloud-sdk-core==3.20.1',
        'ibm-platform-services==0.54.1',
    ]
)