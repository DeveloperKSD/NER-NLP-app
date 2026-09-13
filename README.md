# Named Entity Recognition (NER) App

## How it works 

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

Use test.txt to test it or use ur own material thank you 67




## UI 

<img width="1919" height="770" alt="image" src="https://github.com/user-attachments/assets/d058e92d-a7a7-439b-877f-64c38940401f" />
<img width="1917" height="877" alt="image" src="https://github.com/user-attachments/assets/4410c35a-12cb-4f86-986d-43e38681d414" />
<img width="1919" height="898" alt="image" src="https://github.com/user-attachments/assets/917d8e3f-3ceb-4125-a649-88c035914a04" />




## Usage

1. On the homepage, either drag a `.txt` file into the upload zone (or click to browse) — or paste text straight into the text box. A few one-click examples are provided if you just want to try it out.
2. Click **Analyze text**.
3. The page reloads showing the tagged text, an entity summary (counts, word count, density), and a legend you can click to filter which entity types are highlighted.
4. Click **Show original text** to compare against the untagged version.
