def split_text_into_chunks(text, chunk_size=2000):
    """
    Split input text into chunks of specified size while maintaining word boundaries.
    
    Args:
        text (str): The input text to be split into chunks
        chunk_size (int, optional): Maximum size of each chunk in characters. Defaults to 2000.
    
    Returns:
        list: A list of text chunks, each containing complete words and not exceeding chunk_size
    """
    # Split the input text into individual words
    words = text.split()
    # Initialize list to store final chunks
    chunks = []
    # Initialize list and counter for current chunk being built
    current_chunk = []
    current_length = 0
    
    # Process each word in the input text
    for word in words:
        # Calculate new length including the word and a space
        current_length += len(word) + 1  # +1 for space
        # If adding this word exceeds chunk size, store current chunk and start new one
        if current_length > chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_length = len(word)
        else:
            # Add word to current chunk if within size limit
            current_chunk.append(word)
    
    # Add the final chunk if any words remain
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks