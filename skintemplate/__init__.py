from paste.script.templates import Template, var

class SkinTemplate(Template):

    _template_dir = 'template'
    summary = 'Skin skeleton'
    vars = [
        var('author', 'Author name', default='Think Thanks'),
    ]


