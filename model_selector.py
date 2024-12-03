from translator import translate_to_spanish_with_groq, translate_to_spanish_with_xAI, translate_to_spanish_with_ollama


def get_translator(model_name):
    """
    Returns the translation function corresponding to the specified model name.
    Args:
    model_name (str): The name of the model to use for translation.
    Returns:
    function: The translation function corresponding to the specified model name.
    """
    try:
        model_mapping = {
            "groq": translate_to_spanish_with_groq,
            "xAI": translate_to_spanish_with_xAI,
            "ollama": translate_to_spanish_with_ollama,
        }
        return model_mapping[model_name]
    
    except KeyError:
        raise ValueError(f"Invalid model name: {model_name}")
        
    