# Ohtun miniprojekti

![GitHub Actions](https://github.com/Kove71/Ohtu_miniprojekti/workflows/CI/badge.svg)

## Käyttöohjeet


Ennen ensimmäistä käyttökertaa riippuvuudet tulee asentaa komennolla: 
```bash
poetry install
```
Ohjelma suoritetaan komennolla:
```bash
poetry run invoke start
```
Testaus suoritetaan komennolla:
```bash
poetry run invoke test
```
Pylint suoritetaan komennolla:
```bash
poetry run invoke lint
```
Coverage-report luodaan komennolla:
```bash
poetry run invoke coverage
```
Tämän jälkeen juurihakemistosta löytyy hakemisto htmlcov/, josta voi katsoa raportin.


## Dokumentaatio

- [Backlog](https://docs.google.com/spreadsheets/d/1Av-S8CRkLMrIsAKHgrrVVXugRZbDxyBik0xdSajMxEg)
