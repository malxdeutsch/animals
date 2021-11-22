from django.shortcuts import render
import json

# Create your views here.

def animal (request, animal_id):
    with open ('data.json') as f:
        data = json.load(f)
    selected_animal = None
    for animal in data['animals']:
        if animal['id'] == animal_id:
            selected_animal = animal
    return render(request, 'animal.html', {'animal':selected_animal})

def family (request, family_id):
    with open ('data.json') as f:
        data = json.load(f)
    selected_family = None
    for family in data['families']:
        if family['id'] == family_id:
            selected_family = family_id
        selected_animal = []
        for animal in data['animals']:
            if animal['family'] == family_id:
                selected_animal.append(animal['name'])
    return render(request, 'family.html', {'family':selected_family,'animal':selected_animal })
  