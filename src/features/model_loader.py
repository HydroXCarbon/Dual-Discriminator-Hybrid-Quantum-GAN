import torch.optim as optim
import torch.nn as nn
from models import *
from colorama import Fore, Style, init

def get_model(models, model_selector):
  model_list = []
  optimizer_list = []
  model_selector = model_selector.split(',')
  model_selector = tuple(model.strip() for model in model_selector)
  
  # Initialize models dynamically
  print(Fore.GREEN + "Loading model: " + Style.RESET_ALL, end='')
  for model_name in model_selector:
    if model_name not in models:
      continue
    print(model_name, end=' ')
    learning_rate = models[model_name]['learning_rate']
    betas = models[model_name]['betas']
    betas = betas.split(',')
    betas = tuple(float(beta.strip()) for beta in betas)

    # Get the class object dynamically using globals()
    model_class_name = models[model_name]['model_class']
    model_loss_function_name = models[model_name]['loss_function']
    model_optimizer_name = models[model_name]['optimizer']
    model_class = globals()[model_class_name]

    # Set up models dynamically
    model_instance = model_class()
    existing_names = [model.name for model in model_list]
    unique_name = model_name
    count = 1

    while unique_name in existing_names:
      unique_name = f"{model_name}_{count}"
      count += 1

    model_instance.name = unique_name

    # Dynamically retrieve the loss function class from torch.nn
    loss_function_class = getattr(nn, model_loss_function_name)
    model_instance.loss_function = loss_function_class()

    model_list.append(model_instance)

    # Dynamically retrieve the optimizer class from torch.optim
    optimizer_class = getattr(optim, model_optimizer_name)
    optimizer_instance = optimizer_class(model_instance.parameters(), lr=learning_rate, betas=betas)
    optimizer_instance.name = 'optimizer_' + model_name
    
    optimizer_list.append(optimizer_instance)

  print()
  return model_list, optimizer_list