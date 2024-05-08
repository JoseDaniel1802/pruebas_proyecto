def data_identificator_type(dato):
    if isinstance(dato, str):
        try:
            int(dato)
            return int
        except ValueError:
            try:
                float(dato)
                return float
            except ValueError:
                return str
    elif isinstance(dato, int):
        return int
    elif isinstance(dato, float):
        return float
    else:
        return str