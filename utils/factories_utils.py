def enum_choices_factory(enum_cls):
    return tuple([(member.value, member.value) for name, member in enum_cls.__members__.items()])
