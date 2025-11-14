# AI Prompt Repository

## Doel van de repository
Deze repository is bedoeld om AI-prompts te bewaren, beheren en op te schalen voor diverse workflows. Door een uniforme structuur te hanteren, wordt samenwerken eenvoudiger en kunnen prompts efficiënt worden versiebeheerd.

## Structuuropbouw
De repository is opgedeeld in thematische mappen voor verschillende promptrollen (zoals taak-, systeem- en agent-prompts) en ondersteunende documentatie. Elke map bevat eigen richtlijnen en metadata zodat nieuwe prompts eenvoudig kunnen worden toegevoegd en gevolgd.

## Nieuwe prompts toevoegen
1. Plaats het promptbestand in de juiste map onder `prompts/`.
2. Voeg eventuele aanvullende documentatie toe in de relevante map onder `docs/`.
3. Voer het script `register_prompt.py` uit met de juiste invoerparameters om de prompt te registreren in `index.json`.
4. Controleer de wijzigingen met Git en voer een commit uit.

## Metadata-aanpak
Alle prompts worden geregistreerd in `index.json`. Elke registratie bevat minimaal een unieke `id`, een `name`, een `type`, een `version`, een `description` en een lijst `tags`. Het script `register_prompt.py` vult automatisch de velden `created` en `updated`. Hierdoor ontstaat een centraal overzicht dat eenvoudig door tooling kan worden gebruikt.

## Mappenoverzicht
- `prompts/task` – prompts die taken beschrijven die moeten worden uitgevoerd.
- `prompts/system` – systeem- of contextprompts die algemene richtlijnen bieden.
- `prompts/master` – overkoepelende prompts die andere prompts orkestreren.
- `prompts/validators` – prompts voor validatiemechanismen of kwaliteitscontroles.
- `prompts/finalizers` – prompts die eindoutput verfijnen of afronden.
- `prompts/agents` – agent-specifieke prompts voor verschillende rollen of persoonlijkheden.
- `prompts/pipelines` – prompts die workflows of pijplijnen definiëren.
- `docs/manuals` – handleidingen en gebruikersinstructies.
- `docs/standards` – standaardisatie- en richtlijnbestanden.
- `docs/changelogs` – changelogbestanden voor het bijhouden van wijzigingen.

