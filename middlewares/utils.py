def extract_unique_field_from_error(error):

    error_message = str(error.orig)

    if "violates unique constraint" in error_message:
        start_index = error_message.index("Key (") + 5
        end_index = error_message.index(")=(")
        unique_field = error_message[start_index:end_index]
        return unique_field

    return None
