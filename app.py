import streamlit as st
from pathlib import Path

from readers import get_file_reader
from chuncker import split_text_into_chunks
from model_selector import get_translator
from pdf_constructor import create_pdf_from_text

# Configure the Streamlit page settings
st.set_page_config(page_title="Traductor de Documentos", page_icon="📚", layout="wide")

def translate_document(uploaded_file, model_name, use_chunks=False, chunk_size=2000):
    """
    Translate an uploaded document using the specified model and parameters.
    
    Args:
        uploaded_file: The file object to translate
        model_name: Name of the translation model to use
        use_chunks: Boolean indicating whether to split text into chunks
        chunk_size: Size of chunks when splitting text
        
    Returns:
        str: Path to the translated PDF file
    """
    # Save uploaded file to local storage
    input_path = f"uploads/{uploaded_file.name}"
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Initialize file reader and translator
    reader = get_file_reader(input_path)
    text = reader(input_path)
    translator = get_translator(model_name)
    
    # # Configure text chunking options
    # use_chunks = st.checkbox("Trocea el texto (recomendado para documentos muy grandes)", value=False)
    
    if use_chunks:
        # Process text in chunks for large documents
        chunk_size = st.number_input("Characters per chunk", min_value=500, max_value=10000, value=2000)
        chunks = split_text_into_chunks(text, chunk_size)
        translated_chunks = []
        
        # Show translation progress
        progress_bar = st.progress(0)
        total_chunks = len(chunks)
        
        for i, chunk in enumerate(chunks):
            translated_chunk = translator(chunk)
            translated_chunks.append(translated_chunk)
            progress = (i + 1) / total_chunks
            progress_bar.progress(progress)
            
        translated_text = ' '.join(translated_chunks)
    else:
        # Translate entire text at once
        progress_bar = st.progress(0)
        translated_text = translator(text)
        progress_bar.progress(100)
    
    # Generate output PDF with translation
    output_path = f"output/translated_{uploaded_file.name}"
    create_pdf_from_text(translated_text, output_path)
    return output_path

def main():
    """
    Main application function that handles the UI and translation workflow.
    """
    # Set up the main page title and description
    st.title("📚 Traductor de Documentos")
    st.write("Traduce tus documentos al Español - Rápido y Fácil!")

    # Create two-column layout
    col1, col2 = st.columns([2,1])
    
    with col1:
        # File upload section
        uploaded_file = st.file_uploader(
            "Arrastra y suelta tu archivo aquí o haz clic para seleccionar un archivo",
            type=['pdf', 'epub', 'txt'],
            help="Soporta PDF, EPUB and TXT files"
        )

    with col2:
        # Translation settings section
        model = st.selectbox(
            "Elige el modelo de traducción preferido",
            ["groq", "xAI", "ollama"],
            help="Elige tu modelo de traducción preferido"
        )
        use_chunks = st.checkbox("Selecciona para trocear tu documento.    \n(recomendado para documentos grandes)", value=False)
        if use_chunks:
            chunk_size = st.number_input("Caracteres por trozo", min_value=500, max_value=10000, value=2000)

    if uploaded_file and model:
        # Create necessary directories
        upload_dir = Path("uploads")
        translations_dir = Path("translations")
        output_dir = Path("output")
        
        # Create required directories for file processing
        for dir_path in [upload_dir, translations_dir, output_dir]:
            # Create each directory if it doesn't exist, skip if it does
            dir_path.mkdir(exist_ok=True)
        
        # Translation process
        if st.button("🚀 Traducir"):
            with st.spinner("Traduciendo..."):
                # When not using chunks, we can pass any value like 0 or 1
                chunk_size = chunk_size if use_chunks else 1
                output_pdf = translate_document(uploaded_file, model, use_chunks, chunk_size)
                
                # Provide download option for translated document
                with open(output_pdf, "rb") as pdf:
                    st.success("✨ Traducción completada!")
                    st.download_button(
                        "📥 Descargar traducción",
                        pdf,
                        file_name=f"translated_{uploaded_file.name}",
                    )

if __name__ == "__main__":
    main()

