from contextlib import contextmanager


@contextmanager
def hide_attributes(cls, args):
    stash = {arg: cls.__dict__.pop(arg) for arg in args}
    try:
        yield
    finally:
        cls.__dict__.update(stash)
