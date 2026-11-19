# Template di progetto Odoo

**N.B. Sovrascrivere con file specifico per il proprio progetto.**

Repository dedicata allo sviluppo di nuovi moduli e customizzazioni Odoo.

## 1. Scopo

Addon custom pensati per estendere Odoo in modo:

- compatibile con Odoo.sh
- aderente alle best practice Odoo 19

## 2. Contesto tecnico

- Piattaforma target: Odoo 19.0
- Runtime: Python 3.12+ e PostgreSQL 16+
- Deployment: Odoo.sh
- Strategia: estensione tramite ereditarieta dei modelli e delle viste

## 4. Struttura Repository

La repository è predisposta con la seguente struttura:

- `.github/workflows/` - Contiene gli script automatici di verifica (non modificare).
- `.pylintrc`, `ruff.toml`, `.pre-commit-config.yaml` - Configurazioni dei controlli di qualita del codice (non modificare).
- `requirements.txt` - Installa automaticamente gli strumenti necessari in background.
- Directory principale - Area di lavoro del progetto. Crea qui i moduli Odoo (ad esempio `__manifest__.py`, `models/`, `views/`) direttamente nella cartella base della repository.


## 5. Clonazione e best practices

Per ogni nuovo progetto, procedere con la clonazione di questo template, come da guida [SETUP.md](./SETUP.md).

### 5.1 Workflow

Per ogni progetto creato da questo template, è consigliato seguire il sequente processo di lavoro:

1. Creare branch dedicato dalla base corretta.
2. Implementare una singola modifica logica per commit.
3. Aggiornare sicurezza, viste e dati coerentemente alla modifica.
4. Aggiungere o aggiornare i test del modulo.
5. Verificare installazione/upgrade del modulo in ambiente Odoo.sh di test.
6. Aprire PR verso il branch di destinazione.

### 5.2 Checklist minima prima di una PR

- Manifest aggiornato e coerente (`__manifest__.py`)
- Dipendenze dichiarate correttamente
- Accessi e regole sicurezza verificati
- Viste valide e senza override fragili
- Test eseguiti con esito positivo
- Nessuna modifica al core Odoo

## 6. Aggiornamenti template

I repository derivati non si aggiornano automaticamente: eseguire questa
procedura quando il template introduce correzioni o configurazioni utili al
progetto, su un branch dedicato prima della PR.

### 6.1 Configurazione iniziale

Aggiungere il repository template come remote, se non è già configurato:

```bash
git remote add template https://github.com/pr-consulting-eu/odoo-project-template.git
```

Verificare i remote configurati:

```bash
git remote -v
```

Output atteso:
- `origin`: repository del progetto.
- `template`: repository da cui recuperare gli aggiornamenti.

### 6.2 Aggiornare il repository

Recuperare gli ultimi aggiornamenti del template:

```bash
git fetch template
```

Integrare gli aggiornamenti nel branch corrente, creando un commit di merge:

```bash
git merge template/main --no-ff
```

Git aprirà l'editor per modificare il messaggio del commit di merge.

In alternativa, specificare direttamente il messaggio:

```bash
git merge template/main --no-ff -m "Aggiornamento dal repository template"
```

Sostituire `main` con il branch del proprio progetto, se necessario.
