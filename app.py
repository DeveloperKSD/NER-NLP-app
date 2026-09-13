from flask import Flask, request, render_template
import spacy
from spacy import displacy
from collections import Counter
import re

nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

# Custom color palette for entity highlighting — deliberately avoids
# spaCy's default lavender/purple for PERSON and other purple-ish tones.
ENTITY_COLORS = {
    "PERSON": "#FF6B5B",
    "ORG": "#4DA8DA",
    "GPE": "#FFB84D",
    "LOC": "#6BCB77",
    "DATE": "#F4A6B7",
    "TIME": "#A0DED0",
    "MONEY": "#2E9E86",
    "PERCENT": "#FFD166",
    "ORDINAL": "#B5C99A",
    "CARDINAL": "#E0A96D",
    "NORP": "#EF767A",
    "FAC": "#7FB3D5",
    "PRODUCT": "#F7A072",
    "EVENT": "#90CAF9",
    "WORK_OF_ART": "#F9C74F",
    "LAW": "#577590",
    "LANGUAGE": "#43AA8B",
    "QUANTITY": "#F8961E",
}
DISPLACY_OPTIONS = {"colors": ENTITY_COLORS}


def add_entity_data_labels(html: str) -> str:
    """
    Adds a data-label="LABEL" attribute onto each displaCy <mark> tag so
    the front-end can filter/dim entities by type with plain CSS/JS.
    Doesn't touch how spaCy extracts or scores entities.
    """
    pattern = re.compile(
        r'(<mark class="entity"[^>]*>)(.*?)(<span[^>]*>)([A-Z_]+)(</span>\s*</mark>)',
        re.DOTALL,
    )

    def _inject(match):
        mark_open, content, span_open, label, tail = match.groups()
        mark_open_labeled = mark_open[:-1] + f' data-label="{label}">'
        return mark_open_labeled + content + span_open + label + tail

    return pattern.sub(_inject, html)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/entity', methods=['GET', 'POST'])
def entity():
    if request.method == 'POST':
        readable_file = None

        file = request.files.get('file')
        if file and file.filename:
            readable_file = file.read().decode('utf-8', errors='ignore')

        pasted_text = request.form.get('text_input', '').strip()
        if not readable_file and pasted_text:
            readable_file = pasted_text

        if readable_file:
            docs = nlp(readable_file)  # core NER call, unchanged
            html = displacy.render(docs, style='ent', jupyter=False, options=DISPLACY_OPTIONS)
            html = add_entity_data_labels(html)

            label_counts = Counter(ent.label_ for ent in docs.ents)
            entity_stats = sorted(label_counts.items(), key=lambda x: -x[1])
            total_entities = sum(label_counts.values())
            word_count = len(readable_file.split())
            entity_density = round((total_entities / word_count) * 100, 2) if word_count else 0

            return render_template(
                'index.html',
                html=html,
                text=readable_file,
                entity_stats=entity_stats,
                total_entities=total_entities,
                word_count=word_count,
                entity_density=entity_density,
                entity_colors=ENTITY_COLORS,
            )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
