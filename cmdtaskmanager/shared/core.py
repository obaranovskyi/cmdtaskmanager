def entity_to_repr(entity, name, keys):
    key_value = []
    for key in keys:
        key_value.append(f"{key}={getattr(entity, key)}")
    return f"<{name}(" + \
           ", ".join(key_value) + \
           f")>"
