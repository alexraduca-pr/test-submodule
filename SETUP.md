# Setup iniziale

**N.B. Sovrascrivere con file specifico per il proprio progetto.**

Procedura di creazione nuovo progetto

## 1. Convenzioni di nomenclatura

| Risorsa           | Formato                    |
| ----------------- | -------------------------- |
| Repository GitHub | `odoo-<clt>-<descrizione>` |
| Progetto Odoo.sh  | `<clt>-<descrizione>`      |

- **clt**: codice identificativo del cliente, come da anagrafica gestionale
- **descrizione**: nome breve e significativo che identifica il progetto

In caso di progetto operativo, utilizzare come descrizione **prod**

| Esempio                             | Repository GitHub     | Progetto Odoo.sh |
| ----------------------------------- | --------------------- | ---------------- |
| Progetto di produzione PRConsulting | `odoo-prc-prod`       | `prc-prod`       |
| Progetto di test stampe Ber-Pa      | `odoo-brp-teststampe` | `brp-teststampe` |

## 2. Creazione repository e progetto

1. Creare una nuova repository clonando questo template secondo le [convenzioni di nomenclatura](#1-convenzioni-di-nomenclatura)
1. Accedere a [odoo.sh](https://www.odoo.sh/)
1. Creare un nuovo progetto secondo le [convenzioni di nomenclatura](#1-convenzioni-di-nomenclatura)
1. Scegliere **Existing repository** e selezionare la repository appena creata
1. Scegliere la versione corretta di Odoo, indicata in [Contesto tecnico](#contesto-tecnico)
1. Inserire il codice di sottoscrizione e premere **Deploy**.

## 3. Ambiente di sviluppo

1. Clonare la repository nel proprio ambiente di sviluppo
1. Eseguire i comandi

   ```sh
   pip install -r requirements.txt
   pre-commit install
   ```

   Il comando di `pre-commit install` installa l'hook `pre-commit` per eseguire i controlli di qualità sui file in stage necessari per il completamento di un commit.

## 4. Moduli esterni

In caso si voglia installare moduli custom sviluppati in altre repository esterne, queste andranno collegate nella repository di progetto come sottomoduli.

### 4.1 Autorizzare accesso

Questo passaggio è necessario solo se il progetto è ospitato su Odoo.sh
e la repository esterna da collegare è privata.

1. Nel progetto Odoo.sh, aprire **Settings → Submodules**.
2. Inserire l’URL SSH della repository da aggiungere:

   ```text
   git@github.com:<organizzazione_proprietaria>/<repository_esterna>.git
   ```

3. Copiare la **chiave pubblica** generata da Odoo.sh
4. Aggiungerla nelle impostazioni della repository esterna, in **Settings → Deploy keys**, garantendo accesso anche solo in lettura.

### 4.2 Aggiungere sottomodulo al progetto

Dalla directory principale del progetto eseguire:

```sh
git submodule add git@github.com:<organizzazione_proprietaria>/<repository_esterna>.git
git commit -m "[ADD] addons: add <descrizione_moduli_esterni> repository"
git push
```

### 4.3 Installare moduli in Odoo

1. Aprire il database dell’ambiente corrispondente.
2. Attivare la modalità sviluppatore e aprire **Apps → Update Apps List**.
3. Cercare i moduli desiderati filtrando per le informazioni nei rispettivi manifest
4. Procedere con l'installazione
