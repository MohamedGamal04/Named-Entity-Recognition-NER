import streamlit as st
import spacy
from spacy import displacy

# Set page config
st.set_page_config(page_title="NER from News Articles", layout="wide")

# Title
st.title("Named Entity Recognition (NER) from News Articles")
st.markdown("Extract and visualize named entities from text using spaCy models")

# Load models
@st.cache_resource
def load_models():
    nlp_sm = spacy.load("core_web_sm_custom_ner_model")
    nlp_md = spacy.load("core_web_md_custom_ner_model")
    return nlp_sm, nlp_md

try:
    nlp_sm, nlp_md = load_models()
except OSError:
    st.error("Models not found. Install with: python -m spacy download en_core_web_sm en_core_web_md")
    st.stop()

# Sidebar for model selection
st.sidebar.header("Settings")
model_choice = st.sidebar.radio("Select Model", ["Small (SM)", "Medium (MD)"])
nlp = nlp_sm if model_choice == "Small (SM)" else nlp_md

# Text input
st.subheader("Input Text")
text_input = st.text_area("Enter text for entity extraction:", height=150, 
                          placeholder="Paste your news article here...")

if text_input:
    # Process text
    doc = nlp(text_input)
    
    # Display entities
    st.subheader("Extracted Entities")
    if doc.ents:
        entities_df = []
        for ent in doc.ents:
            entities_df.append({
                "Entity": ent.text,
                "Label": ent.label_,
                "Start": ent.start_char,
                "End": ent.end_char
            })
        st.dataframe(entities_df, use_container_width=True)
    else:
        st.info("No entities found in the text.")
    
    # Visualize with displacy
    st.subheader("Entity Visualization")
    colors = {
        "PERSON": "#FF6B6B",    # Red
        "ORG": "#4ECDC4",       # Teal
        "GPE": "#45B7D1",       # Blue
        "LOC": "#96CEB4",       # Green
        "MISC": "#FFEAA7"       # Yellow
    }
    options = {"colors": colors}
    html = displacy.render(doc, style="ent", page=True, minify=True , options=options)
    html_styled = f"""
    <div style='background-color: white; padding: 20px; border-radius: 8px; margin: 10px 0;'>
        {html}
    </div>
    """
    st.components.v1.html(html_styled, height=300, scrolling=True)
    
    # Entity statistics
    st.subheader("Entity Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Entities", len(doc.ents))
    with col2:
        st.metric("Unique Labels", len(set([ent.label_ for ent in doc.ents])))
    with col3:
        st.metric("Text Length", len(text_input))

else:
    st.info("👈 Enter text in the box above to extract entities")

# Footer
st.markdown("---")
st.markdown("Built with spaCy and Streamlit")