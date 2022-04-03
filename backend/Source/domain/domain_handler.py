from Source.domain import model


def add_file(dict):
    return model.file_factory(
        name=dict["name"],
        source=dict["source"],
        parameters=dict["parameters"],
        placement_name=dict["placement_name"],
        effective_from=dict["effective_from"],
        effective_to=dict["effective_to"],
        active=dict["active"],
    )
