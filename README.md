# Named Entity Recognition (NER) App

A Flask web app that finds and highlights named entities — people, organizations, places, dates, money, and more — in text you upload or paste, using spaCy's pretrained English model.

## How it works (in short)

1. You either upload a `.txt` file or paste text directly into the form on the homepage.
2. Flask (`app.py`) reads that text and runs it through spaCy's `en_core_web_sm` NLP pipeline.
3. spaCy tags each recognized entity (e.g. `PERSON`, `ORG`, `GPE`, `DATE`) in the text.
4. displaCy renders those tags as color-coded highlights, which get sent back to the page along with a quick summary (total entities found, word count, entity density) and a clickable legend to filter by entity type.

## Setup

### 1. Get the project

Clone or download this repository, then move into the project folder.

### 2. Create a virtual environment

On Windows:

```
python -m venv venv
```

Activate it:

```
venv\Scripts\activate
```

You should now see something like:

```
(venv) C:\...\Name-Entity-Recognition-App-Natural-Language-Processing-main>
```

> On macOS/Linux, create it the same way (`python3 -m venv venv`) and activate with `source venv/bin/activate` instead.

### 3. Install the dependencies

Run:

```
pip install flask spacy
```

Then install the English spaCy model:

```
python -m spacy download en_core_web_sm
```

### ⚠️ One thing in this project needs fixing

Your `app.py` has:

```
return render_template('index.html')
```

But `index.html` is currently in the same folder as `app.py`, whereas Flask expects HTML files inside a `templates` folder.

So make the structure:

```
Name-Entity-Recognition-App-Natural-Language-Processing-main/
│
├── app.py
├── README.md
│
└── templates/
    └── index.html
```

Basically: create a folder called `templates` → move `index.html` into it.

### 4. Run it

With the virtual environment still activated:

```
python app.py
```

You should get something like:

```
* Running on http://127.0.0.1:5000
```

Open this in your browser:

```
http://127.0.0.1:5000
```

## Usage

1. On the homepage, either drag a `.txt` file into the upload zone (or click to browse) — or paste text straight into the text box. A few one-click examples are provided if you just want to try it out.
2. Click **Analyze text**.
3. The page reloads showing the tagged text, an entity summary (counts, word count, density), and a legend you can click to filter which entity types are highlighted.
4. Click **Show original text** to compare against the untagged version.
