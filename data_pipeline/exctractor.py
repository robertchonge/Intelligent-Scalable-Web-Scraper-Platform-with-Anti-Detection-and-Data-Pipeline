import logging

def process_data(data):
    """
    Validate and transform scraped data.
    For demo, we trim strings and ensure keys exist.
    """
    logging.info(f"Processing raw data: {data}")
    cleaned = {}
    if not data:
        logging.warning("No data to process")
        return

    cleaned['url'] = data.get('url', '').strip()
    cleaned['title'] = data.get('title', '').strip()
    cleaned['heading'] = data.get('heading', '').strip()

    # Here you could add more validation, type checking, or normalization.

    logging.info(f"Cleaned data ready for loading: {cleaned}")
    # For now, just print or save to DB/file
    print(cleaned)
