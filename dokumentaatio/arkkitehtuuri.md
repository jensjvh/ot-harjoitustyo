# Arkkitehtuurikuvaus

## Pakkausrakenne

```mermaid
  graph LR
    UI --> Services
    Services --> Repositories
    Repositories --> Entities
    Services --> Entities
```

Sovelluksen rakenteessa on kerrokset `UI`, `Services`, `Repositories` ja `Entities`. `UI` kerros kommunikoi `Services` kerroksen kanssa, `Services` `Repositories` ja `Entities` kanssa, sekä `Repositories` `Entities` kanssa.

## Tietojen tallennus

Luokat `BudgetRepository` ja `UserRepository` ovat vastuussa sovelluksen tietojen tallentamisesta. Molemmat käyttävät SQLite-tietokantaa, jonka tablet alustetaan tiedostossa `initialize_database.py`. Tiedostot sijaitsevat juurihakemiston `data` hakemistossa, ja tiedostojen nimet on määritelty `.env`-tiedostossa.

## Sovelluslogiikka

```mermaid
  classDiagram
    UI  ..> BudgetService
    BudgetService ..> UserRepository
    BudgetService ..> BudgetRepository
    BudgetService "1" -- "*" User
    User "1" -- "*" Budget
    UserRepository ..> User
    BudgetRepository ..> Budget
    UI ..> UserService
    UserService ..> UserRepository
    UserService "1" -- "*" User
```

## Käynnistys ja kirjautuminen

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant UserService
    participant UserRepository
    UI->>UI: _show_login_view()
    User->>UI: Login with username and password
    UI->>UserService: login(username, password)
    UserService->>UserRepository: find_user(username)
    UserRepository->>UserService: user
    UserService->>UI: user
    UI->>UI: _show_budget_main_view()
```

Käynnistyksen yhteydessä UI kutsuu _show_login_view()-metodia, jolla näytetään kirjautumisnäkymä käyttäjälle. Käyttäjän painamalla kirjautumispainiketta, kutsuu UI `UserService` palvelun login()-metodia käyttäjätunnuksella ja salasanalla. `UserService` kutsuu `UserRepository` luokan find_user()metodia parametrina käyttäjänimi, joka palauttaa `User` olion, jos käyttäjä löytyy. `UserService` palauttaa tämän `User` olion, ja UI ohjaa käyttäjän sovelluksen päänäkymään metodilla _show_budget_main_view().

## Rekisteröityminen

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant UserService
    participant UserRepository
    participant new_user
    UI->>UI: _show_login_view()
    User->>UI: Click "Create account" button
    UI->>UI: _show_register_view()
    User->>UI: Register with username and password
    UI->>UserService: create_user(username, password)
    UserService->>UserRepository: find_user(username)
    UserRepository->>UserService: None
    UserService->>new_user: User(username, password)
    UserService->>UserRepository: create(new_user)
    UserRepository->>UserService: user
    UserService->>UI: user
    UI->>UI: _show_budget_main_view()
```

UI kutsuu _show_login_view()-metodia, joka näyttää käyttäjälle kirjautumisnäkymän. Käyttäjä painaa "Create account" -painiketta, jolloin UI kutsuu _show_register_view()-metodia, joka näyttää rekisteröitymisnäkymän. UI kutsuu `UserService`-palvelun create_user()-metodia, jossa käyttäjätunnus ja salasana annetaan parametreina. `UserService` kutsuu `UserRepository`-luokan find_user()-metodia tarkistaakseen, onko käyttäjätunnus jo olemassa. `UserRepository` ei löydä käyttäjää, joten se palauttaa None. `UserService` luo uuden käyttäjän User-olion muodossa, käyttäjätunnuksella ja salasanalla. UserService kutsuu `UserRepository`-luokkaa create()-metodilla luodakseen uuden käyttäjän tietokantaan. `UserRepository` palauttaa luodun käyttäjän UserService-palvelulle. UserService palauttaa käyttäjän UI:lle. UI ohjaa käyttäjän sovelluksen päänäkymään kutsumalla _show_budget_main_view()-metodia.

## Käyttöliittymä

Sovelluksessa on näkymät kirjautumiselle, rekisteröitymiselle, budjettien tarkastelulle, sekä pieni popup näkymä budjettien lisäykselle.
